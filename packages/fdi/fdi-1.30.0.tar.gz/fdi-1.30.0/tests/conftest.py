# -*- coding: utf-8 -*-


from werkzeug.datastructures import Authorization
from fdi.dataset.testproducts import get_demo_product, get_related_product
from fdi.dataset.classes import Class_Look_Up
from fdi.dataset.deserialize import deserialize
from fdi.pal.poolmanager import PoolManager
from fdi.pal.productstorage import ProductStorage
from fdi.pns.jsonio import getJsonObj
from fdi.pns.fdi_requests import reqst
from fdi.pns.public_fdi_requests import read_from_cloud
from fdi.utils.common import lls
from fdi.pns.jsonio import auth_headers
from fdi.httppool.model.user import User, getUsers
from fdi.httppool.session import requests_retry_session
from fdi.pal.publicclientpool import PublicClientPool

from fdi.pal.poolmanager import dbg_7types


from flask.testing import FlaskClient
from flask import request

from requests.auth import HTTPBasicAuth
import pytest
import importlib
from urllib.error import HTTPError
import requests
import os
import sys
import json
import time
import copy
import getpass
import shlex
import signal
import datetime
import requests
from subprocess import Popen, TimeoutExpired
import logging
import logging.config
from urllib.error import HTTPError, URLError

# from logdict import logdict
# logging.config.dictConfig(logdict)

logger = logging.getLogger(__name__)
print('**conftest effective logging level** ', logger.getEffectiveLevel())
EX = ' -l /tmp/foo.log'

RUN_SERVER_IN_BACKGROUND = 'python3.8 httppool_app.py --server=httppool_server'
""" set to '' to disable running a pool in the background as the mock. """


TEST_SERVER_LIFE = 600
""" test server time limit in seconds."""

the_session = requests.session()
the_session.secret_key = 'BAD_SECRET_KEY'


@ pytest.fixture(scope='session')
def clean_board():
    importlib.invalidate_caches()
    # importlib.reload(Classes)
    from fdi.dataset.classes import Classes
    return Classes.mapping


pns = None


@ pytest.fixture(scope="session")
def pc():
    """ get configuration.

    """
    global pns
    from fdi.utils.getconfig import getConfig as getc
    pns = getc(force=True)
    # logger.debug(json.dumps(pns))

    return pns


@ pytest.fixture(scope="session")
def mock_in_the_background():

    return RUN_SERVER_IN_BACKGROUND


######


SHORT = 'function'


@ pytest.fixture(scope=SHORT)
def new_user_read_write(pc):
    """
    GIVEN a User model
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
    """
    new_user = User(pc['username'], pc['password'], roles='read_write')
    headers = auth_headers(pc['username'], pc['password'])
    return new_user, headers


@ pytest.fixture(scope=SHORT)
def new_user_read_only(pc):
    """
    GIVEN a User model
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
    """
    users = getUsers(pc)
    new_user = users[pc['ro_user']]
    headers = auth_headers(pc['ro_user'], password=pc['ro_pass'])

    return new_user, headers


@ pytest.fixture(scope=SHORT)
def userpass(pc):
    auth_user = pc['username']
    auth_pass = pc['password']
    return auth_user, auth_pass


@ pytest.fixture(scope="module")
def local_pools_dir(pc):
    """ this is a path in the local OS, where the server runs, used to directly access pool server's internals.

    return: has no trailing '/'
    """
    # http server pool
    schm = 'server'

    # basepath = pc['server_local_pools_dir']
    # basepath = PoolManager.PlacePaths[schm]
    # print('WWW ', basepath, pc['api_version'])
    # pools_dir = os.path.join(basepath, pc['api_version'])
    return PoolManager.PlacePaths[schm]

####


@ pytest.fixture(scope="session")
def mock_app(pc, mock_in_the_background):
    if mock_in_the_background:
        yield None
    else:
        from fdi.httppool import create_app
        app = create_app(config_object=pc, level=logger.getEffectiveLevel())
        app.config['TESTING'] = True
        with app.app_context():
            yield app
            # app.


def background_app():
    """ if requied starts a server in the background. """

    # client side.
    # pool url from a local client
    cschm = 'http'
    aburl = cschm + '://' + PoolManager.PlacePaths[cschm]
    pwdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    pid = os.fork()
    if pid == 0:
        # child process
        # ref https://code.activestate.com/recipes/66012-fork-a-daemon-process-on-unix/
        os.setsid()
        # Redirect standard file descriptors.
        sys.stdin = open('/dev/null', 'r')
        sys.stdout = open('/dev/null', 'w')
        sys.stderr = open('/dev/null', 'w')
        # run server in b/g
        chldlogger = logger
        cmd = shlex.split(RUN_SERVER_IN_BACKGROUND)
        sta = {'command': str(cmd)}
        proc = Popen(cmd, cwd=pwdir, shell=False)
        timeout = TEST_SERVER_LIFE
        try:
            sta['stdout'], sta['stderr'] = proc.communicate(
                timeout=timeout)
        except TimeoutExpired:
            # https://docs.python.org/3.6/library/subprocess.html?highlight=subprocess#subprocess.Popen.communicate
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            msg = 'PID %d is terminated after pre-set timeout %d sec.' % (
                proc.pid, timeout)
        else:
            msg = 'Successful.' if proc.returncode == 0 else 'killed?'
        sta['stdout'], sta['stderr'] = proc.communicate()
        sta['returncode'] = proc.returncode

        sta['message'] = msg
        logg = "Background live server status: %s." % json.dumps(
            dict((k, lls(v, 1000)) for k, v in sta.items()))
        chldlogger.info(logg)
        with open('/tmp/bar.log', 'a') as f:
            f.write(logg)

        assert sta['returncode'] in (
            0, -signal.SIGTERM, -signal.SIGKILL,  signal.SIGHUP), logg
        time.sleep(10000)  # avoid trouble for pytest
        sys.exit(0)
    else:
        # main process
        # wait for checkserver to return 'live'
        time.sleep(2)
        n = 2
        while checkserver(aburl) != 'live':
            logger.debug('No server yet %d' % n)
            n -= 1
            if n == 0:
                break
            time.sleep(2)
        if n:
            msg = 'Made live local server %d' % pid
        else:
            msg = 'Failed running server PID=%s in background. n=%s.' % (
                str(pid), str(n))
        logger.info(msg)
        return pid


def checkserver(aburl):
    """ make sure the server is running when tests start.

    Parameters
    ----------

    Return
    ------
    str
        when aburl points to an live server running either externally to this test (e.g. by `make runpoolserver`), or a server instance by `background_app` fixture created on-demand, server_type is set to 'live'; If no response is returned by `GET`, 'mock' is returned; If server response is abnormal, 'trouble' is returned.
    """

    server_type = None

    # check if data already exists
    try:
        o = getJsonObj(aburl)
        assert o is not None, 'Cannot connect to the server'
        logger.info('Initial server %s response %s' % (aburl, lls(o, 70)))
    except HTTPError as e:
        if e.code == 308:
            logger.info('%s alive. Server response 308' % (aburl))
            server_type = 'live'
        else:
            logger.warning(aburl + ' is alive. but trouble is ')
            logger.warning(e)
            logger.warning('Live server')
            server_type = 'trouble'
    except URLError as e:
        logger.info('Not a live server, because %s' % str(e))
        server_type = 'mock'
    else:
        logger.info('Live server')
        server_type = 'live'
    return server_type

    # assert 'measurements' is not None, 'please start the server to refresh.'
    # initialize test data.


@ pytest.fixture(scope="session")
def live_or_mock(pc, mock_in_the_background, mock_app):
    """ Prepares server absolute base url and common headers for clients to use.

    Based on ``PoolManager.PlacePaths[scheme]`` where ``scheme`` is `http` or `https` and auth info from `pnsconfig` from the configuration file and commandline.

    e.g. ```'http://0.0.0.0:5000/v0.7/', ('foo', 'bar')```

    Return
    ------
    tuple:
       baseurl with no trailing '/' and a string set to 'live' if the
       server os alive, 'mock' if the server is not useable as it is.

    """
    server_type = None

    # client side.
    # pool url from a local client
    cschm = 'http'
    aburl = cschm + '://' + PoolManager.PlacePaths[cschm]
    logger.debug('Check out %s ...' % aburl)
    server_type = checkserver(aburl)
    if server_type == 'mock':
        if mock_in_the_background:
            pid = background_app()
            # None means no mock_in_the_background
            assert pid is not None
            server_type = 'live'
            yield aburl, server_type

            if pid > 0:
                logger.info(
                    'Killing server PID=%d running in the background.' % pid)
                kpg = os.killpg(os.getpgid(pid), signal.SIGTERM)
                logger.info('... killed. rc= %s' % str(kpg))

    elif server_type == 'live':
        yield aburl, server_type
    else:
        logger.error('Invalid server state '+server_type)
        assert 0


@ pytest.fixture(scope=SHORT)
def server(live_or_mock, new_user_read_write):
    """ Server data from r/w user, mock or alive.

    """
    aburl, ty = live_or_mock
    user, headers = new_user_read_write
    headers['server_type'] = ty
    yield aburl, headers


@ pytest.fixture(scope=SHORT)
def server_ro(live_or_mock, new_user_read_only):
    """ Server data from r/w user, alive.

    """
    aburl, ty = live_or_mock
    user, headers = new_user_read_only
    headers['server_type'] = ty
    yield aburl, headers
    del aburl, headers


@ pytest.fixture(scope="module")
def request_context(mock_app):
    """create the app and return the request context as a fixture
       so that this process does not need to be repeated in each test
    https://stackoverflow.com/a/66318710
    """

    yield mock_app.test_request_context


@ pytest.fixture(scope="module")
def client(live_or_mock, mock_app):

    a, server_type = live_or_mock
    if server_type == 'live':
        logger.info('**** requests as client *****')
        with the_session as live_client:
            yield live_client
    elif server_type == 'mock':
        logger.info('**** mock_app as client *****')
        with mock_app.test_client() as client:
            if 0:
                with mock_app.app_context():
                    mock_app.preprocess_request()
            yield client
    else:
        raise ValueError('Invalid server type: ' + server_type)

# @pytest.fixture(scope="module")
# async def a_client(aiohttp_client, server_app, mock_app):
#    if server_app == None:
#        yield aiohttp_client(requests)
#    else:
#        logger.info('**** mock_app as client *****')
#        with mock_app.test_client() as client:
#            with mock_app.app_context():
#                # mock_app.preprocess_request()
#                assert current_app.config["ENV"] == "production"
#            yield aiohttp_client(client)


@ pytest.fixture(scope='module')
def demo_product():
    v = get_demo_product()
    return v, get_related_product()


csdb_pool_id = 'sv2'  # 'test_csdb_fdi2'
url_c = None


@ pytest.fixture(scope="session")
def urlcsdb(pc):
    global url_c

    url_c = '%s://%s:%d%s/%s' % (pc['scheme'],
                                 pc['cloud_host'],
                                 pc['cloud_port'],
                                 pc['cloud_api_base'],
                                 pc['cloud_api_version'])
    return url_c


def make_csdb(poolurl):
    # client = requests_retry_session()

    ps = ProductStorage()
    if PoolManager.size():
        logger.debug("$$$ PM not empty")
    ps.unregisterAll()
    assert ps.isEmpty()
    assert PoolManager.size() == 0

    return ps


def do_clean_csdb():
    urlcsdb = url_c
    pc = pns
    url = pc['cloud_scheme'] + urlcsdb[len('csdb'):] + '/' + csdb_pool_id

    # register to clean up
    ps = ProductStorage()
    ps.PM.removeAll()

    ps.register(poolurl=url, client=the_session, auth=auth)
    # ps.register(poolname=test_pool.poolname, poolurl=poolurl)
    test_pool = ps.getWritablePool(True)  # PublicClientPool(poolurl=url)
    pname = test_pool._poolname
    assert test_pool.serverDatatypes

    ######
    if dbg_7types:
        tl = test_pool.getDataType(substrings='testproducts')
        print('+'*21, len(tl), tl)

    if 0:
        test_pool.wipe()
    else:
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        header['X-AUTH-TOKEN'] = test_pool.token
        requestAPI = 'http' + urlcsdb[len('csdb'):] + \
            f'/pool/delete?resetSN=1&storagePoolName='+csdb_pool_id
        #######
        if dbg_7types:
            tl = test_pool.getDataType(substrings='testproducts')
            print('<'*21, len(tl), tl)

        res = reqst(test_pool.client.post, requestAPI, headers=header,
                    server_type='csdb')
        assert res is None
        #######
        if dbg_7types:
            tl = test_pool.getDataType(substrings='testproducts')
            print('>'*21, len(tl), tl)

    assert pname in PoolManager.getMap()
    assert pname in ps._pools

    assert test_pool.isEmpty()

    ####
    if dbg_7types:
        tl = test_pool.getDataType(substrings='testproducts')
        print('.'*21, len(tl), tl)

    # unregister. this will set test_pool.serverDatatypes to None
    ps.unregister(pname)
    assert not ps.PM.isLoaded(pname)
    assert ps.isEmpty()
    assert test_pool.serverDatatypes == []

    # re-register the wiped pool
    ps.register(poolurl=url, client=the_session, auth=auth)
    assert ps.PM.isLoaded(pname)
    test_pool = ps.getWritablePool(True)

    assert test_pool.serverDatatypes
    if 0 and hasattr(test_pool, 'serverDatatypes'):
        logger.info(
            f"@{pname}.serverDatatypes={sorted(test_pool.serverDatatypes)}")

    return test_pool, url, ps


@ pytest.fixture(scope=SHORT)
def clean_csdb_fs(clean_csdb):
    return do_clean_csdb()


@ pytest.fixture(scope="session")
def clean_csdb(urlcsdb, pc):
    return do_clean_csdb()


@ pytest.fixture(scope=SHORT)
def new_csdb(urlcsdb, pc):
    logger.debug('wipe cdb_new. {purl}')
    url = pc['cloud_scheme'] + \
        urlcsdb[len('csdb'):] + '/' + csdb_pool_id + str(int(time.time()))
    # url = pc['cloud_scheme'] + urlcsdb[len('csdb'):] + '/' + csdb_pool_id
    ps = make_csdb(url)
    ps.register(poolurl=url, client=the_session, auth=auth)
    pool = ps.getWritablePool(True)  # PublicClientPool(poolurl=url)
    poolname = pool._poolname
    assert ps.PM.isLoaded(poolname)
    if hasattr(pool, 'serverDatatypes'):
        logger.debug(f"{poolname}.serverDatatypes={pool.serverDatatypes}")
    if dbg_7types:
        tl = pool.getDataType(substrings='testproducts')
        print('.'*21, len(tl), tl)

    yield pool, url, ps


@ pytest.fixture(scope='session')
def csdb(clean_csdb):

    return clean_csdb


@ pytest.fixture(scope=SHORT)
def tmp_local_storage(tmp_path_factory):
    """ temporary local pool """

    tmppath = tmp_path_factory.mktemp('pools')
    cschm = 'file'
    pdir = str(tmppath.parent)  # PoolManager.PlacePaths[cschm]
    aburl = cschm + '://' + pdir
    poolid = str(tmppath.name)

    pool = PoolManager.getPool(poolid, aburl + '/' + poolid)
    ps = ProductStorage(pool)
    yield ps


@ pytest.fixture(scope=SHORT)
def tmp_remote_storage_no_wipe(server, client, auth):
    """ temporary servered pool with module scope """
    aburl, headers = server
    poolid = 'test_remote_pool'

    pool = PoolManager.getPool(
        poolid, aburl + '/' + poolid, auth=auth, client=client)
    ps = ProductStorage(pool, client=client, auth=auth)
    assert issubclass(ps.getPool(poolid).client.__class__,
                      (requests.Session, FlaskClient))
    yield ps, pool


@ pytest.fixture(scope=SHORT)
def tmp_remote_storage(tmp_remote_storage_no_wipe):
    """ temporary servered pool wiped """
    ps, pool = tmp_remote_storage_no_wipe
    pool.removeAll()
    yield ps


@ pytest.fixture(scope="session")
def tmp_prod_types():
    """ classe of temporary prods with sesion scope """
    ptypes = []
    pobjs = []
    for n in ('DemoProduct', 'TB', 'TP', 'TC', 'TM', 'SP', 'TCC'):
        cls = Class_Look_Up[n]
        pobjs.append(cls())
        ptypes.append(cls)
    return ptypes, pobjs


PRD0_ser = get_demo_product('test-product-0: Demo_Product')
array_ser = Class_Look_Up['ArrayDataset']()


@ pytest.fixture(scope='session')
def tmp_prods(tmp_prod_types):
    """ instances of temporary prods with function scope """
    types, seri = tmp_prod_types
    while True:
        prds = [copy.deepcopy(PRD0_ser)]
        for i, n in enumerate(seri):
            if i == 0:
                continue
            p = copy.deepcopy(n)
            p.description = ('test-product-%d: %s' % (i, n))
            a = copy.deepcopy(array_ser)
            a.data = [[time.time(), n], 's']
            p['the_data'] = a
            prds.append(p)
        logger.debug("Made products: %s" %
                     str(list((p.description, id(p)) for p in prds)))
        res = tuple(prds)
        return res


@ pytest.fixture(scope=SHORT)
def auth(userpass, live_or_mock):

    a, server_type = live_or_mock
    if server_type == 'live':
        return HTTPBasicAuth(*userpass)
    else:
        return Authorization(
            "basic", {"username": userpass[0], "password": userpass[1]})


def gen_pools(url, auth, client, prds):

    tag = str(datetime.datetime.now())
    lst = []
    # n = len(prds)
    n = 2
    for i in range(n):
        poolid = 'test_%d' % i
        poolurl = url + '/' + poolid
        ps = ProductStorage(poolid, poolurl, client=client, auth=auth)
        # the first pool in ps
        pool = ps.getPool(poolid)
        pool.wipe()
        prd = prds[i]
        prd.description = 'lone prod in '+poolid
        ref = ps.save(prd, tag=tag)
        lst.append((pool, prd, ref, tag))
    return lst


@ pytest.fixture(scope=SHORT)
def tmp_pools(server, client, auth, tmp_prods):
    """ generate n pools.

    Return
    ------
    list
        list of tuples containing `ProductPool`, `BaseProduct`, `ProductRef`, `str` for each pool.

"""
    aburl, headers = server
    lst = gen_pools(aburl, auth, client, list(tmp_prods))
    return lst


@ pytest.fixture(scope=SHORT)
def tmp_local_remote_pools(server, client, auth, tmp_prods):
    """ generate n local pools.

    Return
    ------
    list
        list of tuples containing `ProductPool`, `BaseProduct`, `ProductRef`, `str` for each pool.

"""
    aburl, headers = server
    if not aburl.startswith('file://') and not '://127.0.0.1' in aburl and not '://0.0.0.0' in aburl:
        raise ValueError('must be a pool running locally. not %s.' % aburl)
    lst = gen_pools(aburl, auth, client, list(tmp_prods))
    return lst


@ pytest.fixture(scope=SHORT)
def existing_pools(tmp_pools):
    """ return n existing pools.

    Return
    ------
    list
        list of tuples containing `ProductPool`, `BaseProduct`, `ProductRef`, `str` for each pool.

"""
    pools = [p[0] for p in tmp_pools]
    print("get existing pools:", [p.poolname for p in pools])
    return pools

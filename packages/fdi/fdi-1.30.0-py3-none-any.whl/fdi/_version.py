__version_info__ = (1, 30, 0)
__version__ = '.'.join(map(str, __version_info__))
# 1.30.0 GlobalPoolList not weakref anymore, working with server sessions. make login/out, saved cookies work. efficient update of pool HK by csdb backend. improve conftest efficiency for csdb.
# 1.29.0  Implement CSDB pool on HTTPpool v0.16, with secondary_url w/ fxed currentSN in csdb pool api /pool/delete.
# 1.28.3 arrange the order of parameters in yamt2python output.
# 1.28.2 tofits ans image.py adapted to latest pipeline_l1
# 1.28.1 fix 'set' bug and currentSN->0 bugs in pool; add set to serializable, csdb pool, tag and other working.
# 1.28.0 csdb overaul and asynhttp. bug fixes,
# 1.27.0 list input to `remove` localpool and subclasses. async io for HttpClientPool
# 1.26.2 Implement namespace-based getConfig(). Fix unregister bug in PS.remove()
# 1.26.1 simplify user config for httppool.
# 1.26.0 relate the 104 Connection Reset error to auto redirect to trailing '/' url. Add '/' to endpoints. add "/pools" to show pool info.
# 1.25.4 threaded test code. local httppool read/write prod 20-30ms
# 1.25.3 refactor query code
# 1.25.2 server remote debug
# 1.25.1 externalize docker tests.
# 1.25.0 getConfig and configuration improvement
# 1.24.4 requets timeout; logger_level_extras; single thread and python3.8 in wsgi; other improvement to get self-test pass for server docker.
# 1.24.3 improved config.py for docker, RW_USER, missing templates.
# 1.24.2 session works and all tests with live (fore/background) pools, w or w/o session. py3.9 in readthdoc.yml.'
# 1.24.1 intersphinx enabled for docs.
# 1.24.0 session for httppool, testing wih live mock server
# 1.23.1 greatly simplfies MetaData.toString with new Python-tabulate.
# 1.23.0 session and templates for httppool; extra fixed.
# 1.22.3 History docs and working on server
# 1.22.2 improve yaml2python parent sort; implement history tracing; Documents layout fix; Parameter takes anything as value unchecked.

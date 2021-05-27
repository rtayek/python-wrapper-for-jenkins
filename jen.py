#https://python-jenkins.readthedocs.io/en/latest/index.html
#pip install python-jenkin
import jenkins
def getServer(address="192.168.1.6",port='8081',timeout=5):
    server = jenkins.Jenkins('http://'+address+':'+port, username='raz', password='11213')
    if not server.wait_for_normal_op(30): print("Jenkins failed to be ready in sufficient time"); exit(2)
    return server
def names(l,name="name"): return [x[name] for x in l]
def info(server):
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    print(server.jobs_count(),"jobs.")
    jobs = server.get_jobs()
    plugins = server.get_plugins_info()
    print(len(plugins),'plugins.')
    #print(len(plugins),'plugins:',names(plugins,name='shortName'))
    return jobs
server = getServer()
info(server)

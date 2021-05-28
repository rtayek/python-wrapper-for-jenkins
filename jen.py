#https://python-jenkins.readthedocs.io/en/latest/index.html
#pip install python-jenkin
import sys
import jenkins
def getServer(address="192.168.1.6",port='8081',timeout=5,user="admin",password="admin"):
    server=jenkins.Jenkins('http://'+address+':'+port, username=user, password=password)
    if not server.wait_for_normal_op(30): print("Jenkins failed to be ready in sufficient time"); exit(2)
    return server
def names(l,name="name"): return [x[name] for x in l]
def getInfo(server):
    user=server.get_whoami()
    version=server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    print(server.jobs_count(),"jobs.")
    jobs=server.get_jobs()
    print('jobs:',names(jobs))
    plugins=server.get_plugins_info()
    print(len(plugins),'plugins.')
    #print(len(plugins),'plugins:',names(plugins,name='shortName'))
    return jobs
def main():
    if len(sys.argv)<2: raise Exception("user and password please")
    server=getServer(user=sys.argv[1],password=sys.argv[2])
    jobs=getInfo(server)
    try: server.create_node('foo')
    except Exception as e: print(str(e)[:80])
if __name__ == "__main__": main()

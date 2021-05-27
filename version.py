import jenkins

server = jenkins.Jenkins('http://localhost:8081', username='raz', password='11213')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
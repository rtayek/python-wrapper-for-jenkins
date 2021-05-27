import jen
server=jen.getServer()
name='agent-1-from-python'
try: server.create_node(name)
except Exception as e:
    print(e.__class__)
    print(format(e))
    exit(0)
nodes = server.get_nodes()
#print(nodes)
node_config = server.get_node_info(name)
print(node_config)
server.disable_node(name)
server.enable_node(name)

# create node with parameters
params = {
    'port': '22',
    'username': 'juser',
    'credentialsId': '10f3a3c8-be35-327e-b60b-a3e5edb0e45f',
    'host': 'my.jenkins.slave1'
}
exit(0)
server.create_node(
    'slave1',
    nodeDescription='my test slave',
    remoteFS='/home/juser',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)
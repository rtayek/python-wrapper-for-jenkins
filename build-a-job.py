import jen
server=jen.getServer()
jobs = server.get_jobs()
jobNames=jen.names(jobs)
print(jobNames)
#name='agent-1-from-python'
name='fs-python-1'
server.build_job(name)

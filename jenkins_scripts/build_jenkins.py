from api4jenkins import Jenkins
from time import sleep
from datetime import datetime

time = datetime.today()
time_ = datetime.strftime(time, '%Y-%b-%d_%H%M%S')
filename = f'jenkins_log_{time_}.log'
file = open(filename, 'w+')
j = Jenkins('http://127.0.0.1:8080/', auth=('admin', 'admin'))

job = j.get_job('RedactorZone_testing')
print(job)

item = job.build()

while not item.get_build():
    sleep(1)

build = item.get_build()

print(build)

for line in build.progressive_output():
    file.write(line)

file.write(str(build.building))
file.write(str(build.result))
file.close()
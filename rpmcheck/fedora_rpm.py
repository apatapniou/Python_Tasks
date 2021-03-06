import re
import wget
file_new = open('/home/apatapniou/Work/test/curlgrep')
rpmname = []
rpmname_new = []

file_old = open('/home/apatapniou/Work/test/installed_rpm', 'r+')
site = 'http://mirror.datacenter.by/pub/fedoraproject.org/linux/releases/29/Everything/x86_64/os/Packages/k/%s'

for line in file_old:
    result = ''.join(re.findall(r'kernel-.*.rpm', line))
    time = ''.join(re.findall(r'\d{2}-\w+-\d+.\w+:\d{2}', line))
    rpmname.append(result + ' ' + time)

for line in file_new:
    result_new = ''.join(re.findall(r'href=\"(kernel-.*?)"\>', line))
    time_new = ''.join(re.findall(r'href=\"kernel-.*?"\>.*(\d{2}-\w+-\d+.\w+:\d{2})', line))
    rpmname_new.append(result_new + ' ' + time_new)

diffrpm = list(set(rpmname_new).difference(set(rpmname)))

for i in range(len(diffrpm)):
    rpm = ''.join(re.findall(r'kernel-.*.rpm', diffrpm[i]))
    url = site % rpm
    wget.download(url, '/home/apatapniou/Work/test/%s' % (rpm))
    file_old.write(diffrpm[i] + "\n")

file_old.close()
file_new.close()

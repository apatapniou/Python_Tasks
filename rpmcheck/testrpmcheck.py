import re
import wget
f = open('C:\\Users\Aliaksandr_Patapniou\Documents\\test.txt')
rpmlits = []
for line in f:
    result = re.findall(r'href=\"(.*?)"\>', line)
    r = ''.join(result)
    url = 'https://rpmfind.net/linux/fedora/linux/updates/29/Everything/aarch64/Packages/k/%s' % (r)
    rpmlits.append(url)
print(rpmlits)

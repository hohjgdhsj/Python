import re

txt = open('/root/other/password.txt').read()

for x in re.findall('username=(.*?)&password=(.*?)[&?\s]', txt):
    print '\t'.join(x)

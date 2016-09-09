import sys, re, os, paramiko


search_address = re.compile(r'\w*,\w*@\w*:\w*')   # pattern for search remote name or IP
search_path = re.compile('\/+.*')                # pattern for search path 1st-from-path 2nd-dest-path
search_opts = re.compile(r'\-+.*')               # pattern for search opts for rsync(need more check)
search_passwd = re.compile('[p][a][s].*')        # pattern for optional -pass
search_IP = re.compile(r'^[^@]*')                # get ip from address
path = []
opts = []

for args in sys.argv:
    try:
        passwd = search_passwd.findall(args)
        path.append(search_path.search(args).group())
        address = search_address.search(args).group()
        opts.append(search_opts.search(args).group())
        ip = (search_IP.search(address).group())
    except:
        print ('---')

response = os.system("ping -c 1 " + ip)
if response == 0:                 # check the response...
    print ip, 'is up!'
else:
    print ip, 'is down!'


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # need check installed rsync on remote
client.connect(hostname=ip, username=address, password=passwd) # sudo apt-get install rsync or sudo yum -y install rsync
stdin, stdout, stderr = client.exec_command('sudo apt-get install rsync | sudo yum -y install rsync')
stdin.write(passwd)
stdin.flush()
data = stdout.read() + stderr.read()
client.close()


import os
def pinger():
    x=1
    good_ip = []
    try:
        for _ in range(0,200):
            response = os.system('ping -c 1 192.168.6.{}'.format(x))
            x+=1
            if response == 0:
                good_ip.append(x )
    except:
        pass


ping = pinger()

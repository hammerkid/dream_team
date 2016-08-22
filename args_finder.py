import re
import sys

def passwd_arg():
    search_passwd = re.compile(r'\b[p][a][s].*')
    for args in sys.argv:
        #print args
        try:
            passwd = ('-' + search_passwd.search(args).group())
            return passwd
        except:
            pass

#a = passwd_arg()
#print a



def opts_arg():
    allow_opts = ['P', 'a', 'v', 'S', 'z', 'q', 'progress', 'e']
    opts = []
    search_opts = re.compile(r'\-+.*')
    for args in sys.argv:
        try:
            x=[]
            opts = (search_opts.search(args).group())
            for opt in opts:
                if opt in allow_opts:
                    x.append(opt)
                    print x
        except:
            pass


optsx = opts_arg()
print optsx

def path_arg():
    path = []
    search_path = re.compile('\/+.*')
    for args in sys.argv:
        try:
            path.append(search_path.search(args).group())
            return path
        except:
            pass


def IP_arg():
    search_IP = re.compile(r'\w*,\w*@\w*:\w*')
    for args in sys.argv:
        try:
            IP = search_IP.search(args).group()
            return IP
        except:
            pass



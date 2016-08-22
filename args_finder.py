import re
import sys

def passwd_arg():   #find and return password
    search_passwd = re.compile(r'\b[p][a][s].*')    #pattern for password search
    for args in sys.argv:
        #print args
        try:
            passwd = ('-' + search_passwd.search(args).group())
            return passwd
        except:
            pass

#a = passwd_arg()
#print a



def opts_arg():        #search for options for rsyc(need improve with allow opts)
    allow_opts = ['P', 'a', 'v', 'S', 'z', 'q', 'progress', 'e']
    opts = []
    search_opts = re.compile(r'\-+.*')        #pattern for search options starts with -
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

def path_arg():    #find path in args
    path = []
    search_path = re.compile('\/+.*') #pattern for search path
    for args in sys.argv:
        try:
            path.append(search_path.search(args).group())
            return path  #1st in list is from path 2nd is dest path
        except:
            pass


def IP_arg():    #search for IP and name of remote machine
    search_IP = re.compile(r'\w*,\w*@\w*:\w*')  #pattern for IP and name
    for args in sys.argv:
        try:
            IP = search_IP.search(args).group()
            return IP
        except:
            pass



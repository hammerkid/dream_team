import sys
import re

search_IP = re.compile(r'\w*,\w*@\w*:\w*')       #pattern for search remote name or IP
search_path = re.compile('\/+.*')                #pattern for search path 1st-from-path 2nd-dest-path
search_opts = re.compile(r'\-+.*')               #pattern for search opts for rsync(need more check)
search_passwd = re.compile('[p][a][s].*')        #pattern for optional -pass
path = []
opts = []
#passwd =''
for args in sys.argv:

    #print args
    try:
         passwd = search_passwd.findall(args)
         print passwd
         path.append(search_path.search(args).group())
         print path
         IP = search_IP.search(args).group()
         print IP
         opts.append(search_opts.search(args).group())
         print opts


    except:
        print ('---')



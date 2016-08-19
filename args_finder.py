import sys

path_list = []

for argument in sys.argv:
    if '@' and ':' or ',' or '.'  in argument:
        IP_adress = argument
        print IP_adress
    if argument.startswith('-'):
        rsync_opt = argument
    if '/' in argument:
        path_list.append(argument)
    if '.txt' in argument:
        txt_file = argument
    if '.avi' in argument:
        avi_file = argument

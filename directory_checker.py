import os

# We need to connect to remote host, than check for existing file / directory
def check_dir_exist(os_dir):
    if not os.path.exists(os_dir):
        print os_dir, "does not exist."
    else:
        # This command copies data recursively from local host to remote host
        os.system("rsync -avrz /opt/data/filename root@ip:/opt/data/file")
                # -r copies data recursively
                #- v verbose
                #- a : archive mode, archive mode allows copying files recursively and it also
                #  preserves symbolic links, file permissions, user & group ownerships and timestamps
                #-z : compress file data
                # --exclude=PATTERN       exclude files matching PATTERN
                # --exclude-from=FILE     read exclude patterns from FILE
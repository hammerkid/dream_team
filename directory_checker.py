import os
import subprocess
subprocess.call(["rsync", "10.0.2.54", "-rvazh", "/usr/src","/usr/src/",])

# We need to connect to remote host, than check for existing file / directory
#def check_dir_exist(os_dir):
    #if not os.path.exists(os_dir):
       # print os_dir, "does not exist."
    #else:
        # This command copies data recursively from local host to remote host
     #   os.system("rsync -avrz /opt/data/filename root@ip:/opt/data/file")
                # -r copies data recursively
                #- v verbose
                #- a : archive mode, archive mode allows copying files recursively and it also
                #      preserves symbolic links, file permissions, user & group ownerships and timestamps
                #-z : compress file data
                # --exclude=PATTERN       exclude files matching PATTERN
                # --exclude-from=FILE     read exclude patterns from FILE
                # Exclude a specific file type rsync -avz --exclude '*.txt' source/ destination/
                # Excluding from a List in a File
                #      rsync --exclude-from=/path/to/exclusion-file /path/to/source /path/to/dest
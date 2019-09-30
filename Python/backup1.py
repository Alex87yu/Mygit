#!/usr/bin/python

# Filename: backup1.py

import os

import time

# 1. The files and directories to be backed up are specified in a list.

source = ['/data/data/com.termux/files']
''' If you are using Windows, use source =
[r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup

directory
'''
target_dir = '/sdcard/backup/'

''' Remember to change this

to what you will be using

# 3. The files are backed up into a zip file.

# 4. The name of the zip archive is the current date and

time'''
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file

comment = input('Enter a comment --> ')

if len(comment) == 0: # check if a comment was entered
  target = today + os.sep + now + '.zip'

else:
  target = today + os.sep + now + '_' + \

            comment.replace(' ', '_') + 'tar.gz'     # Notice the backslash!




#target = target_dir + time.strftime('%Y%m%d%H%M%S') +'termux-backup.tar.gz'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive

tar_command = "tar -zcvf '%s' %s" % (target, ' '.join(source))

# Run the backup

if os.system(tar_command) == 0:

    print ('Successful backup to', target)

else:

    print ('Backup FAILED')

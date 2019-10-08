#!/usr/bin/python
# Filename: backup2.py
import os
import time

# 1. The files and directories to be backed up are specified in a list.

source = ['/data/data/com.termux/files']
# If you are using Windows, use source =[r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory/today make a new dir if today is not exist.

target_dir = '/sdcard/backup/'

#Remember to change this to what you will be using
# 3. The files are backed up into a tar file.

# 4. The name of the tar archive is commence +  the current time

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file

comment = input('Enter a comment --> ')

if len(comment) == 0: # check if a comment was entered
  target = today + os.sep + now + '_termux.tar.gz'#os.sep means / . \ accodding to diff OS
else:
  target = today + os.sep + now + '_' + \
comment.replace(' ', '_') + '_termux.tar.gz'     # Notice the backslash!
#using '_' instead of ' ' to filename 

#target = target_dir + time.strftime('%Y%m%d%H%M%S') +'termux-backup.tar.gz'

#Create the subdirectory if it isn't already there

if not os.path.exists(today):
  os.mkdir(today) # make directory
  print ('Successfully created directory', today)

# 5. We use the tar command (in Unix/Linux) to put the files in a tar  archive

tar_command = "tar -zcvf '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(tar_command) == 0:
  print (source ,'is successful backup to', target)
else:
  print ('Backup FAILED')

 #' '.join(a) 将a里面的数据变为字符串并用空格隔开

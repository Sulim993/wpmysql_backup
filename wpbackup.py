#!/usr/local/bin/python
import optparse
import os
import datetime
import shutil
import socket
from subprocess import Popen, PIPE

 
date = datetime.datetime.now().strftime('%Y-%m-%d--%H:%M')  # register date and time

 
def backup_all_databases():  # backup all mysql databases
          # to avoid warning message using mysql password create a file in '/etc/mysql/mysql-backup-script.cnf' and put user and password info
    args = ['mysqldump', '--defaults-extra-file=/etc/mysql/mysql-backup-script.cnf', '--all-databases'] # command to access mysql databases and backup all databases to gzip
    with open("%s.sql.gz" % date, 'wb') as f:  # Opening a file using with
        p1 = Popen(args, stdout=PIPE) # executes the command specified by the string command
        p2 = Popen('gzip', stdin=p1.stdout, stdout=f)
        p1.stdout.close()
        p2.wait()
        p1.wait()
 
def main():  # create dump folder for the backups files named with date,time and hostname
    archive_path = "%s" % date 
    os.mkdir(archive_path, 0755)
    backup_all_databases()
    src_file = "%s.sql.gz" % date
    dst = "%s" % date 
    shutil.move(src_file, dst)
    tar_html_folder()


def tar_html_folder():  # backup wordpress folder to zip file
    output_filename_1 = "%s.html_dir"  % date
    output_filename_2 = "%s.html_dir.zip"  % date
    dir_name = '/var/www/html'
    dst = "%s" % date 
    shutil.make_archive(output_filename_1, 'zip', dir_name)
    shutil.move(output_filename_2, dst)
 

 
if __name__ == "__main__":
    main()

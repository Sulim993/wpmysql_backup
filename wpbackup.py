#!/usr/local/bin/python
import optparse
import os
import datetime
import shutil
import socket
from subprocess import Popen, PIPE

 
date = datetime.datetime.now().strftime('%Y%m%d-%h%m')  # register date and time

 
def backup_all_databases():  # backup all mysql databases
    args = ['mysqldump', '-u', 'root', '-p123', '--all-databases'] # command to access mysql databases and backup all databasesto gzip
    with open("%s.sql.gz" % date, 'wb') as f:
        p1 = Popen(args, stdout=PIPE)
        p2 = Popen('gzip', stdin=p1.stdout, stdout=f)
        p1.stdout.close()
        p2.wait()
        p1.wait()
 
def main():  # create dump folder for the backups files named with date,time and hostname
    archive_path = "%s" % date + socket.gethostname()
    os.mkdir(archive_path, 0755)
    backup_all_databases()
    src_file = "%s.sql.gz" % date
    dst = "%s" % date + socket.gethostname()
    shutil.move(src_file, dst)
    tar_html_folder()


def tar_html_folder():  # backup wordpress folder to zip file
    output_filename_1 = "%s.html_dir"  % date
    output_filename_2 = "%s.html_dir.zip"  % date
    dir_name = '/var/www/html'
    dst = "%s" % date + socket.gethostname()
    shutil.make_archive(output_filename_1, 'zip', dir_name)
    shutil.move(output_filename_2, dst)
 

 
if __name__ == "__main__":
    main()

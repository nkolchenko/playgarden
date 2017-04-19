#!/usr/bin/python

from __future__ import print_function
import zipfile
import os
from datetime import datetime, timedelta
#import logging
import traceback
import sys


## logger = logging.getLogger(__name__)
## logger.setLevel(logging.INFO)
## logger = logging


timestamp=datetime.today()
today = datetime.date(timestamp - timedelta(11))

date_for = datetime.strftime(today,'%Y_%m_%d')

zip_file_dir='/Users/nkolchenko/playgarden/python/zip_files/'
zip_file_name=zip_file_dir+'google_'+date_for+'.zip'

##logger.info("START")


def fmt_last_exception():
    exc_info = traceback.format_exception(*sys.exc_info())
    return ''.join(exc_info)


try:
    #raise ZeroDivisionError
     with zipfile.ZipFile(zip_file_name, 'r') as myzip:
         #print('is zip: '+str(zipfile.is_zipfile(zip_file_name)))
         arch_file=zipfile.ZipFile.namelist(myzip)
         #a={1,4,7,2,3}
         #i = a.__len__()
         i = arch_file.__len__()

         if i != 1:
             print('got '+str(i)+' files instead of 1 inside archive: '+str(zip_file_name))
         else:
             ##print('file name in archive :'+arch_file[0])
             ##print(zipfile.ZipFile.getinfo(myzip,arch_file[0]))
             zipfile.ZipFile.extractall(myzip,zip_file_dir)
             source=zip_file_dir+arch_file[0]
             dest=zip_file_dir+'google_'+date_for+'.csv'
             #print("src: "+source+"\ndst: "+dest)
             os.rename(source,dest)

except IOError:
    print("No such file or directory: "+str(zip_file_name))



except Exception as e:
    print('foo', fmt_last_exception())
    #print(type(e))
    #print(dir(e))


    # logger.exception('Ooops there is no: '+str(zip_file_name))
    # raise

###logger.info("DID")

# PEP 8

# (pip install ...) = six ; six.reraise (optional reading)

# traceback, sys

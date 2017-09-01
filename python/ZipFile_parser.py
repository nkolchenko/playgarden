#!/usr/bin/python

from __future__ import print_function
import zipfile
import os
import csv
from datetime import datetime, timedelta
#import logging
import traceback
import sys
import codecs


## logger = logging.getLogger(__name__)
## logger.setLevel(logging.INFO)
## logger = logging
##logger.info("START")


timestamp=datetime.today()
today = datetime.date(timestamp - timedelta(1))

date_for = datetime.strftime(today,'%Y_%m_%d')

zip_file_dir='/Users/nkolchenko/playgarden/python/zip_files/'
zip_file_name=zip_file_dir+'google_'+date_for+'.zip'
dest=zip_file_dir+'google_'+date_for+'.csv'

def fmt_last_exception():
    exc_info = traceback.format_exception(*sys.exc_info())
    return ''.join(exc_info)

def extract_data_from_zip():

    try:
        with zipfile.ZipFile(zip_file_name, 'r') as myzip:
             arch_file=zipfile.ZipFile.namelist(myzip)
             i = arch_file.__len__()

             if i != 1:
                 print('got '+str(i)+' files instead of 1 inside archive: '+str(zip_file_name))
             else:
                 ##print('mapping_file name in archive :'+file_list[0])
                 ##print(zipfile.ZipFile.getinfo(myzip,file_list[0]))
                 zipfile.ZipFile.extractall(myzip,zip_file_dir)
                 source=zip_file_dir+arch_file[0]
                 #dest=zip_file_dir+'google_'+date_for+'.csv'
                 os.rename(source,dest)

    except IOError:
        print("No such mapping_file or directory: "+str(zip_file_name))

    except Exception as e:
        print('foo', fmt_last_exception())
        #print(type(e))
        #print(dir(e))


def csv_parse():

    try:

        with codecs.open(dest, 'rb', 'utf-16') as csv_file:
            reader = csv.DictReader(csv_file, delimiter='\t', quotechar='"')
            for row in reader: #{'Advertiser cost': '5.238', 'Ad impressions (legacy)': '130,699', 'Days': '2017-04-05'}
                return (row['Days'],
                        'google',
                        float(row['Advertiser cost']),
                        int(row['Ad impressions (legacy)'].replace(',','')))


    except Exception as e:
        print('foo', fmt_last_exception())


if __name__ == '__main__':
    extract_data_from_zip()
    csv_parse()


# logger.exception('Ooops there is no: '+str(zip_file_name))
# raise
###logger.info("DID")
# PEP 8
# (pip install ...) = six ; six.reraise (optional reading)
# traceback, sys

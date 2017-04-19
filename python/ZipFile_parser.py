#!/usr/bin/python

from __future__ import print_function
import zipfile
from datetime import datetime, timedelta

timestamp=datetime.today()
today=datetime.date(timestamp-timedelta(1))

date_for = datetime.strftime(today,'%Y_%m_%d')

zip_file_dir='/Users/nkolchenko/playgarden/python/zip_files/'
zip_file_name=zip_file_dir+'google_'+date_for+'.zip'

print("START")

try:

    with zipfile.ZipFile(zip_file_name, 'r') as myzip:
        #print('is zip: '+str(zipfile.is_zipfile(zip_file_name)))
        arch_file=zipfile.ZipFile.namelist(myzip)
        #a={1,4,7,2,3}
        #i = a.__len__()
        i = arch_file.__len__()

        if(i <> 1):
            print('got '+str(i)+' files instead of 1 inside archive: '+str(zip_file_name))
        else:
            #print('file name in archive :'+arch_file[0])
            print(zipfile.ZipFile.getinfo(myzip,arch_file[0]))
            zipfile.ZipFile.extractall(myzip,zip_file_dir+date_for)
            #myzip.write('/Users/nkolchenko/playgarden/python/zip_files/google_2017_04_04.csv')

except:
   print('Ooops there is no: '+str(zip_file_name))

print("DID")




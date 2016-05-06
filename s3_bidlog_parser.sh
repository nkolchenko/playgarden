#!/bin/bash

#filestructer is describved in 
# https://github.com/strikead/rtb/blob/develop/doc/logging.md

date=2016_04_16
hours=00
i=0
#for i in {1..3}; do date "+%Y_%m_%d" -d "$i day ago"; done

for i in 0{0..9} {10..23}; do 
file="bids-"$date"_"$i"_00*"
#echo $file 
#aws s3 sync s3://strikead-data/logs/$DAY/ . --exclude '*' --include '*clicks*'
aws s3 sync s3://strikead-data/logs/"$date"/ . --exclude '*' --include $file && awk -F"\t" '{if ($79==75997) print $1","$17","$18}' $file > 75997.csv && rm $file
done



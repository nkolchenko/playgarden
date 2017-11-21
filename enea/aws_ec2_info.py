#!/usr/bin/python

""" 
done with the help of 
https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#instance

I assume that  aws_keys_file uses structure like:

parus:.aws_knp nkolchenko$ cat my_config.csv 
Access key ID,Session token
access_key_id_1,some_token_here
access_key_id_2,another_token_here
"""

from __future__ import print_function

import csv

import boto3

aws_keys_file = '/Users/nkolchenko/.aws_knp/my_config.csv'
output_file = '/Users/nkolchenko/.aws_knp/aws_result.csv'

with open(aws_keys_file, 'r') as creds:
    with open(output_file, 'wb') as out_file:
        reader = csv.DictReader(creds, delimiter=',', quotechar='"')
        for row in reader:
            ACCESS_KEY = row['Access key ID']
            # SECRET_KEY = row['Secret access key']
            SESSION_TOKEN = row['Session Token']

            client = boto3.client(
                'ec2',
                aws_access_key_id=ACCESS_KEY,
                # aws_secret_access_key=SECRET_KEY,
                aws_session_token=SESSION_TOKEN
            )
            response = client.describe_vpcs()
            vpc_id = response['Vpcs'][0]['VpcId']
            ec2 = boto3.resource('ec2')
            vpc = ec2.Vpc(vpc_id)

            # lets list all the vpc instances names, instance types, and availability zones

            for i in vpc.instances.all():
                # id = str(i)
                instance_name = i.private_dns_name  # technically it is possible to get i.tags Tag 'Name' here
                instance_type = i.instance_type
                instance_zone = i.placement['AvailabilityZone']

                # simpliest way:
                data = (instance_name + ',' + instance_type + ',' + instance_zone)
                out_file.write(data + '\n')

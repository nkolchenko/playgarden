#!/usr/bin/python

""" 
done with the help of 
https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#instance

v.1 is using credentials file
"""

from __future__ import print_function

import csv

import boto3

aws_keys_file = '/Users/nkolchenko/.aws_knp/my_config.csv'
output_file = '/Users/nkolchenko/.aws_knp/aws_result.csv'

# TODO: add argparse . So far I'm parsing particular cred file in order not to mess my 'prod' credentials

with open(aws_keys_file, 'r') as creds:
    reader = csv.DictReader(creds, delimiter=',', quotechar='"')
    for row in reader:
        ACCESS_KEY = row['Access key ID']
        SECRET_KEY = row['Secret access key']
        client = boto3.client(
            'ec2',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            # aws_session_token=SESSION_TOKEN,
        )
        response = client.describe_vpcs()
        vpc_id = response['Vpcs'][0]['VpcId']
        ec2 = boto3.resource('ec2')
        vpc = ec2.Vpc(vpc_id)

        # name, instance type, and availability zone

        with open(output_file, 'wb') as out_file:
            for i in vpc.instances.all():
                id = str(i)
                instance_name = i.private_dns_name  # technically it is possible to get i.tags Tag 'Name' here
                instance_type = i.instance_type
                instance_zone = i.placement['AvailabilityZone']

                # simpliest way:
                data = (instance_name + ',' + instance_type + ',' + instance_zone)
                out_file.write(data + '\n')

#!/usr/local/bin/python

import shlex, subprocess

task = "gcalcli --calendar test quick 'T1'"
#task = "gcalcli agenda"

args = shlex.split(str(task))

print args
send = subprocess.Popen(args) # I assume you already have Config file for this.
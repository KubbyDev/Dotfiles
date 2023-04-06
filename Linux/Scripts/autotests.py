#!/usr/bin/python3

import os
import sys

downloaded_location = "/media/kubby/Data/Tmp"
fPIC_flag_location = "CFLAGS = "

name = ''
options = []

for arg in sys.argv[1:]:
    if arg[0] == '-': options.append(arg)
    else: name = arg

if name == '':
    cwd = os.getcwd()
    name = cwd[cwd.rindex('/')+1:]
    print("No practical name given, using folder name (%s)" % name)

print("Extracting files...")
os.system('cd .. && tar -xvf %s/piscine-2023-c%s-*' % (downloaded_location, name))

if '-fPIC' in options:
    print("Adding -fPIC flag to Makefile")
    with open('Makefile', 'r') as f: content = f.read()
    fPICloc = content.index(fPIC_flag_location)+len(fPIC_flag_location)
    content = content[:fPICloc] + '-fPIC ' + content[fPICloc:]
    with open('Makefile', 'w') as f: f.write(content)

print("Testing...")
os.system('make all check')

print("Cleaning")
os.system("make clean")
if '-nr' not in options:
    os.system("rm tests -rf")
    os.system("rm Makefile")

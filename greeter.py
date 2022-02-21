#!/usr/bin/env python3
 
import argparse
 
 
parser = argparse.ArgumentParser()
parser.add_argument('name', type=str, help='Enter a name here')
args = parser.parse_args()
print('Hello, {}!'.format(args.name))

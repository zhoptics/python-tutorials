#!usr/bin/env python
# -*- coding:utf-8 -*-

import json

filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
    
print(numbers)

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:06:04 2021

@author: sun78
"""
# 列出当前目录的所有文件名
# 相关链接：https://stackabuse.com/python-list-files-in-a-directory/

import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
        
        
        
        
        
        
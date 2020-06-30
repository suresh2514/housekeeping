#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:32:56 2020

@author: surkumar
"""
import psutil

def cpu_percent() :
    return psutil.cpu_percent()

def memory_percent() :
    return psutil.virtual_memory().percent

def diskSpace_percent() :
    diskSpace = []
    for partition in psutil.disk_partitions():
        device = partition[1]
        diskSpace.append((device,psutil.disk_usage(device).percent))
 
    return diskSpace

    
#def diskFileUtilization() :
    
    
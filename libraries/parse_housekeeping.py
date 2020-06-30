# -*- coding: utf-8 -*-
import configparser 
config = configparser.ConfigParser() 
config.read(r"../config/housekeeping.ini") 
threshold_cpu=config['threshold']['threshold_cpu']
threshold_df = config['threshold']['threshold_df']
threshold_memory = config['threshold']['threshold_memory']
threshold_du = config['threshold']['threshold_du']
sender = config['mail']['sender']
receiver = config['mail']['receiver']

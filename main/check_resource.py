#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:18:47 2020

@author: surkumar
"""


from  libraries import parse_housekeeping as p
from libraries import mail
from  src import utilisation

_sender = p.sender
_receiver = p.receiver
_subject = "System resource usage alert: hostname:"
_password='password'
_body=""
for diskspace in utilisation.diskSpace_percent():
    if diskspace[1] > int(p.threshold_du):
        _body += f"Disk usage for {diskspace[0]} is greater than threhsold limit.\n"
        _body += f"Current usage is {diskspace[1]}%\n"

cpu = utilisation.cpu_percent()
if cpu > int(p.threshold_cpu):
        _body += "CPU utilization is greater than threhsold limit.\n"
        _body += f"Current usage is {cpu}%\n"

memory = utilisation.memory_percent()
if memory > int(p.threshold_memory):
        _body += "memory utilization is greater than threhsold limit\n"
        _body += f"Current usage is {memory}%\n"

mail.gmail_sent(sender=_sender, receiver=_receiver, password=_password, subject=_subject, body=_body)

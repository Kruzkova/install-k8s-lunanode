#! /usr/bin/env python
from lndynamic import LNDynamic

with open(r"/home/hme/.lunanode/commands.txt") as hpass:
    lines = hpass.readlines()

api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))
results = api.request('vm', 'list')
print(results)
results = api.request('vm', 'info', {'vm_id': 'e3e7ab5c-a944-4118-bf78-8a67b4722c48'})
print ("-----------------------")
print (results)

results = api.request('image', 'list')
print(results)


#1c018f61-e116-46d2-8a64-18f6963e3be7
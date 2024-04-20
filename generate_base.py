"""
Created on Sat Apr 20 18:27:52 2024

@author: xunya
"""

import pickledb

db = pickledb.load('data/File-Peers.db', False)

peer1 = ['one', 'two', 'three']
peer2 = ['three', 'four']
peer3 = ['one', 'two', 'three', 'four']

db.set('A', peer1)
db.set('B', peer2)
db.set('C', peer3)

db.dump()
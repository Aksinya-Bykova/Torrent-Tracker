"""
Created on Sat Apr 20 21:42:46 2024

@author: xunya
"""

import time
import pickledb
from edit_base import get_peers
from edit_base import exclude_peer

db = pickledb.load('data/File-Peers.db', False)

db_list = ['A', 'B', 'C']

def ping(file_name, peer):
    check_exist = True #TODO request to peer
    if check_exist == False:
        exclude_peer(x, y)

while True:
   time.sleep(10)
   for x in db_list:
       peers = get_peers(x)
       for y in peers:
           ping(x, y)

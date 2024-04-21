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
current_file_name = ""

flag_send_request = False
flag_send_filename = False

def check_exist_file():
    if not flag_send_request:
        flag_send_request = True
        flag_send_filename = False
        return "EXIST_FILE"
    elif not flag_send_filename:
        flag_send_request = False
        flag_send_filename = True
        return current_file_name
    
    flag_send_request = False
    flag_send_filename = False
    return "Ping"

def ping(file_name, peer):
    current_file_name = file_name
    check_exist_file()
    check_exist = True #TODO response from peer
    if check_exist == False:
        exclude_peer(x, y)

while True:
   time.sleep(10)
   for x in db_list:
       peers = get_peers(x)
       for y in peers:
           ping(x, y)

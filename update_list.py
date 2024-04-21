"""
Created on Sat Apr 20 23:06:39 2024

@author: xunya
"""
import pickledb
from edit_base import get_peers
from edit_base import set_file

flag_first_arg = False
flag_set_file = False
update_file = ""
update_peer = ""

def parse_set_file(request, peername):
    global flag_first_arg
    global update_file
    update_peer = peername
    
    if not flag_first_arg:
        update_file = request
        flag_first_arg = True
    else:
        flag_first_arg = False

while True:    
    if flag_set_file:
        set_file(update_file, update_peer)
        flag_set_file = False

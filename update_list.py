"""
Created on Sat Apr 20 23:06:39 2024

@author: xunya
"""
import pickledb
from edit_base import get_peers
from edit_base import set_file

flag_update_files = False #TODO from peer request 
update_file = ""
update_peer = ""

while True:
    if flag_update_files:
        set_file(update_file, update_peer)
        flag_update_files = False
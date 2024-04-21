"""
Created on Sat Apr 20 23:06:39 2024

@author: xunya
"""
import pickledb
from edit_base import get_peers
from edit_base import set_file

flag_update_files = False
flag_first_arg = False
update_file = ""
update_peer = ""

def parse_request(request):
    if (request == "SET_FILE"):
        flag_update_files = True
    elif flag_update_files:
        if not flag_first_arg:
            update_file = request
            flag_first_arg = True
        else:
            update_peer = request
            flag_first_arg = False

        flag_update_files = False

while True:
    if flag_update_files:
        set_file(update_file, update_peer)
        flag_update_files = False
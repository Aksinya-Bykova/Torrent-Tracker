"""
Created on Sun Apr 21 13:30:49 2024

@author: xunya
"""

from monitoring import current_file_name

flag_send_request = False
flag_send_filename = False

def get_response(): #TODO
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
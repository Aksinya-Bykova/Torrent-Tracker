"""
Created on Sun Apr 21 13:30:49 2024

@author: xunya
"""

from monitoring import check_exist_file
from update_list import parse_set_file
from update_list import flag_set_file

def parse_request(request):
    global flag_set_file
    if flag_set_file:
        parse_set_file(request)
        flag_set_file = False
    
    if (request == "SET_FILE"):
        flag_set_file = True


def get_response(): #TODO
    return "Ping"
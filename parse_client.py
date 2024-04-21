"""
Created on Sun Apr 21 13:30:49 2024

@author: xunya
"""

from monitoring import check_exist_file
from monitoring import flag_need_exist_file
from monitoring import check_exist
from update_list import parse_set_file
from update_list import flag_set_file
from edit_base import get_peers

flag_answer_exist = False
flag_get_peers = False
flag_ready_send_list = False

file_name = ""
peers_list_answer = []
i = -1

def parse_request(request):
    global flag_set_file
    global flag_answer_exist
    global flag_get_peers
    
    global file_name
    global peers_list_answer
    
    if flag_set_file:
        parse_set_file(request)
        flag_set_file = False
        
    if flag_answer_exist:
        if (request == "TRUE"):
            check_exist = True
            flag_answer_exist = False
        if (request == "FALSE"):
            check_exist = False
            flag_answer_exist = False
    
    if (flag_get_peers):
        file_name = request
        peers_list_answer = get_peers(file_name)
        flag_ready_send_list = True
        flag_get_peers = False
        
    if (request == "SET_FILE"):
        flag_set_file = True
    
    if (request == "EXIST_FILE"):
        flag_answer_exist = True
        
    if (request == "GET_PEERS"):
        flag_get_peers = True

def get_response():
    global flag_need_exist_file
    global flag_ready_send_list
    global i
    
    if flag_need_exist_file:
        return check_exist_file()
    
    if flag_ready_send_list:
        if (i < len(peers_list_answer - 1)):
            i += 1
            return peers_list_answer[i]
        else:
            flag_ready_send_list = False
    
    return "ping"

"""
Created on Sun Apr 21 13:30:49 2024

@author: xunya
"""

from monitoring import check_exist_file
from monitoring import flag_need_exist_file
from monitoring import check_exist
from update_list import parse_set_file
from update_list import flag_set_file

flag_answer_exist = False

def parse_request(request):
    global flag_set_file
    global flag_answer_exist
    
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
    
    if (request == "SET_FILE"):
        flag_set_file = True
    
    if (request == "EXIST_FILE"):
        flag_answer_exist = True

def get_response():
    global flag_need_exist_file
    
    if flag_need_exist_file:
        return check_exist_file()
    
    return "ping"

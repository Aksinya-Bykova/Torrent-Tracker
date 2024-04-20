"""
Created on Sat Apr 20 18:54:35 2024

@author: xunya
"""

import pickledb

db = pickledb.load('data/File-Peers.db', False)

#def exclude_peer(file_name):
    
def exclude_filename(file_name, peer):
    peers = list(db.get(file_name))
    peers.remove(peer)
    db.set(file_name, peers)
    db.dump()
    
def set_file(file_name, peer):
    peers = list(db.get(file_name))
    peers.append(peer)
    db.set(file_name, peers)
    db.dump()
    
def get_peers(file_name):
    return db.get(file_name)

#set_file("A", "two-three-nine")
#print(get_peers("A"))
#exclude_filename("A", "two-three-nine")
#print(get_peers("A"))
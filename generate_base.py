"""
Created on Sat Apr 20 18:27:52 2024

@author: xunya
"""

import pickledb

db = pickledb.load('data/File-Peers.db', False)

db.set('file.pdf', ['127.0.0.1:8001'])

db.dump()

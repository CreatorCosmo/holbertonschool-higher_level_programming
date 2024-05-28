#!/usr/bin/python3
#!/usr/bin/python3
"""
This module adds items (objects) from
command line arguments to a JSON file
'add_item.json'. If the file 
does not exist, it creates it.
If it does exist, it appends 
new items to it.
"""



import sys
import os.path

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

list_readed = []
list_1 = sys.argv[1:]
if os.path.exists("add_item.json"):
    list_readed = load_from_json_file("add_item.json")
save_to_json_file(list_readed + list_1, "add_item.json")

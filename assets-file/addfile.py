import os
import json
import shutil

folder_path = '/home/ec2-user/assets/Resource-Icons_10182023/'
pastefolder = '/home/ec2-user/assets-file/assets/'
# contents = os.listdir(folder_path)

# shutil.copy(folder_path, pastefolder)

def list_files_recursive(folder_path):
    items=[]
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            source = root +'/'+ file
            files={'item': file}
            items.append(files)
            print(source)
            shutil.copy(source, pastefolder)
    # return items

list_files_recursive(folder_path)
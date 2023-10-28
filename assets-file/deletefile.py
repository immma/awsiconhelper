import os

folderpath = '/home/ec2-user/assets-file/assets/'

for file in os.listdir(folderpath):
    if file.endswith('.svg'):
        print(file)
        os.remove(folderpath + file)
import os
import json

items = []
for file in os.listdir('/home/ec2-user/assets-file/assets/'):
    item = {'item': file}
    items.append(item)

print(json.dumps(items, indent=4))
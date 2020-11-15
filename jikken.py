import json
import pprint
 
dict = {"name": "tarou", "age": 23, "gender": "man"}
 
json_file = open('sample.json', 'w')
json.dump(dict, json_file)
json_file = open('sample.json', 'r')
data = json.load(json_file)
pprint.pprint(data)
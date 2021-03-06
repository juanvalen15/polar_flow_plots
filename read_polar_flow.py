# Python program to read polar flow .json training files

import json

# opening json file
f = open('test.json');

# returns json object as a dictionary
data = json.load(f)

# iterating through the json list
irange = range(10);
for i in irange:
	print(data["exercises"][0]["samples"]["speed"][i])

# closing file
f.close()
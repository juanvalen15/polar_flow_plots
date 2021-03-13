# Python program to read polar flow .json training files

import json
import numpy as np

# opening json file
f = open('test.json')

# returns json object as a dictionary
data = json.load(f)
speed = np.array(20)


# iterating through the json list
irange = range(3)
for i in irange:
	if (data["exercises"][0]["samples"]["speed"][i]["value"]) is not None:
		print('value does not exist at i=',i)
	else:
		print(data["exercises"][0]["samples"]["speed"][i])



# closing file
f.close()
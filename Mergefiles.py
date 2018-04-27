import json

filename = 'ResultwithNameGender'
f = open('ResultwithNameGender1.json')
data = json.load(f)
f.close()
f = open('ResultwithNameGender2.json')
tempdata = json.load(f)
for temp in tempdata:
    data.append(temp)
f.close()
f = open('ResultwithNameGender3.json')
tempdata = json.load(f)
for temp in tempdata:
    data.append(temp)
f.close()
f = open('ResultwithNameGender4.json')
tempdata = json.load(f)
for temp in tempdata:
    data.append(temp)
f.close()
f = open('ResultwithNameGender5.json')
tempdata = json.load(f)
for temp in tempdata:
    data.append(temp)
f.close()

with open(filename + '.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

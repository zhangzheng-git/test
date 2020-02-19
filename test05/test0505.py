import  json

list={'name':'zhang','age':12}

print(list)

print(json.dumps(list))

with open("data.json","w") as f:
    json.dump(list,f)
with open("data.json","r") as f:
    json_str = json.load(f)
print(json_str)
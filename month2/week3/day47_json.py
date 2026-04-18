import json
from pathlib import Path

# # Python to json string
# print(f"=== Python to json ===")

data = {
    'name':'kartik',
    'age': 20,
    'skills':['Python','Linux', 'Bash'],
    'scores':{
        'python': 85,
        'linux': 70,
        'bash': 65
    },
    'active':True,
    'gpa':6.2,
    'nickname': None   # None ~ null in json
}
json_string= json.dumps(data,indent=4)
print(json_string)
print(f"\nType: {type(json_string)}")

# # without indent == not human readable
# compact = json.dumps(data)
# print(f"\nCompact: {compact}")

# Json to Python
print(f"=== Json to Python ===")

# json.loads -- Json string to dictionary
parsed = json.loads(json_string)
print(f"Type: {type(parsed)}")
print(f"Name: {parsed['name']}")
print(f"First skill : {parsed['skills'][0]}")
print(f"Python score : {parsed['scores']['python']}")
# these name, scores, python, scores are case-sensitive

# #  Writing Json to file
# print("=== Writing Json to File ===")
output_path = Path('/home/kartik007/Desktop/python-new/python-journey/month2/week3/data.json')

# # Method 1- using json.dumps + write_text
# output_path.write_text(json.dumps(data , indent=4))
# print(f"Written to : {output_path}")

# # Method 2- using json.dump with open()
# with open(output_path , 'w') as f:
#     json.dump(data ,f, indent=4)
# print(f"Written again with json.dump")


# # Reading json file with python
# print(f"\n === Reading Json from Python === ")

# # Method 1- using read_text + json_loads
# content = output_path.read_text()
# loaded = json.loads(content)
# print(f"Loaded name: {loaded['name']}")

# # Method 2- using json.load with open()
# with open(output_path, 'r') as f: 
#     loaded2 = json.load(f)
# print(f"Loaded skills : {loaded2['skills']}")

# Navigation of Nested Json 
print(f"\n === Navigating NESTED JSON === ")

# this is like a structure of API responses
api_response = {
    'status':'success',
    'data': {
        'user':{
            'id':12345,
            'username': 'kartik007',
            'profile': {
                'bio': 'BTech CS Student',
                'location' : 'Uttarakhand'
            }
        },
        'repos':[
            {'name':'python-journey', 'stats':0,'languages':'Python'},
            {'name': 'project2', 'stars':2, 'language': 'Shell'}
        ]
    }
}
#  Accessing nested values
username = api_response['data']['user']['username']
location = api_response['data']['user']['profile']['location']
first_repo = api_response['data']['repos'][0]['name']
all_repo_name = [repo['name'] for repo in api_response['data']['repos']]

print(f"Username : {username}")
print(f"Location : {location}")
print(f"First repo : {first_repo}")
print(f"All repos : {all_repo_name}")

#  Safe access with .get() ---- use when a key might not exist
bio = api_response['data']['user']['profile'].get('bio', 'No bio') 
twitter = api_response['data']['user']['profile'].get('twitter', 'NOt set')
print(f"Bio : {bio}")
print(f"Twitter : {twitter}")
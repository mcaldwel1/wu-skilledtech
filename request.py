import requests 
import json
import re

courseArray = []

response = requests.get(url="https://www.wu-skilledtech.com/admin/api/v2/courses", 
    headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
            "Lw-Client": "647a25ef09b3e9a6f00aa290",
            "Accept": "application/json"})
prsd = response.json()

for a in (prsd['data']):
    courseArray.append(a['id'])

course_Length = len(courseArray)
c = 0

def get_new_url(index, length, arr): 
    if(index < length):
        return arr[index]
    else: 
        return arr[0]

preArray = []
titleArray = []

while c < course_Length:

    fetchUrl = "https://www.wu-skilledtech.com/admin/api/v2/courses/" + get_new_url(c, course_Length, courseArray) + "/contents"

    response = requests.get(url=fetchUrl, 
        headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
                "Lw-Client": "647a25ef09b3e9a6f00aa290",
                "Accept": "application/json"})

    parsed = response.json()

    if('error' in parsed):
        courseArray.pop(c)
        course_Length -=1
        continue

    for a in parsed['sections']:
        for b in a:
            if(a[b] and 'Pre-Course' in a[b]):
                preArray.append(a['learningUnits'][0]['id'])
                titleArray.append(parsed['id'])
            if(a[b] and 'precourse' in a[b]):
                preArray.append(a['learningUnits'][0]['id'])
                titleArray.append(parsed['id'])
            if(a[b] and 'Post-Course' in a[b]):
                preArray.pop()
            if(a[b] and b == 'learningUnits'):
                for unit in a[b]:
                    if(unit and 'Pre-Course' in unit):
                        preArray.append(unit['id'])
                        titleArray.append(parsed['id'])
                    if(unit and 'precourse' in unit):
                        preArray.append(unit['id'])
                        titleArray.append(parsed['id'])
    c+=1

"""print(*courseArray, sep="\n")"""

print(courseArray)
print(course_Length)

print('\n', preArray)

#find a duplicate pre-course id's and remove them from pre-array

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

"""print("\n", "duplicates: ", find_duplicates(preArray))"""

def remove_duplicates(arr, main):
    for a in arr:
        for b in main:
            if(b == a): main.pop(main.index(b))
    return main

preArray = remove_duplicates(find_duplicates(preArray), preArray)
titleArray = remove_duplicates(find_duplicates(titleArray), titleArray)

id_length = len(preArray)

print("\n", titleArray)

#some pre-course assessments aren't populated, haven't been set up, or have no user responses 
#these assessment id's will be removed from pre-array 

false_id_list = []
false_list = []
d=0

#make calls to all pre-course assessment id's in pre-array

def make_call(i, length, array):
    fetchUrl_2 = "https://www.wu-skilledtech.com/admin/api/v2/assessments/" + get_new_url(i, length, array) + "/responses"

    response = requests.get(url=fetchUrl_2, 
        headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
                "Lw-Client": "647a25ef09b3e9a6f00aa290",
                "Accept": "application/json"})

    parsed = response.json()

    if(not response):
        false_list.append(i)
        """false_list.append(get_new_url(i, length, array))"""

    return parsed


while d < id_length:
    parsed = make_call(d, id_length, preArray)
    d+=1

print("\n", "list of no response surveys: ", false_list)

index = (len(false_list) - 1)
for a in false_list:
    preArray.pop(false_list[index])
    index-= 1

"""print("\n", preArray)"""


global participant_arr      #global in case need to use variable in jupyter notebook
participant_arr = []

#class to define properties of each user who completed the pre-course array
 
class participant:
    def __init__(self, name, age, gender, race, education, employment_status, served):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        self.education = education
        self.employment_status = employment_status
        self.served = served
    
    def format_json(self):
        return json.dumps(self.__dict__, indent=4)

#object make for each user 
#all properties are strings except for 'age' 
def make_p():
    p = participant("a", 0, "a", "a", "a", "a", "a")
    return p

for a in preArray:
    ay = preArray
    result = make_call(ay.index(a), len(ay), ay)
    for b in result['data']:
        pa = make_p()
        flag = 0
        for c in b['answers']:
            if(re.match(r'.*[Nn]ame$|.*[Ff]irst and [Ll]ast', (c['description']))):
                pa.name = c['answer']
                flag+=1
            if(re.match(r'[Aa]ge', (c['description']))):
                pa.age = c['answer']
                flag+=1
            if(re.match(r'[Gg]ender', (c['description']))):
                pa.gender = c['answer']
                flag+=1
            if(re.match(r'.*[Rr]ace', (c['description']))):
                if(c['answer']):
                    pa.race = c['answer']
                else:
                    pa.race = 'not specified'
                flag+=1
            if(re.match(r'.*[Ss]chool|[Ee]ducation', (c['description']))):
                pa.education = c['answer']
                flag+=1
            if(re.match(r'.*[Cc]urrently [Ee]mployed', (c['description']))): 
                pa.employment_status = c['answer']
                flag+=1
            if(re.match(r'.*[Aa]ctive [Dd]uty', (c['description']))): 
                pa.served = c['answer']
                flag+=1
        if(flag >= 2): participant_arr.append(pa)

print(len(participant_arr))

json_arr = []

for a in participant_arr:
    a = a.format_json()
    json_arr.append(a)
    

data_file = open('data.json', 'w')
data_file.write('{')
data_file.write('\n')
data_file.write('"data" : [')
data_file.write('\n')
z = 0
for x in json_arr:
    if(z < (len(participant_arr) - 1)):
        data_file.write(x)
        data_file.write(",")
    elif(z == (len(participant_arr) - 1)): 
        data_file.write(x)
    z+=1
data_file.write('\n')
data_file.write(']')
data_file.write('\n')
data_file.write('}')
data_file.close()










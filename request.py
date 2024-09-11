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

    def get_id(data1, sect):
        for sect in data1:
            if(data1[sect] == None):
                data1[sect] == 0.1
            else:
                if("Pre-Course" in data1[sect]): return True

    keyArray = []
    sectionArray = []

    if(parsed['sections'][0]['learningUnits']):
        for item in list(parsed['sections'][0]['learningUnits'][0].keys()):
            keyArray.append(item)

    if(parsed['sections'][0]):
        for item in list(parsed['sections'][0].keys()):
            sectionArray.append(item)

    for a in parsed['sections']:
        for b in a:
            if(a[b] and 'Pre-Course' in a[b]):
                preArray.append(a['learningUnits'][0]['id'])
            if(a[b] and b == 'learningUnits'):
                i=0
                for unit in a[b]:
                    for item in keyArray:
                        if(a[b][i][item] and 'Pre-Course' in a[b][i][item]):
                            preArray.append(a[b][i]['id'])
                    i+=1
    c+=1

print(*courseArray, sep="\n")

print('\n', preArray)

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

print("\n", "duplicates: ", find_duplicates(preArray))

def remove_duplicates(arr, main):
    for a in arr:
        for b in main:
            if(b == a): main.pop(main.index(b))
    return main

print("\n", preArray)
preArray = remove_duplicates(find_duplicates(preArray), preArray)
print("\n", preArray)

id_length = len(preArray)

false_list = []
d=0

def make_call(index, i, length, array):
    fetchUrl_2 = "https://www.wu-skilledtech.com/admin/api/v2/assessments/" + get_new_url(i, length, array) + "/responses"

    response = requests.get(url=fetchUrl_2, 
        headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
                "Lw-Client": "647a25ef09b3e9a6f00aa290",
                "Accept": "application/json"})

    parsed = response.json()

    if(not response):
        false_list.append(index)

    return parsed


while d < id_length:
    parsed = make_call(d, d, id_length, preArray)
    d+=1

print("\n", "list of no response surveys: ", false_list)

index = (len(false_list) - 1)
for a in false_list:
    preArray.pop(false_list[index])
    index-= 1

print("\n", preArray)

participant_arr = []

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

def make_p():
    p = participant("a", 0, "a", "a", "a", "a", "a")
    return p

for a in preArray:
    ay = preArray
    result = make_call(ay.index(a), ay.index(a), len(ay), ay)
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
                pa.race = c['answer']
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

        if(flag == 7): participant_arr.append(pa)

print(len(participant_arr))

json_arr = []

for a in participant_arr:
    a = a.format_json()
    json_arr.append(a)

data_file = open("data.json", 'w')
for x in json_arr:
    data_file.write(x)
data_file.close()







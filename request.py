import requests 
import json
import re

courseArray = [
    "powerofai", 
    "doverdata", 
    "appliediotmay2024", 
    "iotfundamentalsshell", 
    "iotfundamentalsmay2024", 
    "mpm365sb", 
    "ai4-product-managers", 
    "iotfapril2024", 
    "cfda1", 
    "appliediotsolutions", 
    "iotsolutions", 
    "iotfundamentals", 
    "gradallmsexcel2", 
    "advanced-cybersecurity-and-future-trends", 
    "cybersecurity-fundamentals", 
    "computer-programming-fundamentals", 
    "jsmo", 
    "mactdpwcpb", 
    "mactdpwcp", 
    "mac365", 
    "excelbasic", 
    "upltd", 
    "timken-steel-data-analytics-ii", 
    "ican", 
    "test4", 
    "gwmsoffice", 
    "psgoodwill", 
    "psmt", 
    "tsda", 
    "msoffice", 
    "stw-job-skills-c"
]

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
            if(a[b] and "Pre-Course" in a[b]):
                """print(a['id'])
                print(a['learningUnits'][0]['id'])"""
                preArray.append(a['learningUnits'][0]['id'])
            if(a[b] and b == 'learningUnits'):
                i=0
                for unit in a[b]:
                    for item in keyArray:
                        if(a[b][i][item] and "Pre-Course" in a[b][i][item]):
                            """print(a[b][i]['id'])
                            print(a[b][i]['title'])"""
                            preArray.append(a[b][i]['id'])
                    i+=1
    c+=1

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

def remove_duplicates(arr, main):
    for a in arr:
        for b in main:
            if(b == a): main.pop(main.index(b))
    return main

preArray = remove_duplicates(find_duplicates(preArray), preArray)
print(preArray)

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
    
    """if(response):
        for a in parsed['data']:
            if("Name" in (a['answers'][0]['description'])):
                print(a['answers'][0]['answer'])"""

    d+=1

print(false_list)

index = (len(false_list) - 1)
for a in false_list:
    preArray.pop(false_list[index])
    index-= 1

print("\n", preArray)

e=0
for a in preArray:
    ay = preArray
    result = make_call(ay.index(a), ay.index(a), len(ay), ay)
    for b in result['data']:
        for c in b['answers']:
            if(re.match(r'.*[Nn]ame$|.*[Ff]irst and [Ll]ast', (c['description']))):
                print(c['answer'])
            """if(re.match(r'[Aa]ge', (c['description']))):
                print(c['answer'])
            if(re.match(r'[Gg]ender', (c['description']))):
                print(c['answer'])"""
            if(re.match(r'.*[Rr]ace', (c['description']))):
                print(c['answer'])
            """if(re.match(r'.*[Ss]chool|[Ee]ducation', (c['description']))):
                print(c['answer'])
            if(re.match(r'.*[Cc]urrently [Ee]mployed', (c['description']))): 
                print(c['answer'])
            if(re.match(r'.*[Aa]ctive [Dd]uty', (c['description']))): 
                print(c['answer'])"""
        












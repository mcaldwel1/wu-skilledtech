import requests 
import json

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
c = 16

preArray = []

def get_new_url(): 
    if(c < course_Length):
        return courseArray[c] + "/contents"
    else: 
        return courseArray[0] + "/contents"

fetchUrl = "https://www.wu-skilledtech.com/admin/api/v2/courses/" + get_new_url()

response = requests.get(url=fetchUrl, 
    headers={"Authorization": "Bearer AunFTUso15kMMpqHTyfm8CdZ6HRRjvrhkwtoUCWz", 
            "Lw-Client": "647a25ef09b3e9a6f00aa290",
            "Accept": "application/json"})

"""parsed = json.loads(response.text)"""
parsed = response.json()

def get_id(data1, sect):
    for sect in data1:
        if(data1[sect] == None):
            data1[sect] == 0.1
        else:
            if("Pre-Course" in data1[sect]): return True

"""for y in parsed['sections'][0]['learningUnits']:
    i=0
    result = filter(get_id(parsed['sections'][i]['learningUnits']), parsed['sections'][i]['learningUnits'])
    filtered = list(result)
    i+=1"""

keyArray = []
sectionArray = []

if(parsed['sections'][0]['learningUnits']):
    for item in list(parsed['sections'][0]['learningUnits'][0].keys()):
        keyArray.append(item)

print(keyArray)

if(parsed['sections'][0]):
    for item in list(parsed['sections'][0].keys()):
        sectionArray.append(item)

valArray =[]

for y in parsed['sections'][0]['learningUnits']:
    i=0
    for item in keyArray:
        if(parsed['sections'][0]['learningUnits'][i]):
            valArray.append(parsed['sections'][0]['learningUnits'][i][item])
    i+=1

for a in parsed['sections']:
    """if(a == parsed['sections'][0]): print(a['id'])"""
    for b in a:
        if(a[b] and "Pre-Course" in a[b]):
                print(a['id'])
                print(a['learningUnits'][0]['id'])
        if(a[b] and b == 'learningUnits'):
             i=0
             for unit in a[b]:
                for item in keyArray:
                    if(a[b][i][item] and "Pre-Course" in a[b][i][item]):
                        print(a.items())
                        print(a[b][i]['id'])
                        print(a[b][i]['title'])
                i+=1

"""for a in parsed['sections']:
    for b in a:
        if(a[b] and "Pre-Course" in a[b]):
            print(a[b].keys())"""

print(len(parsed['sections']))
print(len(keyArray))
print(c)

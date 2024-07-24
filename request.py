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
c = 5

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

def get_id(data):
    if("Pre-Course" in data): return data

"""result = filter(get_id(parsed['sections'][0]['learningUnits']), parsed)
filtered = list(result)"""

keyArray = []

for item in list(parsed['sections'][0]['learningUnits'][0].keys()):
    keyArray.append(item)

for item in keyArray:
    i=0
    for y in parsed['sections'][0]['learningUnits']:
        if(get_id(parsed['sections'][0]['learningUnits'][i][item])):
            preArray.append((parsed['sections'][0]['learningUnits'][i]['id']))
        i+=1

print(preArray)
print(keyArray)
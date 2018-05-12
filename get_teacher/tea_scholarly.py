import scholarly
import json
with open('new_teacher.json', 'r', encoding = 'utf-8') as f:
    data = f.read()
    json_data = json.loads(data)
query = []
for k in json_data:
    query +=json_data['title']

for t in query: # teacher
    i = 0
    search_query = scholarly.search_pubs_query(t)
    with open('dataset/{}.json'.format(t), 'w', encoding = 'utf-8') as f:
        data = [] 
        for a in search_query: # articles
            i += 1
            if i > 100:
                break
            else:
                data.append(a.__dict__)
        json.dump(data, f)

"""
with open('zh_zhan.txt', 'w') as f:
    for a in search_query:
        i+=1
        if i > 100:
            break
        else:
            f.write(a.__str__())
            f.write(',\n')

with open('zh_zhan.json', 'w', encoding = 'utf-8') as f:
    data = []
    for a in search_query:
        i+=1
        if i > 100:
            break
        else:
            data.append(a.__dict__)
    json.dump(data, f)
"""

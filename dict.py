
dic = {}
dic0 = {"id": 1, "name": "aaa", "like": 0}
dic1 = {"id": 2, "name": "bbb", "like": 0}
dic[dic0['name']] = dic0
dic[dic1['name']] = dic1
print(dic)

dic['bbb']['like'] = 1

print(dic['bbb'])

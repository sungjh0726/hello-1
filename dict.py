
dic = {}

# html 파싱 데이터
dic0 = {"id": 1, "name": "aaa", "like": 0}
dic1 = {"id": 2, "name": "bbb", "like": 0}

dic[dic0['name']] = dic0
dic[dic1['name']] = dic1

print(dic)

# 찾기
bbbJson = dic['bbb']

# 수정 및 추가하기
bbbJson['like'] = 1
bbbJson.update({'others': 'pppppppp'})

print(dic['bbb'])
print(dic)

dic = {}

# html 파싱 데이터
dic0 = {"songno": 1, "name": "aaa", "like": 0}
dic1 = {"songno": 2, "name": "bbb", "like": 0}

# dic에 dic0과 dic1을 키값 songno로 추가하기
dic[dic0['songno']] = dic0
dic[dic1['songho']] = dic1

print(dic)
print("-------------------------------------")


# 찾기
bbbJson = dic['bbb']

# 수정 및 추가하기
bbbJson['like'] = 1
bbbJson.update({'others': 'pppppppp'})

print(dic['bbb'])
print(dic)

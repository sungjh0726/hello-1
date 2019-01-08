print("---------- This is test.py --------------")

def set_dic_param(*argv, **kargv):
	print("set params=", len(argv), '<--', argv)
	print("dic params=", kargv.keys(), '<--', kargv)

set_dic_param(1, 2, 3, name='hong', age=23)

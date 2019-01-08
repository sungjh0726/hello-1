import math

s = "q2"
try:
    a = '2' + 1
    i = int(s)

except TypeError as e:
    print("TypeError>>", type(e), "==>", e)
except ValueError as e:
    print("ValueError>>", type(e), "==>", e)

except Exception as e:
    print("EEEEE>>", type(e), "==>", e)

else:
    print(math.sqrt(i))

finally:
    print("Thans a lot.")
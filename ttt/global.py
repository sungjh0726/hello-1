g_x  = 10000

def change_x():
    global g_x
    print("Inner change_x>>", g_x)
    g_x = 300
    print("Inner change_x>>", g_x)

print("111>>", g_x)

change_x()

print("222>>", g_x)

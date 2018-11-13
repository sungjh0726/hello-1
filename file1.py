def write_file():
    with open("a.csv", "a") as file:
        file.write("이름,성별,나이\n")
        file.write("김일수,남,14\n")
        file.write("김이수,남,24")

def read_file():
    with open("a.csv", "r") as file:
        for line in file:
            print("line>>", line)

# write_file()
read_file()
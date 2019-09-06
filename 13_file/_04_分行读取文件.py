file = open("13_file/README")

text = file.readline()

while text: 
    print(text)
    text = file.readline()

file.close()

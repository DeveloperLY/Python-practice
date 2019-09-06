file_read = open("13_file/README")
file_write = open("13_file/README[复件]", "w")

while True:
    text = file_read.read()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()

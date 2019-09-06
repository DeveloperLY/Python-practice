file_read = open("13_file/README")
file_write = open("13_file/README[复件]", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()

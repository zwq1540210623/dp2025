


text = "This is my first test.\nThis is next line.\nThis is last line.\n"

print(text)

# w:写 r:读 a:追加
my_file = open('my_file.txt', 'w')
my_file.write(text)
my_file.close()

append_text = "This is appended file.\n"
my_file = open('my_file.txt', 'a')
my_file.write(append_text)
my_file.close()


file = open("my_file.txt", "r")
content = file.readline()
second_content = file.readline()
print(content)
print(second_content)

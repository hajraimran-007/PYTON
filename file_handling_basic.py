'''#concept of write(w)
file = open("data.txt", "w")
file.write("Hello, file handling!")
file.close()

print("Data written successfully!")

#concept of read:
file = open("data.txt", "r")

content = file.read()
print(content)

file.close()'''''

#append(add without del old data):
file = open("data.txt", "a")

file.write("\nThis is new line added later.")

file.close()

#count words in file
file = open("data.txt", "r")

text = file.read()
words = text.split()

print("Total words:", len(words))

file.close()

#count lines in file:
file = open("data.txt", "r")

lines = file.readlines()

print("Total lines:", len(lines))

file.close()

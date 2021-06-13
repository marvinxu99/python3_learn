from writablefile import WritableFile

with WritableFile("hello.txt") as file:
	file.write("Hello, World!")
print("done")
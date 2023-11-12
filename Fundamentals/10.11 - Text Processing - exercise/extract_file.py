# Write a program that reads the path to a file and subtracts the file name and its extension.

path = input().split("\\")
file_name = path[-1].split(".")
print(f"File name: {file_name[0]}\n"
      f"File extension: {file_name[1]}")

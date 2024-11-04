for i in range(1, 11):
  print(i, end=" * ")
print("\n")
str1 = input("Enter the string: ")
length = len(str1)
for i in range(length):
  print((" " * ((length - i) * 2)), end="")
  for j in range(i + 1):
    print(str1[i], end=" ")
  print("")
str2 = input("Enter the string: ")
complete = str2
length2 = len(str2)
for i in range(length2):
  print(str2[:i])
print(complete)

num = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
  print(" " * (num - i) + "* " * i)
for i in range(1, num + 1):
  print(" " * i + "* " * (num - i))

num2 = int(input("Enter the number of rows: "))
for i in range(1, num + 1):
  print("* " * i)
for i in range(1, num + 1):
  print("* " * (num - i))

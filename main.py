# Write a Python program to read the marks in five subjetcs (maximum mark 20 for each subject) and compute the percentage and grade 
# Grade A >=90%
# Grade B >=80%

x=int(input())
y=int(input())
z=int(input())
i=int(input())
j=int(input())
pre=((x+y+z+i+j))

print(pre,end="%")
print("")
if(pre>=90):
  print("A")
if(pre>=80):
  print("B")
if(pre>=70):
  print("C")
if(pre>=60):
  print("D")
if(pre>=50):
  print("E")
   
# opening file 1 and 2 in read mode
file=open("./afterclassproj.txt","r")
data=file.read()
file1=open("./afterclassproj2.txt","r")
data2=file1.read()

# data transfer to third file
file2=open("./afterclassproj3.txt","w")
file2.write(data)
file2.write("\n")
file2.write(data2)

print("The data has been successfully transfered to file 3")
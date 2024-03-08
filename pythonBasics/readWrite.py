File = open("test.txt")

#Read all the contents of file
# Read n number of characters by passing parameters
#print(File.read(7))
#read one single line at a time readline()
#print(File.readline())
#print(File.readline())



# Print line by line by readline method

line = File.readline()
#while line!="":
 #   print(line)
  #  line = File.readline()


for line in File.readlines():
    print(line)

File.close()






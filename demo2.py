List = [1, 2, 3, "Fail"]
print(List[0])
print(List[3])

print(List[0:4])
List.insert(3, "Test")
print(List)
List[3] = "Pass"
print(List)
del List[0]
print(List)

#Tuple

val = [1, 2, "Abi", 3,]


print(val[2])

val.insert(2, "ABHIshek")

print(val[0:3])



#Dictionary

Dic = {1:"Test", 2:"Run", "Pass": 100}
print(Dic[1])
print(Dic[2])
print(Dic["Pass"])




# How to create Dictionary on runtime

Dict={}

Dict["FirstName"] = "Abhishek"
Dict["LastName"] = "Himalyan"
Dict["Gender"] = "Male"

print(Dict)

print(Dict["LastName"])











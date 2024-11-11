#list
thislist=["apple", True, "apple", 10, 24.5]
#print(type(thislist))

#thislist.append(False)
#print(thislist)
#print(thislist[0])
#thislist.pop()
#thislist.clear()
#thislist.remove(24.50)
#count_list=thislist.count("apple")
#print(count_list)
#thislist.extend([12,"yes"])
#index_list=thislist.index(12)
#print(index_list)

#Tuple
my_tuple=("apple", 3.14, True, 12, "apple")
count_tuple=my_tuple.count("apple")
index_tuple=my_tuple.index(3.14)

#num1=(1,2,3)
#num2=(4,5,6,)
#num=num1+num2
#print(num)
#print(index_tuple) 
#my_tuple=('a','b')
#repeated_tuple=my_tuple*3
#print(my_tuple*3)

#Dictionary
my_dict={"apple":2, "AC": True,"orange":1, "name": "John"}
print(my_dict["AC"])

my_dict["food"]="rice"# Add a new entry
my_dict["orange"]=7 # Modify an entry
my_dict.pop("apple")
del my_dict["AC"]
print(my_dict)

student={"person1": "David",
         "person2":{"name": "John", "age":20,"course":{"python":"Begin","HTML":3}}
        }

print(student["person2"]["course"]["HTML"][8])
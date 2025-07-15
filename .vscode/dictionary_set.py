# myself = {
#     "name" : "annapurna",
#     "regd_no" : 2401206030,
#     "branch" : "cse",
#     "year" :2024,
#     "section" : "A"
# }

# print(myself)
# myself["name"] = "Annapurna Poria"
# myself["ending_year"] = 2028
# myself["starting_year"] = myself.pop("year")
# print(myself)
# print(myself["name"])

# null_dict = {}
# null_dict["name"] = "annapurna"
# print(null_dict["name"])

# dict = {
#     "name" : "annapurna poria",
#     "subjects" : {
#         "sub_1" : "python",
#         "sub_2" : "java",
#         "sub_3" : "c++"
#     }
# }
# print(dict["subjects"]["sub_1"])
# dict["subjects"]["sub_4"] = "javascript"
# print(dict["subjects"])

# print(dict.keys())
# print(tuple(dict.keys()))
# print(list(dict.keys()))
# print(len(list(dict.keys())))
# print(dict.values())
# print(tuple(dict.values()))
# print(list(dict.values()))
# print(dict.items())
# pairs = list(dict.items())
# print(pairs[0])
# # print(dict.get("name2"))
# # this will return none if the key does not exist
# # print(dict["name2"]) 
# # this will give an error as key does not exist
# new_dict = {"city" : "cuttack"}
# dict.update(new_dict)
# print(dict)


# set = {"a", "d", "c", "w", 1, 2, 2, 8, 8}
# print(set)
# print(type(set))
# print(len(set))
# empty_set = {}
# print(type(empty_set))    
# this is not a set , this is a dictionary (empty dictionary)
# collection = set()
# print(type(collection))
# collection.add("a")
# collection.add("2")
# collection.add("b")
# # collection.add(["c", 3, 4])
# # this is will give an error as set cannot contain list values; list is unhashable
# # only one argument is allowed in add method 
# # collection.remove("2")
# # this will remove a perticular element from the set.
# # collection.clear()
# # o/p will be empty set i.e. set().
# print(collection.pop())
# # this will remove arbitrary element from the set.
# print(collection)
# print(len(collection))

# set1 = {1, 2, 3, 4}
# set2 = {4, 1, 5, 7}
# print(set1.union(set2))
# print(set1.intersection(set2))

# q1.
# word_meanings = {
#     "table" : ["a piece of furniture ","list of facts and fiures" ] ,
#     "cat" : "a small animal"    
# }
# print(word_meanings)

# q2.
# classrooms = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(classrooms)
# print(len(classrooms))

# q3.
# mark_list = {}
# X = int(input("chemistry :"))
# mark_list.update({"chemistry" : X})

# Y = int(input("physics :"))
# mark_list.update({"physics" : Y})

# Z = int(input("maths :"))
# mark_list.update({"maths" : Z})
# print(mark_list)

# q4.
# num = {9, 9.0}
# print(num)
# o/p = {9}

# int = "9"
# float = "9.0"
# num = {int, float}
# print(num)

# values = {
#     ("int" , 9),
#     ("float" , 9.0)
# }
# print(values)
# tup= (1,2,3,8,55,"Subhash",True,789)
# # print(type(tup),tup)
# # print(len(tup))
# # print(tup[0])
# # print(tup[2])
# # print(tup[-2])
# # print(tup[34])

# # if 55 in tup :
# #     print("Yes 55 is present in this tuple")

# tup2 = tup[1:4]
# print(tup2)

# countries = ("Spain","Italy","India","France","England")
# temp = list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)

tuple1 = (0,1,2,3,4,2,3,9,3,5,6,3,8,3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(3,5,8)
res = len(tuple1)
print('Count of 3 in tuple1 is:',res)
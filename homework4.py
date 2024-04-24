immutable_var = (2, 7.2, False, "Lose")
print(immutable_var)
#immutable_var [2] = True Кортежи не меняются. 
mutable_list = ([2, 7.2, False, "Lose"], "Good")
mutable_list [0] [0] = 5
mutable_list [0] [1] = 75 + 5
mutable_list [0] [2] = True
mutable_list [0] [3] = "Win"
print(mutable_list)
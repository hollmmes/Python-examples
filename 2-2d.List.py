food = ["pizza","hamburger","salad","sausage",]

print(food)

food.append("ice cream")
food.remove("salad")
food.insert(0,"cake")


for i in food:
    print((i))

food.clear()
    
#2d list
print("-"*50)
fast = ["pizza","hamburger","salad","sausage",]
drink= ["cola","tea","water"]
dessert = ["hmm","tatlı yokki","oyy olsa yerdim"]

food= [fast,drink,dessert]

print(food)

print(food[1][2])


#choosing game left or right

name = input("your name ? ")
print("Welcome", name, "to this adventure." )

answer = input("you are on dirt road, it has come to an end and you go left or right,what whould you choose(left/right) ")

if answer == "left":
    answer = input("you come to river, you can walk around it or swim across? type walk or swim(walk/swim)" )
    if answer == "swim":
        print("you came across and you were eaten by a alligator." )
    elif answer == "walk":
        print("you walked many miles,  ran out of water and died." )
    else: 
        print("choose right option mention above" )

elif answer == "right":
    answer = input("you came to bridge do you want to go back or cross the river type (cross/back)" )
    
    if answer == "back":
        print("you go back and lose." )
    elif answer == "cross":
        answer = input("you crass the river and meet a strager, do you talk to them (yes/no)" )

        if answer == "yes":
            print("you talk to stranger and they give you gold and you win " )
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose" )
    else: 
        print("choose right option mention above" ) 
else:
    print("not a valid options. you lose." )        

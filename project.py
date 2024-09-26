#making full form quiz

print("welcome to the quizes")

playing = input("do you want to play " )
if playing.lower() != "yes":
    quit()
print("okey let's play:)")
score = 0 
answer = input("what's cpu stands for?" )
if answer == "central processing unit":
    print("correct")
    score += 1
else: 
    print("wrong answer try again:)")


answer = input("what's GPU stands for?" )
if answer == "graphical processing unit":
    print("correct")
    score += 1
else: 
    print("wrong answer try again:)")
        
    

answer = input("what's ram stands for?" )
if answer == "rondam access memorey":
    print("correct")
    score += 1
else: 
    print("wrong answer try again:)")
        
    

answer = input("what's rom stands for?" )
if answer == "read only memorey":
    print("correct")
    score += 1
else: 
    print("wrong answer try again:)")

print("you got " + str(score) + "question correct " )
print("percentage " + str(score/4*100))
        
    

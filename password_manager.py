master_pwd = input("whats the master password? ")
def view():
    
     with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)
    
    
def add():
    name = input("Account name: ")
    pwd = input("password:")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd +"\n")
    
while True:
   mode = input("whould u like to view or add new password ")
   if mode == "q":
       break
       
   if mode == "view":
       view()
       
       
   elif mode == "add":
       add()
   else:
       print("invalid")
       
       
             
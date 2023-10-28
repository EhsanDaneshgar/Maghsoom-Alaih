import os
import time
password="Ehsan12345"
password_counter=0
flag = False # only when the flag turens True, Line 19 will be executed.
#flag turnes True in line 12, only if the inserted password is correct.
while True:
    taken_password=str(input("Enter the password:""\t"))
    password_counter=password_counter+1
    if taken_password==password:
        print("Password is corect!")
        flag=True
        break
    elif password_counter==3:
        print( "You just have one more chance to insert the correct password!")
    elif password_counter==4:
        print ("All attempts for password were failed!")
        break

if flag is True:
    time.sleep(3)
    os.system("cls") 
    while True:
        print("Enter a Integer:", end="\t")
        list1=[]
        num=int(input())
        for i in range(1,int(num/2)+1):
            if num%i==0:
                list1.append(i)
        list1.append(num)
        print("List of dividors of %d is:" %(num),list1)
        time.sleep(3) # This order pauses the execution of the program for 3 seconds.
        os.system("cls") # This order clears the screen
    
        while True:
            try:
                flag=int(input("Would you like to countinue? 1) Yes 2) No""\t"))
                if flag==1 or flag==2:
                    break #Valid input, break out of the inner loop
                else:
                    print("Please entereither 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if flag==1:
            continue
        elif flag==2:
            break






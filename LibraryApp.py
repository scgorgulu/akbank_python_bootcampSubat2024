#Coded by Serhat Çağrı Görgülü
import os
import emoji
from Library import Library

message="Welcome to Global Ai Library"
print(message.center(50,"*"))
lib=Library("book.txt")

message="Please choose an action"
print(message.center(50))
menu_list=["Press 1 to ADD  a book",
        "Press 2 to DELETE  a book",
        "Press 3 to LIST",
        "Press q to EXIT"]
while(True): 
    print(*menu_list, sep="\n")  
    menu_action=input()
    if menu_action=="1":
        lib.add_book()
        print("book is added")
    elif menu_action=="2":
        lib.delete_book()
        print("book is deleted")
    elif menu_action=="3":
        lib.list_book()
    elif menu_action=="q":
        print(emoji.emojize("Have a nice day :red_heart:", variant="emoji_type"))
        break
    else: print("Invalid action\nTry again\n")





          

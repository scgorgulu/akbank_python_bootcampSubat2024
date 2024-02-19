#Coded by Serhat Çağrı Görgülü 
from Library import Library

print("Welcome to Global Ai Library".center(100,"*"))
lib=Library("book.txt")
print("Please choose an action".center(100))
menu_list=["Press 1 to ADD  a book",
        "Press 2 to DELETE  a book",
        "Press 3 to LIST",
        "Press 4 to SEARCH the list",
        "Press q to EXIT"]
while(True): 
    print(*menu_list, sep="\n")  
    menu_action=input()
    if menu_action=="1":
        lib.add_book()
    elif menu_action=="2":
        lib.delete_book()
    elif menu_action=="3":
        lib.list_book()
    elif menu_action=="4":
        lib.search_list()
    elif menu_action=="q" or menu_action=="Q":
        print("Have a nice day".center(100,"-"),"\n")
        break
    else: print("Invalid action\nTry again\n")





          

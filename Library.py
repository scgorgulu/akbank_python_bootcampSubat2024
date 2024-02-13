import emoji

class Library:
    def __init__(self) -> None:
        pass
    
    def menu(self):
        menuList=["Press 1 to ADD  a book",
                  "Press 2 to DELETE  a book",
                  "Press 3 to LIST",
                  "Press q to EXIT"]
        while(True): 
            print(*menuList, sep="\n")  
            menuAction=input()
            if menuAction=="1":
                print("book is added")
            elif menuAction=="2":
                print("book is deleted")
            elif menuAction=="3":
                print("books are listed")
            elif menuAction=="q":
                print(emoji.emojize("Have a nice day :red_heart:", variant="emoji_type"))
                break
            else: print("Invalid action\nTry again\n")
       


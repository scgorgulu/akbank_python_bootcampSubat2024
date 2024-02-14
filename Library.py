import os
import emoji

class Library:
    def __init__(self):
        if os.path.exists("book.txt")==False:
            first_line=("id","Book Name", "Author", "Release Date", "# of Pages")
            f=open("book.txt","a+")
            for item in first_line:       
                f.write("{:30}".format(item))
                
    id=1
    def menu(self):
        menuList=["Press 1 to ADD  a book",
                  "Press 2 to DELETE  a book",
                  "Press 3 to LIST",
                  "Press q to EXIT"]
        while(True): 
            print(*menuList, sep="\n")  
            menuAction=input()
            if menuAction=="1":
                self.addBook()
                print("book is added")
            elif menuAction=="2":
                print("book is deleted")
            elif menuAction=="3":
                print("books are listed")
            elif menuAction=="q":
                print(emoji.emojize("Have a nice day :red_heart:", variant="emoji_type"))
                break
            else: print("Invalid action\nTry again\n")
       
    def addBook(self):
        f=open("book.txt", "a+")
        bookname=input("Name of Book?")
        author=input("Author Name?")
        releaseDate=input("Release Date?")
        pages=input("Number of Pages?")
        bookAdd=[str(self.id),bookname,author,releaseDate,pages]
        f.write("\n")
        for item in bookAdd:       
            f.write("{:30}".format(item))
        self.id+=1    
            
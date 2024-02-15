import os
import emoji


class Library:
    def __init__(self):
        if os.path.exists("book.txt")==False:
            first_line=["Book Name", "Author", "Release Date", "# of Pages", "Aktif Mi?"]
            self.writeFile(first_line)
    id=1
    isActive=True
    def writeFile(self,line):
        f=open("book.txt","a+")
        f.write("\n")
        for item in line:
            if item==line[0] or item==line[1]:
               f.write("{:50}".format(item))
            else: f.write("{:15}".format(item))       
    def menu(self):
        message="Please choose an action"
        print(message.center(50))
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
        bookAdd=[bookname,author,releaseDate,pages,str(self.isActive)]   
        self.writeFile(bookAdd)
        
       
       

            
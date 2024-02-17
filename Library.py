import os
import emoji


class Library:
    def __init__(self,file_name):
        if os.path.exists(file_name)==False:
            self.file_name=file_name
            self.f=open(file_name, "a+")
            first_line="Book Name, Author, Release Date, #of Pages"
            self.f.write(first_line)
            self.f.write("\n")
        else: 
            self.file_name=file_name
            self.f=open(file_name, "a+")
            
    def __del__(self):
        self.f.close()
 
    """ def menu(self):
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
                self.add_book()
                print("book is added")
            elif menuAction=="2":
                self.delete_book()
                print("book is deleted")
            elif menuAction=="3":
                self.list_book()
            elif menuAction=="q":
                print(emoji.emojize("Have a nice day :red_heart:", variant="emoji_type"))
                break
            else: print("Invalid action\nTry again\n") """
       
    def add_book(self):
        #f=open("book.txt", "a+")
        book_name=input("Name of Book?: ")
        author=input("Author Name?: ")
        release_date=input("Release Date?: ")
        pages=input("Number of Pages?: ")
        new_book=f"{book_name}, {author}, {release_date}, {pages}"
        print(new_book)
        self.f.seek(0)
        self.f.write(new_book)
        self.f.write("\n")
        
    def delete_book(self):
        #All content in the lines list
        #f=open("book.txt", "r" )
        self.f.seek(0)  
        lines=self.f.read().splitlines()
        is_sure=True
        #the book name has taken
        book_name=input("Please enter the Book Name to Delete: ")
        #if the book is in the list or not will be checked in here
        is_in_list=False
        while(is_sure):
            for line in lines:
                if book_name in line:
                    is_in_list=True   
            if is_in_list==False:
                print("Book Name is not in the List")
                is_sure=False
            break
                
        #Delete Process start
        index=0
        while(is_sure):
            answer=input(f"{book_name} will be deleted. Do you want to continue? Y or N ?\n")
            if answer=='Y' or  answer=='y':
                delete_file=open(self.file_name, "w")
                index_counter=0
                for line in lines:
                    if book_name in line:
                        index=index_counter
                        break
                    index_counter+=1
                for line in lines:
                    if line==lines[index]:
                        continue
                    delete_file.write(line)
                    delete_file.write("\n")
                print(f"{book_name} is deleted")
                break
            elif answer=='N' or answer=='n':
                print(f"{book_name} is not deleted")
                is_sure=False
            else: print("Invalid Aciton")
       
    def list_book(self):
        #f=open("book.txt","r+")
        self.f.seek(0)
        lines=self.f.read().splitlines()
        for line in lines:
            screen_list=line.split(",")
            print(screen_list[0:2])

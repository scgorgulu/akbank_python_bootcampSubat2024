import os
from datetime import datetime
import emoji


class Library:
    def __init__(self,file_name):
        now=datetime.now()
        self.year=now.strftime("%Y")
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
#--------------Adding operation starts here---------------------       
    def add_book(self):
        book_name=input("Name of Book?: ")
        author=input("Author Name?: ")
#Validation of release year
        while(True):
            release_date=input("Release Year?: ")
            try:
                if int(release_date) <=int(self.year):
                    break
                else: print("Invalid data. Please do not enter a future data")
            except:
                print("Invalid data. Please enter release year eg: 1985")
                continue
#Validation of page number       
        while(True):
            pages=input("Number of Pages?: ")
            try:
                if int(pages)>0:
                    break
                else: print("Invalid data. Please enter a positive number")
            except:
                print("Invalid data. Please enter a positive number")
                continue        
#Adding Operation       
        new_book=f"{book_name}, {author}, {release_date}, {pages}"
        print(new_book)
# Reseting line index to zero to avoid from blank lines
        self.f.seek(0)
        self.f.write(new_book)
        self.f.write("\n")
        print(f"{book_name} is added".center(50,"*"))
#--------------Adding Operation ends here------------------
#--------------Starting Deletion Operation-----------------                
    def delete_book(self):
#Taking all content in the lines list
        self.f.seek(0)  
        lines=self.f.read().splitlines()
        is_sure=True
#Taking the book name
        book_name=input("Please enter the Book Name to Delete: ")
#if the book is in the list or not will be checked in here
        is_in_list=False
        while(is_sure):
            for line in lines:
                if book_name in line:
                    is_in_list=True   
            if is_in_list==False:
                print(f"{book_name} is not in the List".center(20,"!"))
                is_sure=False
            break                
#Delete Process start
        index=0
        while(is_sure):
            answer=input(f"{book_name} will be deleted. Do you want to continue? Y or N ?\n")
            if answer=='Y' or  answer=='y':
                self.f.truncate(0)
                index_counter=0
                for line in lines:
                    if book_name in line:
                        index=index_counter
                        break
                    index_counter+=1
                for line in lines:
                    if line==lines[index]:
                        continue
                    self.f.write(line)
                    self.f.write("\n")
                print(f"{book_name} is deleted".center(50,"*"))
                break
            elif answer=='N' or answer=='n':
                print(f"{book_name} is not deleted".center(20,"!"))
                is_sure=False
            else: print("Invalid Aciton".center(50,"*"))
#--------------Deletion operation ends here----------------
#--------------Listing operation starts here---------------       
    def list_book(self):
        self.f.seek(0)
        lines=self.f.read().splitlines()
        for line in lines:
            screen_list=line.split(",")
            print(*screen_list[0:2], sep=" , ")
#-------------Listing operation ends here------------------
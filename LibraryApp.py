from Library import Library
#Coded by Serhat Çağrı Görgülü
print("Welcome to Global Ai Library\nPlease choose an action")
akbank=Library()
menuAction="start"
while(menuAction!="q"):
    akbank.menu()
    menuAction=input()



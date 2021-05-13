from manipulation import Data_Manipulation
#create object
d1=Data_Manipulation()
while True:
    d1.menu()
    ch=int(input("Enter your choice=>"))
    if ch==1:
        d1.insert_record()
    elif ch==2:
        d1.view_record()
    elif ch==3:
        d1.search_record()
    elif ch==4:
        d1.update_salary()
    elif ch==5:
        d1.delete_record()
    elif ch==6:
        break
    else:
        print("invalid choice")

from connect import connection#connect file connect.py
class Data_Manipulation:
    def insert_record(self):
        #create object of class connection
        con=connection()
        #create cursor means create object of cursor
        cur=con.cursor()
        #insert record  into table Employee table
        q="insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #input from user
        eid=int(input("Enter Employee id=>"))
        dno=int(input("Enter department number=>"))
        desig=input("Enter designation=>")
        emn=input("Enter Employee name=>")
        a=int(input("Enter employee age=>"))
        c=input("Enter Empolyee city=>")
        email=input("Enter Email=>")
        p=input("Enter password=>")
        m=input("Enter mobile number=>")
        bs=float(input("Enter basic salary=>"))
        #create tuple
        val=(eid,dno,desig,emn,a,c,email,p,m,bs)
        #insert Query run
        try:
            cur.execute(q,val)
        except:
            print("Query Error")
        else:
            #save in database use commit()
            con.commit()
            print("Record Insert successfully")
        #close connection
            cur.close()
            con.close()
        

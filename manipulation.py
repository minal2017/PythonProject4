from connect import Connection#connect file connect.py
class Data_Manipulation:
    def insert_record(self):
        #create object of class connection
        con1=Connection()
        con=con1.conn()
        #create cursor means create object of cursor
        cur=con.cursor()
        #insert record  into table Employee table
        q="insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #input from user
        empid=int(input("Enter Employee id=>"))
        dno=int(input("Enter department number=>"))
        deptn=input("Enter department name=>")
        desig=input("Enter designation=>")
        emn=input("Enter Employee name=>")
        a=int(input("Enter employee age=>"))
        c=input("Enter Empolyee city=>")
        email=input("Enter Email=>")
        p=input("Enter password=>")
        m=input("Enter mobile number=>")
        bs=float(input("Enter basic salary=>"))
        #create tuple
        val=(empid,dno,deptn,desig,emn,a,c,email,p,m,bs)
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
    def menu(self):
        print("1.insert_record\n2.view_record\n3.search_record\n4.update_salary\n5.delete record\n6.exit")
    def view_record(self):
        con1=Connection()
        con=con1.conn()
        query="SELECT * FROM employee"
        cur=con.cursor()
        #run select query
        cur.execute(query)
        result=cur.fetchall()
        print(result)
        cur.close()
        con.close()
    def search_record(self):
        empid=int(input("Enter Employee id"))
        con1=Connection()
        con=con1.conn()
        query="SELECT * FROM employee  where empid=%s"
        
        cur=con.cursor()
        try:
            cur.execute(query,empid)
            con.commit()
        except Exception:
            print("Query Error")
        else:
            result=cur.fetchall()
            print(result)
        cur.close()
        con.close()
    def update_salary(self):
        con1=Connection()
        con=con1.conn()
        empid=int(input("Enter employee id"))
        basic_salary=float(input("Enter  salary"))
        
        q="UPDATE employee SET basic_salary=%s where empid=%s"
        cur=con.cursor()
        q="select salary from employee where empid=%s"
        cur.execute(q,empid)
        result=cur.fetchall()
        sal=result[0]
        #print("current salary",sal)
        s1=sal[0]
        print("current salary",s1)
        s1=s1+s1*s/100
        print("after salary",s1)
        val=(s1,empid)
        
        
        try:
            cur.execute(q,val)
            con.commit()
            print("Record update successfully")
        #print("record update successfully")
        except:
            print("Record not found")
        cur.close()
        con.close()
    def delete_record(self):
        con1=Connection()
        con=con1.conn()
        empid=int(input("Enter employee id no. to be delete=>"))
        q="delete from employee where empid=%s"
        cur=con.cursor()
        try:
            cur.execute(q,empid)
            con.commit()
            print("record delete successfully")
        except:
            print("record not found")
        cur.close()
        con.close()
    



        
        
        

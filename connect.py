import pymysql
class Connection:#connection user defind class
    def conn(self):#constructor function
        #
        self.servername="localhost"
        self.username="root"
        self.password=""
        self.dbname="employee_managment"
        try:
            self.con=pymysql.connect(self.servername,self.username,self.password,self.dbname)
            
        except:
            print("connectivity Error")
        else:
            print("connect successfully")
            return self.con


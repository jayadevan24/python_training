import pyodbc

#DESKTOP-Q8SRJL9\SQLEXPRESS

connection_string = r'Driver={SQL Server};Server=DESKTOP-Q8SRJL9\SQLEXPRESS;Database=employee_db;Trusted_Connection=yes;'

#select query
connection_obj = pyodbc.connect(connection_string)
curser_obj = connection_obj.cursor()

#executing the sql statements inside our mssql serrver
my_query = 'SELECT * FROM employees WHERE SALARY<70000'
curser_obj .execute(my_query)

'''
#data access method 1
for i in curser_obj:
    print(i)


#data access method 2
for eachrow in curser_obj.fetchall():
    print(eachrow) #each row is a pyodbc object

'''

#data access method 3
employees=[{'EMPLOYEEID':eachrow[0],'EMPLOYEENAME':eachrow[1]} for eachrow in curser_obj.fetchall()]

print(type(employees)) #list of dictionaries
print(type(employees[0])) #a single dictionary (row) of data

print(employees) #the entire list of dictionaries

curser_obj=connection_obj.close() #to reset the cursor


#CREATE TABLE QUERY
#--------------------

connection_obj=pyodbc.connect(connection_string)

#create tbale can have many unexpected outcmomes,have in try block

try:
    curser_obj = connection_obj.cursor()
    my_query='''CREATE TABLE employeemasternew 
    (id INT IDENTITY PRIMARY KEY,
    EMPLOYEECODE Varchar(20),
    EmployeeName varchar(50),
    Salary int)'''

    curser_obj.execute(my_query) #try to execute

except Exception as e:
    print('Cannot create thetable because of this error:')
    print(f'{type(e).__name__} was raised. Details are as follow:')
    #print short name of error
    print(e)

connection_obj.commit()# commit for all create ,update,del queries
#close the connection
curser_obj=connection_obj.close()


#INSERT query
connection_obj = pyodbc.connect(connection_string)
curser_obj = connection_obj.cursor()

#executing the sql statements inside our mssql serrver
my_query = '''INSERT INTO employeemasternew VALUES 
('EMP001','George BUsh',10000)'''
curser_obj.execute(my_query)
connection_obj.commit()# commit for all create ,update,del queries

curser_obj= connection_obj.close()

#UPDATE query
connection_obj = pyodbc.connect(connection_string)
curser_obj = connection_obj.cursor()

#executing the sql statements inside our mssql serrver
my_query = '''UPDATE employeemasternew SET EmployeeName ='Joe biden ' where EmployeeName='George BUsh' '''
curser_obj.execute(my_query)
connection_obj.commit()# commit for all create ,update,del queries

curser_obj= connection_obj.close()


#delete query
connection_obj = pyodbc.connect(connection_string)
curser_obj = connection_obj.cursor()

#executing the sql statements inside our mssql serrver
my_query = '''DELETE FROM employeemasternew WHERE EmployeeName='Joe biden' '''
curser_obj.execute(my_query)
connection_obj.commit()# commit for all create ,update,del queries

curser_obj= connection_obj.close()






























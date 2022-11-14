#Exercise/mini Project: Hospital Information System
#Exercise 1: Connect to your database server and print its version
'''import sqlite3
conn = sqlite3.connect('python_db.db')
cursor = conn.cursor()'''
'''cursor.execute("""CREATE TABLE Hospital(Hospital_id int not null primary key,\
    Hospital_name text not null, Bed_count int not null )""")
conn.commit() '''
'''cursor.execute("INSERT INTO Hospital(Hospital_id,Hospital_name,Bed_count)values\
    ('1','Mayo Clinic',200),('2','Cleveland Clinic',400),\
        ('3','Johns Hopkins',1000),('4','UCLA Medical Center',1500)")
conn.commit()'''
'''cursor.execute("CREATE TABLE Doctor(doctor_id int not null primary key,\
    doctor_name text not null,Hospital_id int not null,joining_date text not null,\
        speciality text not null,salary int not null,experience int)")
conn.commit()'''
'''cursor.execute("INSERT INTO Doctor(doctor_id,doctor_name,Hospital_id,joining_date,speciality,\
    salary,experience) values\
        ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL),\
        ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL),\
        ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL),\
        ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL),\
        ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL),\
        ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL),\
        ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL),\
        ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL)")  
conn.commit()'''
#in this exercise i've also used DB Browser(SQLIte) tool
import sqlite3
def get_connection():
    conn = sqlite3.connect('python_db.db')
    return conn
def close_connection(connection):
    if connection:
        connection.close()    
#Exercise 1: Connect to your database server and print its version
'''def get_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchall()
        print('version is',db_version)
        close_connection(connection)
    except (Exception,sqlite3.Error) as error:
        print('error while getting data',error)   
print("Question 1: Print Database version")         
get_version()'''

#Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id
'''def get_hospital_detail(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query_select = "SELECT * FROM hospital WHERE hospital_id = ?"
        cursor.execute(query_select,(hospital_id,))
        print("Printing hospital record")
        data = cursor.fetchall()
        for d in data:
            print("hospital_id",d[0])
            print("hospital name",d[1])
            print("bed count",d[2])
        close_connection(connection)    
    except (Exception,sqlite3.Error) as error:
        print('error while getting data',error)  
def get_doctor_detail(doctor_id):
    try:
        connection = get_connection()  
        cursor = connection.cursor()
        query_select = "SELECT * FROM doctor WHERE doctor_id = ?"
        cursor.execute(query_select,(doctor_id,))
        print("Printing doctor record")
        data = cursor.fetchall()
        for d in data:
            print("doctor_id",d[0])
            print("doctor name",d[1])
            print("hospital_id",d[2])
            print("joining date",d[3])
            print("speciality",d[4])
            print("salary",d[5])
            print("experience",d[6])
        close_connection(connection)     
    except (Exception,sqlite3.Error) as error:
        print('error while getting data',error)   
print("Question 2: Read given hospital and doctor details \n")                
get_hospital_detail(2)
print("\n)
get_doctor_detail(105)'''

#Exercise 3: Get the list Of doctors as per the given specialty and salary
'''def get_specialist_by_salary(speciality,salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query_select = "SELECT * FROM doctor WHERE speciality = ? and salary > ?"
        cursor.execute(query_select,(speciality,salary))
        print("Printing doctors whose specialty is Garnacologist and salary greater than 30000 ")
        data = cursor.fetchall()
        for d in data:
            print("doctor_id",d[0])
            print("doctor name",d[1])
            print("hospital_id",d[2])
            print("joining date",d[3])
            print("speciality",d[4])
            print("salary",d[5])
            print("experience",d[6],'\n')
        close_connection(connection)    
    except (Exception,sqlite3.Error) as error:
        print('error while getting data',error)  
print("Question 3: Get Doctors as per given Speciality\n")           
get_specialist_by_salary('Garnacologist',30000) '''

#Exercise 4: Get a list of doctors from a given hospital
'''def get_hospital(hospital_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query_select = "SELECT * FROM hospital WHERE hospital_id = ?"
        cursor.execute(query_select,(hospital_id,))
        data = cursor.fetchone()
        close_connection(connection)
        return data[1]
    except (Exception,sqlite3.Error)as error:
        print('error while getting data',error)    
def get_doctors(hospital_id):
    try:
        hospital_name = get_hospital(hospital_id)
        connection = get_connection()
        cursor = connection.cursor()
        query_select = "SELECT * FROM doctor WHERE hospital_id = ?"
        cursor.execute(query_select,(hospital_id,))
        print('Printing Doctors name of',hospital_name,'Hospital')
        data = cursor.fetchall()
        for d in data:
            print('doctor_id',d[0])
            print('doctor name',d[1])
            print('hospital_id',d[2])
            print("joining date",d[3])
            print("speciality",d[4])
            print("salary",d[5])
            print("experience",d[6],'\n')
        close_connection(connection)       
    except (Exception,sqlite3.Error)as error:
        print('error while getting data',error)   
print("Question 4:  Get List of doctors of a given Hospital Id\n")
get_doctors(3)  '''

#Operation 5: Update doctor experience in years
'''from dateutil.relativedelta import relativedelta
import datetime,sqlite3
def update_doctor_experience(doctor_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query_select = "SELECT joining_date FROM doctor WHERE doctor_id=?"
        cursor.execute(query_select,(doctor_id,))
        joining_date = cursor.fetchone()
        joining_date2 = datetime.datetime.strptime(''.join(map(str,joining_date)),'%Y-%m-%d')
        today_date = datetime.datetime.now()
        experience = relativedelta(today_date,joining_date2).years
        connection = get_connection() 
        cursor = connection.cursor()
        query_update = "UPDATE doctor SET experience = ? WHERE doctor_id = ?"
        cursor.execute(query_update,(experience,doctor_id))
        connection.commit() 
        print('Doctor Id: ',doctor_id,'Experience updated to: ',experience,'years')
        close_connection(connection)
    except (Exception,sqlite3.Error)as error:
        print('error while getting data',error)
print("Question 5: Calculate and Update experience of all doctors  \n")        
update_doctor_experience(101) '''                 
       
import mysql.connector
from mysql.connector import Error
import mysql.connector          
from time import sleep
import keyboard
from prettytable import PrettyTable
from os import system

#Creating a connection to MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='from-director.gl.at.ply.gg',
            port='36481',
            database='HospitalManagement',
            user='pythonconnection',
            password='pythonconnection'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

#creating Appointment query 
def create_appointment(connection):
    cursor = connection.cursor()
    doctor_id = int(input("Enter Doctor ID assigned to the patient: "))
    patient_id = input("Enter Patient ID: ")
    report = input("Enter Report: ")
    payment = input("Enter Payment ID: ")
    date=input("Enter the Date for the appointment: ")
    time=input("Enter the time for the appointment: ")
    query = "INSERT INTO department (DoctorId, PatientId, ReportOfPatient, PaymentId, Date, Time) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (doctor_id, patient_id, report, payment, date, time))
    connection.commit()
    print("Appointment created successfully.")

def insert_doctor(connection):
    cursor = connection.cursor()
    doctor_id = integer_input("Enter Doctor ID: ")
    doctor_name = input("Enter the name of the doctor: ")
    designation = input("Enter job designation: ")
    doj = input("Enter Date of Joining (YYYY-MM-DD): ")
    salary=0
    bonus=0
    password=password_create("Create a password (Leave it blank to cancel creation): ")
    if password==-1:
        return -1
    name=input("Enter your full name: ")
    query = "INSERT INTO doctor (DoctorId, Designation, Salary, Bonus, DoctorName, DOJ, Password, Name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (doctor_id, designation, salary, salary, bonus, doctor_name, doj, password, name))
    connection.commit()
    print("Doctor data inserted successfully.")
    sleep(3)

def insert_patient(connection):
    cursor = connection.cursor()
    guardid = integer_input("Enter Guardian ID: ")
    phno = input("Enter the name of the doctor: ")
    address = input("Enter your address: ")
    dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
    weight=float_input("Enter your Weight in KG: ")
    height=float_input("Enter your height in CM: ")
    password=password_create("Create a password (Leave it blank to cancel creation): ")
    if password==-1:
        return -1
    name=input("Enter your full name: ")
    query = "INSERT INTO patient (GuardianId,Phno,Address,DOB,Weight,Height,password,Name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (guardid, phno, address, dob, weight, height ,password, name))
    connection.commit()
    print("Patient data inserted successfully.")
    sleep(3)

def insert_guardian(connection):
    cursor = connection.cursor()
    phno = input("Enter the name of the doctor: ")
    emailid = input("Enter your email id: ")
    address = input("Enter your address: ")
    name=input("Enter your full name: ")
    query = "INSERT INTO guardian (GuardianName,Phno,Emailid,Address) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name,phno,emailid,address))
    connection.commit()
    print("Patient data inserted successfully.")
    sleep(3)

def retrieve_patient_record(connection, patientid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient where PatientId=%s" % patientid)
    records = cursor.fetchall()
    records = list(records[0])
    return records
def retrieve_guardian_record(connection, guardianid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM guardian where GuardianId=%s" % guardianid)
    records = cursor.fetchall()
    records = list(records[0])
    return records

def retrieve_doctor_appointments(connection, doctorid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Appointments where DoctorId=%s" % doctorid)
    records = cursor.fetchall()
    return records

def retrieve_doctor_record(connection, doctorid):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM doctor where DoctorId=%s" % doctorid)
    records = cursor.fetchall()
    records = list(records[0])
    return records

def password_input(msg, password):
    while True:
        print("Don't type anything to exit")
        inp=input(msg)
        inp=inp.lower()
        if inp is None:
            print("Please enter some data") 
        elif len(inp)>255:
            print("The password cannot be longer than 255 characters")
        elif inp=="":
            return -1
        elif inp!=password:
            print("The password entered is incorrect")
        else:
            return inp
        
def password_create(msg):
    while True:
        print("Press enter to exit")
        inp=input(msg)
        inp=inp.lower()
        if inp is None:
            print("Please enter some data")
        elif len(inp)>255:
            print("The password cannot be longer than 255 characters")
        elif inp=="":
            return -1
        else:
            confirminp=input("Please reenter your password: ")
            confirminp.lower()
            if confirminp==inp:
                return inp
            else:
                print("The entered passwords don't match. Please try again")

def clear_screen():
    system('cls')

def retrieve_payments(connection,patientid):
    cursor=connection.cursor()
    cursor.execute("Select * from Payments where PatientId=%s" % patientid)
    table=PrettyTable()
    table.field_names=["PaymentID","Cost","Discount","Payment Mode","Card or UPI ID", "Date", "Patient ID"]
    records=cursor.fetchall()
    for item in records:
        table.add_row(item)
    print(table)

def update_patient(connection,attribute,patientid,typeofmsg):
    tempblockenter(0.5)
    cursor=connection.cursor()
    if typeofmsg=="int":
        inp=integer_input("Please enter the new value: ")
        cursor.execute("Update patient set %s=%s where PatientId=%s" % (attribute,inp,patientid))
    elif typeofmsg=="float":
        inp=float_input("Please enter the new value: ")
        cursor.execute("Update patient set %s=%s where PatientId=%s" % (attribute,inp,patientid))
    elif typeofmsg=="text":
        inp=input("Please enter the new value: ")
        cursor.execute("Update patient set %s='%s' where PatientId=%s" % (attribute,inp,patientid))
    elif typeofmsg=="password":
        inp=password_create("Please enter the new password: ")
        cursor.execute("Update patient set %s='%s' where PatientId=%s" % (attribute,inp,patientid))
    connection.commit()

def update_doctor(connection,attribute,doctorid,typeofmsg):
    tempblockenter(0.5)
    cursor=connection.cursor()
    if typeofmsg=="int":
        inp=integer_input("Please enter the new value: ")
        cursor.execute("Update doctor set %s=%s where DoctorId=%s" % (attribute,inp,doctorid))
    elif typeofmsg=="float":
        inp=float_input("Please enter the new value: ")
        cursor.execute("Update doctor set %s=%s where DoctorId=%s" % (attribute,inp,doctorid))
    elif typeofmsg=="text":
        inp=input("Please enter the new value: ")
        cursor.execute("Update doctor set %s='%s' where DoctorId=%s" % (attribute,inp,doctorid))
    elif typeofmsg=="password":
        inp=password_create("Please enter the new password: ")
        cursor.execute("Update doctor set %s='%s' where DoctorId=%s;" % (attribute,inp,doctorid))
    connection.commit()

def update_appointment(connection,attribute,appid,typeofmsg):
    tempblockenter(0.5)
    cursor=connection.cursor()
    if typeofmsg=="int":
        inp=integer_input("Please enter the new value: ")
        cursor.execute("Update Appointments set %s=%s where AppointmentId=%s" % (attribute,inp,appid))
    elif typeofmsg=="float":
        inp=float_input("Please enter the new value: ")
        cursor.execute("Update Appointments set %s=%s where AppointmentId=%s" % (attribute,inp,appid))
    elif typeofmsg=="text":
        inp=input("Please enter the new value: ")
        cursor.execute("Update Appointments set %s='%s' where AppointmentId=%s" % (attribute,inp,appid))
    elif typeofmsg=="password":
        inp=password_create("Please enter the new password: ")
        cursor.execute("Update Appointments set %s='%s' where AppointmentId=%s;" % (attribute,inp,appid))
    elif typeofmsg=="date":
        inp=input("Please enter the date in the format of YYYY-MM-DD: ")
        cursor.execute("Update Appointments set %s='%s' where AppointmentId=%s;" % (attribute,inp,appid))
    elif typeofmsg=="time":
        inp=input("Please enter the time in the format of HH:MM: ")
        inp+=":00"
        cursor.execute("Update Appointments set %s='%s' where AppointmentId=%s;" % (attribute,inp,appid))
    connection.commit()

def create_menu(listformenu, beginmsg=""):
    pointat=0
    updatescreen=1
    while True:
        tempblockenter(0.1)
        if keyboard.is_pressed("down"):
            if pointat<len(listformenu)-1:
                pointat+=1
                clear_screen()
                updatescreen=1
        elif keyboard.is_pressed("up"):
            if pointat>0:
                pointat-=1
                updatescreen=1
        elif keyboard.is_pressed("enter"):
            clear_screen()
            return pointat+1
        if updatescreen!=0:
            clear_screen()
            print(beginmsg)
            for i in range(len(listformenu)):
                print(listformenu[i], end=" ")
                if i==pointat:
                    print("<",  end="")
                print()
                updatescreen=0

def blockalpha():
    charlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","'","\"","{","}","[","]","(",")",",",".","/","\\","~","`"]
    for item in charlist:
        keyboard.block_key(item)

def unblockalpha():
    charlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","'","\"","{","}","[","]","(",")",",",".","/","\\","~","`"]
    for item in charlist:
        keyboard.unblock_key(item)

def integer_input(msg):
    blockalpha()
    while True:
        inp=input(msg)
        if inp.isdigit():
            inp=int(inp)
            break
        else:
            print("The text you entered is not a digit")
    unblockalpha()
    return inp

def float_input(msg):
    blockalpha()
    keyboard.unblock_key(".")
    while True:
        inp=input(msg)
        if inp.isdecimal():
            inp=float(inp)
            break
        else:
            print("The text you entered is not a digit")
    unblockalpha()
    return inp

def tempblockenter(time=0.3):
    keyboard.block_key("enter")
    sleep(time)
    keyboard.unblock_key("enter")

def viewallappointment(connection):
    cursor=connection.cursor()
    cursor.execute("Select * from Appointments;")
    records=cursor.fetchall()
    return records

def deleteappointment(connection, appid):
    cursor=connection.cursor()
    cursor.execute("Delete from Appointments where AppointmentId=%s;" % appid)
    cursor.commit()

def deletedoctor(connection, docid):
    cursor=connection.cursor()
    cursor.execute("Delete from doctor where DoctorId=%s;" % docid)
    cursor.commit()

def deletepatient(connection, patid):
    cursor=connection.cursor()
    cursor.execute("Delete from patient where PatientId=%s;" % patid)
    cursor.commit()
    
def deleteguardian(connection, guid):
    cursor=connection.cursor()
    cursor.execute("Delete from guardian where GuardianId=%s;" % guid)
    cursor.commit()

while True:
    connection = create_connection()
    if connection is None:
        print("Failed to create connection to the database.")

        print("The program will automatically close in 5 seconds...")
        sleep(5)
        exit()
    else:
        match create_menu([ "Sign Up", "Login as Patient", "Login as Doctor", "Login as Receptionist", "Login as HR", "Exit the Program"], "Use the Up and Down arrow keys to navigate the menu and enter key to select an option:"):
            case 1:
                match create_menu(["Create a Patient Account", "Create a Guardian Account", "Create a doctor Account", "Cancel"], "Select an option:"):
                    case 1:
                        insert_patient(connection)
                    case 2:
                        insert_guardian(connection)
                    case 3:
                        password=input("Enter the password given to you by the admin/recruiter: ")
                        if password=="doc":
                            insert_doctor(connection)
                        else:
                            print("Wrong password please try again")
                            sleep(3)
                    case 4:
                        pass
            case 2:
                tempblockenter(0.5)
                patientid=integer_input("Enter your patient ID: ")
                record=retrieve_patient_record(connection, patientid)
                if record==[]:
                    print("The patientid specified does not exist please try again")
                    sleep(3)
                    continue
                tempblockenter(0.5)
                if password_input("Enter your password: ", record[8])==-1:
                    continue
                while True:
                    tempblockenter(0.5)
                    match create_menu(["View Your Account", "Edit Your Account", "View Payment Records", "LogOut"], "Select an Option:"):
                        case 1:
                            table = PrettyTable()
                            table.field_names = ["Patient ID", "Guardian ID", "Phone No", "Address", "DOB", "Weight", "Height", "RoomNo", "Password", "Name"]
                            table.add_row([record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]])
                            print(table)
                            print("Press ESC to continue...")
                            keyboard.wait("Esc")
                        case 2:
                            match create_menu(["Guardian ID","Phone No","Address","DOB","Weight","Height","Password","Name", "Cancel"],"Select what you want to edit:"):
                                case 1:
                                    update_patient(connection,"GuardianId",patientid,"int")
                                case 2:
                                    update_patient(connection,"Phno",patientid,"int")
                                case 3:
                                    update_patient(connection,"Address",patientid,"text")
                                case 4:
                                    update_patient(connection,"DOB",patientid,"text")
                                case 5:
                                    update_patient(connection,"Weight",patientid,"float")
                                case 6:
                                    update_patient(connection,"Height",patientid,"float")
                                case 7:
                                    update_patient(connection,"password",patientid,"password")
                                case 8:
                                    update_patient(connection,"Name",patientid,"text")
                                case 9:
                                    pass
                        case 3:
                            retrieve_payments(connection,patientid)
                            print("Press ESC to continue...")
                            keyboard.wait("Esc")
                        case 4:
                            print("Logging out")
                            sleep(2)
                            break
            case 3:
                tempblockenter(0.5)
                doctorid=integer_input("Enter your doctor ID: ")
                record=retrieve_doctor_record(connection, doctorid)
                if record==[]:
                    print("The patientid specified does not exist please try again")
                    continue
                tempblockenter(0.5)
                if password_input("Enter your password: ", record[7])==-1:
                    continue
                tempblockenter(0.5)
                while True:
                    match create_menu(["View your Account", "Edit your Account", "View your appointments", "View Patient Records", "LogOut"],"Select an Option:"):
                        case 1:
                            record=viewallappointment(connection)
                            table = PrettyTable()
                            table.field_names = ["Doctor ID", "Designation", "Salary", "Department", "Bonus", "Doctor Name", "DOJ", "Password", "Name"]
                            table.add_row([record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]])
                            print(table)
                            print("Press ESC to continue...")
                            keyboard.wait("Esc")
                        case 2:
                            match create_menu(["Password","Name", "Cancel"],"Select what you want to edit:"):
                                case 1:
                                    update_doctor(connection,"Password",doctorid,"password")
                                case 2:
                                    update_doctor(connection,"Name",doctorid,"text")
                                case 3:
                                    pass
                        case 3:
                            records=retrieve_doctor_appointments(connection,doctorid)
                            table=PrettyTable()
                            table.field_names=["Doctor ID","Patient ID","Report Of Patient","PaymentID","Date","Time"]
                            for item in records:
                                table.add_row(item)
                            print(table)
                            print("Press ESC to continue...")
                            keyboard.wait("Esc")
                        case 4:
                            patientid=integer_input("Enter the patient ID: ")
                            record=retrieve_patient_record(connection, patientid)
                            if record==[]:
                                print("The patient ID specified does not exist please try again")
                                sleep(3)
                                continue
                            table = PrettyTable()
                            table.field_names = ["Patient ID", "Guardian ID", "Phone No", "Address", "DOB", "Weight", "Height", "RoomNo", "Password", "Name"]
                            table.add_row([record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9]])
                            print(table)
                            print("Press ESC to continue...")
                            keyboard.wait("Esc")
                        case 5:
                            print("Logging Out...")
                            sleep(3)
                            break
            case 4:
                password=input("Enter the reception password: ")
                if password=='reception':
                    while True:

                        match create_menu(["View All Appointments", "Create an Appointment", "Edit an Appointment", "Delete an Appointment", "LogOut"],"Select an option:"):
                            case 1:
                                table = PrettyTable()
                                table.field_names = ["Appointment ID", "Doctor ID", "Patient ID", "Patient Report", "Payment ID", "Date", "Time"]
                                table.add_row([record[6],record[0],record[1],record[2],record[3],record[4],record[5]])
                                print(table)
                                print("Press ESC to continue...")
                                keyboard.wait("Esc")
                            case 2:
                                create_appointment(connection)
                            case 3:
                                appid=integer_input("Enter the Appointment ID: ")
                                match create_menu(["Doctor ID", "Patient ID", "Payment ID", "Date", "Time", "Cancel"], "Select what you want to edit:"):
                                    case 1:
                                        update_appointment(connection,"DoctorId",appid,"int")
                                    case 2:
                                        update_appointment(connection,"PatientId",appid,"int")
                                    case 3:
                                        update_appointment(connection,"PaymentId",appid,"int")
                                    case 4:
                                        update_appointment(connection,"Date",appid,"date")
                                    case 5:
                                        update_appointment(connection,"Time",appid,"time")
                                    case 6:
                                        pass
                            case 4:
                                appid=integer_input("Enter the Appointment ID: ")
                                deleteappointment(connection,appid)
                            case 5:
                                print("Logging Out...")
                                sleep(3)
                                break
                else:
                    continue
            case 5:
                password=input("Enter the admin password: ")
                if password=='admin':
                    while True:
                        match create_menu(["Delete a Patient Record","Delete A Guardian Record", "Delete a Doctor Record", "Edit a Doctor Record", "LogOut"]):
                            case 1:
                                patientid=integer_input("Enter patient ID to delete: ")
                                record=retrieve_patient_record(connection, patientid)
                                if record==[]:
                                    print("The patientid specified does not exist please try again")
                                    sleep(3)
                                    continue
                                deletepatient(connection,patientid)
                            case 2:
                                guardianid=integer_input("Enter guardian ID to delete: ")
                                record=retrieve_guardian_record(connection, guardianid)
                                if record==[]:
                                    print("The guardianid specified does not exist... please try again")
                                    sleep(3)
                                    continue
                                deleteguardian(connection,guardianid)
                            case 3:
                                doctorid=integer_input("Enter doctor ID to delete: ")
                                record=retrieve_patient_record(connection, doctorid)
                                if record==[]:
                                    print("The doctorid specified does not exist please try again")
                                    sleep(3)
                                    continue
                                deletedoctor(connection,doctorid)
                            case 4:
                                doctorid=integer_input("Enter doctor ID to edit: ")
                                record=retrieve_patient_record(connection, doctorid)
                                if record==[]:
                                    print("The doctorid specified does not exist please try again")
                                    sleep(3)
                                    continue
                                match create_menu(["Designation","Salary","Bonus","Department", "Cancel"],"Select an option to edit:"):
                                    case 1:
                                        update_doctor(connection,"Designation",doctorid,"text")
                                    case 2:
                                        update_doctor(connection,"Salary",doctorid,"float")
                                    case 3:
                                        update_doctor(connection,"Bonus",doctorid,"float")
                                    case 4:
                                        update_doctor(connection,"Department",doctorid,"text")
                                    case 5:
                                        pass
                            case 5:
                                print("Logging Out...")
                                sleep(3)
                                break
            case 6:
                print("Closing the program. Thank you for using the Hospital Database Managment System")
                sleep(3)
                exit()
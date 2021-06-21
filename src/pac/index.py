from dal.Json_doctor import JsonDoctor
from dal.Json_patient import JsonPatient
from dal.Write_data import WriteData
from flows.add_patient import AddPatientFlow
from flows.delete_appointment_by_id import DeleteAppointmentByIdFlow
from flows.delete_patient_by_id import DeletePatientByIdFlow
from flows.get_appointments import AppointmentsListFlow
from flows.get_available_doctors import AvailableDoctorsListFlow
from flows.get_doctor_by_id import GetDoctorByIdFlow
from flows.get_doctors import DoctorsListFlow
from flows.get_patient_by_id import GetPatientByIdFlow
from flows.get_patients import PatientsListFlow
from flows.get_waiting_list import WaitingListFlow
from model.config_model import Patient, Doctor

Patient_New_List_Json_File_Path = 'local_json/PatientData.json'
Doctor_New_List_Json_File_Path = 'local_json/DoctorData.json'

Patients_DataBase = PatientsListFlow().get_all_patients()
Doctors_DataBase = DoctorsListFlow().get_all_doctors()
Appointments_DataBase = AppointmentsListFlow.get_all_appointments()
doctors_list_data = Patients_DataBase
patients_list_data = Doctors_DataBase
#  for patient in patients_list_data:

print("********************************************************************")
print("*                                                                  *")
print("*      Welcome to Hospital appointment system for doctors          *")
print("*                                                                  *")
print("********************************************************************")

tries = 0
tries_flag = ""
while tries_flag != "Close the program":

    print("-----------------------------------------")
    print("|Enter 1 for Admin mode			|\n|Enter 2 for Patient mode 	|\n|Enter 3 for Doctor mode		|")
    print("-----------------------------------------")
    Admin_user_mode = input("Enter your mode : ")

    if Admin_user_mode == "1":  # Admin mode
        print(
            "*****************************************\n|         Welcome to admin mode         |\n*****************************************")
        Password = input("Please enter your password : ")
        while True:

            if Password == "1234":
                print("-----------------------------------------")
                print(
                    "|To manage patients Enter 1 		|\n|To manage doctors Enter 2	 	"
                    "|\n|To manage appointments Enter 3 	|\n|To be back Enter E			|")
                print("-----------------------------------------")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Patients Management
                    print("-----------------------------------------")
                    print("|To add new patient Enter 1	  	|")
                    print("|To display patient Enter 2	  	|")
                    print("|To delete patient data Enter 3		|")
                    print("|To Back enter E      			|")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Patients Management --> Enter new patient data
                        try:  # To avoid non integer input
                            patient_id = int(input("Enter patient ID : "))
                            while patient_id in Patients_DataBase:  # if Admin entered used ID
                                patient_id = int(input("This ID is unavailable, please try another ID : "))
                            Name = input("Enter patient name                      : ")
                            DoctorName = input("Enter name of doctor following the case : ")
                            patient_phone = input("Enter patient age                       : ")
                            patient_message = input("Enter patient gender                    : ")
                            res_patient = Patient(patient_id, Name, DoctorName, patient_phone, patient_message)
                            JsonPatient.read_and_create(res_patient)
                            WriteData(Patient_New_List_Json_File_Path).init_patients_data()
                            print("----------------------Patient added successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Patients Management --> Display patient data
                        try:  # To avoid non integer input
                            patient_id = int(input("Enter patient ID : "))
                            while patient_id not in Patients_DataBase:
                                patient_id = int(input("Incorrect ID, Please Enter patient ID : "))
                            patient_flow_C_2 = GetPatientByIdFlow(patient_id)
                            result = patient_flow_C_2.get_patient_by_id()
                            print("\npatient name        : ", result.patient_full_name)
                            print("patient Doctor         : ", result.doctor_full_name)
                            print("patient Phone      : ", result.patient_phone)
                            print("patient Message     : ", result.patient_message)
                            print("patient is in " + result.patient_waiting_status + " Status")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Patients Management --> Delete patient data
                        try:  # To avoid non integer input
                            patient_id = int(input("Enter patient ID : "))
                            while patient_id not in Patients_DataBase:
                                patient_id = int(input("Incorrect ID, Please Enter patient ID : "))
                            flow_delete = DeletePatientByIdFlow(patient_id)
                            flow_delete.remove_patient()
                            print("----------------------Patient data deleted successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "E":  # Admin mode --> Patients Management --> Back
                        break

                    else:
                        print("Please enter a correct choice\n")

                elif AdminOptions == "2":  # Admin mode --> Doctors Management
                    print("-----------------------------------------")
                    print("|To add new doctor Enter 1              |")
                    print("|To display doctor Enter 2              |")
                    print("|To be back enter E                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Doctors Management --> Enter new doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                                Doctor_ID = int(input("This ID is unavailable, please try another ID : "))
                            Name = input("Enter Doctor name       : ")
                            doctor_phone = input("Enter Doctor phone    : ")
                            doctor_available_status = input("Enter Doctor available status : ")
                            doctor_available_dates = input("Enter Doctor dates : ")
                            doctor_specialty = input("Enter Doctor department : ")
                            res_doctor = Doctor(Doctor_ID, Name, doctor_phone, doctor_available_status,
                                                doctor_available_dates, doctor_specialty)
                            JsonDoctor.read_and_create(res_doctor)
                            WriteData(Doctor_New_List_Json_File_Path).init_doctors_data()
                            print("----------------------Doctor added successfully----------------------")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Doctors Management --> Display doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            doctor_flow_C_2 = GetDoctorByIdFlow(Doctor_ID)
                            result_doc_by_id_C_2 = doctor_flow_C_2.get_doctor_by_id()
                            print("Doctor name    : ", result_doc_by_id_C_2.doctor_full_name)
                            print("Doctor phone : ", result_doc_by_id_C_2.doctor_phone)
                            print("Doctor available status : ", result_doc_by_id_C_2.doctor_available_status)
                            print("Doctor available dates : ", result_doc_by_id_C_2.doctor_available_dates)
                            print("Doctor specialty : ", result_doc_by_id_C_2.doctor_specialty)
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "E":  # Back
                        break

                    else:
                        print("\nPlease enter a correct choice\n")

                elif AdminOptions == "3":  # Admin mode --> Appointment Management
                    print("-----------------------------------------")
                    print("|To book an appointment Enter 1         |")
                    print("|To cancel an appointment Enter 3       |")
                    print("|To be back enter E                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()
                    if Admin_choice == "1":  # Admin mode --> Appointment Management --> Book an appointment
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter the ID of doctor : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
                            doctor_flow_C_3 = GetDoctorByIdFlow(Doctor_ID)
                            result_doc_by_id_C_3 = doctor_flow_C_3.get_doctor_by_id()
                            print("---------------------------------------------------------")
                            print(
                                "|For book an appointment for an exist patient Enter 1   |\n|For book an appointment for a new patient Enter 2      |\n|To be Back Enter E                                     |")
                            print("---------------------------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                patient_id = int(input("Enter patient ID : "))
                                while patient_id not in Patients_DataBase:  # if Admin entered incorrect ID
                                    patient_id = int(input("Incorrect ID, please Enter a correct patient ID : "))

                            elif Admin_choice == "2":
                                patient_id = int(input("Enter patient ID : "))
                                while patient_id in Patients_DataBase:  # if Admin entered used ID
                                    patient_id = int(input("This ID is unavailable, please try another ID : "))
                                Department = result_doc_by_id_C_3.doctor_specialty
                                DoctorName = result_doc_by_id_C_3.doctor_full_name
                                Name = input("Enter patient name    : ")
                                Phone = input("Enter patient phone    : ")
                                message = input("Enter patient message  : ")
                                status = input("Enter Waiting Status : ")
                                RoomNumber = ""
                                res_patient_n = Patient(patient_id, Name, DoctorName, Phone, message, status)
                                new_p_flow = AddPatientFlow(res_patient_n)
                                new_p_flow.add_patient()

                            elif Admin_choice == "E":
                                break

                            Session_Start = input("Session starts at : ")
                            while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                Session_Start = input(
                                    "Appointments should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")

                            for i in Doctors_DataBase[Doctor_ID]:
                                if type(i[0]) != str:
                                    while Session_Start >= i[1] and Session_Start < i[2]:
                                        Session_Start = input(
                                            "This appointment is already booked, Please Enter an other time for start of session : ")
                            Session_End = input("Session ends at : ")

                            New_Appointment = list()
                            New_Appointment.append(patient_id)
                            New_Appointment.append(Session_Start)
                            New_Appointment.append(Session_End)
                            Doctors_DataBase[Doctor_ID].append(New_Appointment)
                            print("/----------------------Appointment booked successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Appointment Management --> Cancel an appointment
                        try:  # To avoid non integer input

                            appointment_id = int(input("Enter appointment ID : "))
                            while appointment_id not in Appointments_DataBase:
                                appointment_id = int(input("Incorrect ID, Enter patient ID : "))
                            try:
                                del_flow = DeleteAppointmentByIdFlow(appointment_id).remove_appointment()
                                print("/----------------------appointment canceled successfully----------------------/")
                            except:
                                print("No Appointment for this patient")
                        except:  # To avoid no return function
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "E":  # Back
                        break

                    else:
                        print("please enter a correct choice")

                elif AdminOptions == "E":  # Back
                    break

                else:
                    print("Please enter a correct option")

            elif Password != "1234":
                if tries < 2:
                    Password = input("Password incorrect, please try again : ")
                    tries += 1
                else:
                    print("Incorrect password, no more tries")
                    tries_flag = "Close the program"
                    break

            Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Patients_DataBase)
            Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)


    elif Admin_user_mode == "2":  # Patient mode
        print(
            "****************************************\n|         Welcome to Patient mode         |\n****************************************")
        while True:
            print("\n-----------------------------------------")
            print("|To view hospital's available doctors Enter 1 |")
            print("|To view hospital's doctors Enter 2     |")
            print("|To view patients' residents Enter 3    |")
            print("|To view patient's details Enter 4      |")
            print("|To view doctor's appointments Enter 5  |")
            print("|To be Back Enter E                     |")
            print("-----------------------------------------")
            UserOptions = input("Enter your choice : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1":  # Patient mode --> view available doctors
                print("Hospital's available doctors :")
                flow = AvailableDoctorsListFlow()
                res = flow.get_available_doctors()

            elif UserOptions == "2":  # Patient mode --> view hospital's Doctors
                print("Hospital's doctors :")
                flow = DoctorsListFlow()
                res = flow.get_all_doctors()

            elif UserOptions == "3":  # Patient mode --> view patients waiting list
                print("Hospital's patients waiting list :")
                flow = WaitingListFlow()
                res = flow.get_waiting_list()

            elif UserOptions == "4":  # Patient mode --> view patient's details
                try:  # To avoid non integer input
                    patient_id = int(input("Enter patient's ID : "))
                    while patient_id not in Patients_DataBase:
                        patient_id = int(input("Incorrect Id, Please enter patient ID : "))
                    flow = GetPatientByIdFlow(patient_id)
                    result = flow.get_patient_by_id()
                    print("\npatient name        : ", result.patient_full_name)
                    print("patient Doctor         : ", result.doctor_full_name)
                    print("patient Phone      : ", result.patient_phone)
                    print("patient Message     : ", result.patient_message)
                    print("patient is in " + result.patient_waiting_status + " Status")
                except:
                    print("Patient ID should be an integer number")

            elif UserOptions == "5":  # Patient mode --> view doctor's appointments
                try:  # To avoid non integer input
                    Doctor_ID = int(input("Enter doctor's ID : "))
                    while Doctor_ID not in Doctors_DataBase:
                        Doctor_ID = int(input("Incorrect Id, Please enter doctor ID : "))
                    print(Doctors_DataBase[Doctor_ID][0][1] + " has appointments :")
                    for i in Doctors_DataBase[Doctor_ID]:
                        if type(i[0]) == str:
                            continue
                        else:
                            print("	from : " + i[1] + "    to : " + i[2])
                except:
                    print("Doctor ID should be an integer number")

            elif UserOptions == "E":  # Back
                break

            else:
                print("Please Enter a correct choice")

    elif Admin_user_mode == "1":  # Doctor mode
        print(
            "****************************************\n|         Welcome to Doctor mode         |\n****************************************")
        while True:
            print("\n-----------------------------------------")
            print("|To view hospital's list of waiting patients sorted by arrival time Enter 1 |")
            print("|To be Back Enter E                     |")
            print("-----------------------------------------")
            UserOptions = input("Enter your choice : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1":  # Patient mode --> view available doctors
                print("Hospital's available doctors :")
                flow = AvailableDoctorsListFlow()
                res = flow.get_available_doctors()

            elif UserOptions == "2":  # Patient mode --> view hospital's Doctors
                print("Hospital's doctors :")
                flow = DoctorsListFlow()
                res = flow.get_all_doctors()

            elif UserOptions == "E":  # Back
                break

            else:
                print("Please Enter a correct choice")
    else:
        print("Please choice just 1 or 2")

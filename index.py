import json
from dataclasses import asdict
from dal.json_patient import JsonPatient
from dal.write_data import WriteData
from flows.delete_appointment_by_id import DeleteAppointmentByIdFlow
from flows.get_appointments import AppointmentsListFlow
from flows.get_available_doctors import AvailableDoctorsListFlow
from flows.get_doctors import DoctorsListFlow
from flows.get_patients import PatientsListFlow
from flows.get_waiting_list import WaitingListFlow
from model.config_model import Patient

Patient_New_List_Json_File_Path = 'local_json/PatientData.json'
Doctor_New_List_Json_File_Path = 'local_json/DoctorData.json'

patients_list_data = PatientsListFlow().get_all_patients()
doctors_list_data = DoctorsListFlow().get_all_doctors()
Appointments_DataBase = AppointmentsListFlow.get_all_appointments()

print("********************************************************************")
print("*                                                                  *")
print("*      Welcome to Hospital appointment system for doctors          *")
print("*                                                                  *")
print("********************************************************************")

tries = 0
tries_flag = ""
while tries_flag != "Close the program":

    print("-----------------------------------------")
    print("|Enter 1 for Patient mode			|\n|Enter 2 for Doctor mode 			|")
    print("-----------------------------------------")

    user_mode = input("Enter your mode : ")

    if user_mode == "1":  # Patient mode
        print(
            "*****************************************\n|         Welcome to Patient mode         |\n*****************************************")
        Password = input("Please enter your password : ")
        while True:
            if Password == "1234":
                print("\n-----------------------------------------")
                print("|To add new patient (Signup) Enter 1	  	|")
                print("|To view hospital's available doctors Enter 2 |")
                print("|To view all hospital's doctors Enter 3 |")
                print("|To book an appointment Enter 4         |")
                print("|To cancel an appointment Enter 5       |")
                print("|To view doctor’s waiting list Enter 6  |")
                print("|To be Back Enter E                     |")
                print("-----------------------------------------")
                PatientOptions = input("Enter your choice : ")
                PatientOptions = PatientOptions.upper()

                if PatientOptions == "1":  # Patient mode --> add new patient
                    try:  # To avoid non integer input
                        patient_id = int(input("Enter patient ID : "))
                        for patient in patients_list_data:
                            while patient_id in patient.patient_id:  # if Admin entered used ID
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
                if PatientOptions == "2":  # Patient mode --> available doctors
                    print("Hospital's available doctors :")
                    flow = AvailableDoctorsListFlow()
                    res = flow.get_available_doctors()
                    result_as_list_of_dict = [asdict(x) for x in res]
                    print(result_as_list_of_dict)

                elif PatientOptions == "3":  # Patient mode --> view all hospital's doctors
                    print("Hospital's doctors :")
                    flow = DoctorsListFlow()
                    res = flow.get_all_doctors()
                    print(json.dumps(res))

                elif PatientOptions == "4":  # Patient mode --> book an appointment
                    print("book")

                elif PatientOptions == "5":  # Patient mode --> cancel an appointment
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

                elif PatientOptions == "6":  # Patient mode --> view doctor’s waiting list
                    print("Hospital's doctor’s waiting list :")
                    flow = WaitingListFlow()
                    res = flow.get_waiting_list()
                    result_as_list_of_dict = [asdict(x) for x in res]
                    print(json.dumps(result_as_list_of_dict))

                elif PatientOptions == "E":  # Back
                    break

                else:
                    print("Please Enter a correct choice")

            elif Password != "1234":
                if tries < 2:
                    Password = input("Password incorrect, please try again : ")
                    tries += 1
                else:
                    print("Incorrect password, no more tries")
                    tries_flag = "Close the program"
                    break

    elif user_mode == "2":  # Doctor mode
        print(
            "****************************************\n|         Welcome to Doctor mode         |\n****************************************")
        while True:
            if Password == "4321":
                print("\n-----------------------------------------")

                print("|To view hospital's list of waiting patients sorted by arrival time Enter 1 |")
                print("|To be Back Enter E                     |")
                print("-----------------------------------------")
                DoctorOptions = input("Enter your choice : ")
                DoctorOptions = DoctorOptions.upper()

            elif Password != "4321":
                if tries < 2:
                    Password = input("Password incorrect, please try again : ")
                    tries += 1
                else:
                    print("Incorrect password, no more tries")
                    tries_flag = "Close the program"
                    break

    else:
        print("Please choice just 1 or 2")

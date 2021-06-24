import json
from dataclasses import asdict

import win32api

from dal.doctor_repository import DoctorRepository
from dal.write_data import WriteData
from flows.add_appointment import AddAppointmentFlow
from flows.add_patient import AddPatientFlow
from flows.delete_appointment_by_id import DeleteAppointmentByIdFlow
from flows.get_appointments import AppointmentsListFlow
from flows.get_doctors import DoctorsListFlow
from flows.get_patients import PatientsListFlow
from model.config_model import Patient, Appointment, Doctor
from random import randint

Patient_New_List_Json_File_Path = 'local_json/PatientData.json'
Doctor_New_List_Json_File_Path = 'local_json/DoctorData.json'

random_num = randint(104, 999)


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
                        print(DoctorsListFlow.get_all_doctors())
                        DoctorName = input("Enter name of doctor from list: : ")
                        patient_phone = input("Enter patient age                       : ")
                        patient_message = input("Enter patient gender                    : ")
                        patient_arrival_time = input("Enter arrival time                  : ")
                        res_patient = Patient(patient_id, Name, DoctorName, patient_phone, patient_message, patient_arrival_time)
                        AddPatientFlow(res_patient).add_patient()
                        print("----------------------Patient added successfully----------------------")
                    except:
                        print("Patient ID should be an integer number")
                if PatientOptions == "2":  # Patient mode --> available doctors
                    print("Hospital's available doctors :")
                    flow = DoctorsListFlow()
                    res = flow.get_available_doctors()
                    result_as_list_of_dict = [asdict(x) for x in res]
                    print(result_as_list_of_dict)

                elif PatientOptions == "3":  # Patient mode --> view all hospital's doctors
                    print("Hospital's doctors :")
                    flow = DoctorsListFlow()
                    res = flow.get_all_doctors()
                    print(json.dumps(res))

                elif PatientOptions == "4":  # Patient mode --> book an appointment
                    # Appointment
                    appointment_id = random_num
                    appointment_start_time = input("Enter arrival time                  : ")
                    appointment_end_time = input("Enter arrival time                  : ")
                    appointment_type = input("Enter arrival time                  : ")
                    # Patient
                    appointment_patient_id = patient_id
                    print(DoctorsListFlow.get_all_doctors())
                    doctor_id = input("Enter doctor id from list ")

                    # Parsed Doctor Object
                    appointment_doctor_info = DoctorsListFlow().get_doctor_by_id(doctor_id)
                    # Parsed Patient Object
                    appointment_patient_info = PatientsListFlow().get_patient_by_id(appointment_patient_id)

                    # Parsed Appointment Object
                    appointment = Appointment(appointment_id, appointment_start_time, appointment_end_time,
                                              appointment_type,
                                              doctor_id, appointment_patient_id, appointment_patient_info,
                                              appointment_doctor_info)

                    doctor_waiting_patients_id = appointment_doctor_info.waiting_patients_id
                    # flow
                    appointment_flow = AddAppointmentFlow()

                    doctor_available_time_start = appointment_doctor_info.doctor_available_start_time
                    doctor_available_time_end = appointment_doctor_info.doctor_available_end_time
                    if doctor_available_time_start <= appointment_start_time < doctor_available_time_end:
                        appointment_doctor_info.doctor_available_status = False

                    if appointment_doctor_info.doctor_available_status:  # Waiting list condition
                        appointment_flow.get_notification()
                        appointment_result = appointment_flow.add_appointment(appointment)
                        print("your appointment detail: " + f"{appointment_result}")
                    else:
                        doctor_waiting_patients_id.append(appointment_patient_info.patient_id)
                        win32api.MessageBox(0, 'Hello, we want to inform you that the doctor is Un-Available',
                                            'Notification!!')

                    print('You added to wait list')



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
                    print(DoctorsListFlow.get_all_doctors())
                    doctor_id = input("Enter doctor id from list ")
                    print("Hospital's doctor’s waiting list :")
                    doctor_flow = DoctorsListFlow()
                    result = doctor_flow.get_waiting_patients_by_doctor_id(doctor_id)
                    parsed_result = doctor_flow.parse_patients(result)
                    result_as_list_of_dict = [asdict(x) for x in parsed_result]
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
                print("|To add new doctor (Signup) Enter 1	  	|")
                print("|To view the list of waiting patients sorted by arrival time at the hospital doctor Enter 2 |")
                print("|To be Back Enter E                     |")
                print("-----------------------------------------")
                DoctorOptions = input("Enter your choice : ")
                DoctorOptions = DoctorOptions.upper()
                if DoctorOptions == "1":  # Doctor mode --> List of waiting patients sorted by arrival time
                    try:  # To avoid non integer input
                        doctor_id = int(input("Enter Doctor ID : "))
                        for doctor in doctors_list_data:
                            while doctor_id in doctor.doctor_id:  # if Doctor entered used ID
                                doctor_id = int(input("This ID is unavailable, please try another ID : "))
                        doctor_name = input("Enter doctor name                      : ")
                        doctor_phone = input("Enter doctor age                       : ")
                        doctor_available_status = input("Enter doctor availability(True = available, False = Not available  : ")
                        doctor_available_start_time = input("Doctors working hours should be between 01:00PM to 10:00PM, Please enter a time between working hours : ")
                        doctor_end_time = input("Session ends at : ")
                        doctor_specialty = input(" Please enter Doctor Department  : ")
                        print(" Please enter id of patients that waiting for you (if exist) with space between each one : ")
                        Doctor_waiting_patients_id = [int(x) for x in input().split()]
                        doctor_obj = Doctor(doctor_id, doctor_name, doctor_phone, doctor_available_status,
                                            doctor_available_start_time, doctor_end_time,
                                            doctor_specialty, Doctor_waiting_patients_id)
                        DoctorRepository().add_doctor(doctor_obj)
                        print("----------------------Doctor added successfully----------------------")
                    except:
                        print("Doctor ID should be an integer number")

                elif DoctorOptions == "2":
                    doctor_flow = DoctorsListFlow()
                    result = doctor_flow.get_patients_sorted_by_arrival_time(doctor_id)
                    result_as_list_of_dict = [asdict(x) for x in result]
                    print(json.dumps(result_as_list_of_dict))

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

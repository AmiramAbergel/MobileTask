from typing import List
from model.config_model import Patient, Doctor, Appointment


class InMemoryDatabase:
    def __init__(self):
        # our data base
        self.doctors_list = []
        self.patients_list = []
        self.appointments_list = []
        self.waiting_list = []

    def add_appointment(self, appointment: Appointment):
        self.appointments_list.append(appointment)

    """
    Cancel an appointment using the appointment id parameter
    • param appointment_id: Appointment uniq identity document
    • return: confirmation of cancellation
    """
    def remove_appointment(self, appointment_id: int) -> str:
        patients_appointments_list = self.appointments_list
        appointment = list(filter(lambda m: m.appointment_index == appointment_id, patients_appointments_list))
        self.appointments_list.remove(appointment[0])
        return "Canceled!", 200

    """
    Getting appointment bookings based on appointment Index parameter
    • param: appointment_id: appointment uniq index
    • return: appointment as Appointment class
    """
    def get_appointment_by_index(self, appointment_id: int) -> Appointment:
        appointments_list = self.appointments_list
        appointment = list(filter(lambda m: m.appointment_index == appointment_id, appointments_list))
        return appointment[0]


    """
    Getting appointment bookings based on doctor ID parameter
    • param: doctor_id: Doctor uniq identity document
    • return: appointment as Appointment class
    """
    def get_appointments_by_doc_id(self, doctor_id: int) -> List[Appointment]:
        appointments_list = self.appointments_list
        appointments = list(filter(lambda m: m.appointment_doctor_id == doctor_id, appointments_list))
        return appointments

    """
    Getting appointment bookings based on patient ID parameter
    • param: doctor_id: Doctor uniq identity document
    • return: appointment as Appointment class
    """
    def get_appointments_by_patient_id(self, patient_id: int) -> List[Appointment]:
        appointments_list = self.appointments_list
        appointments = list(filter(lambda m: m.appointment_patient_info.patient_id == patient_id, appointments_list))
        return appointments

    def add_doctor(self, doctor: Doctor):
        self.doctors_list.append(doctor)

    """
    Getting doctor information based on doctor ID parameter
    • param: doctor_id: Doctor uniq identity document
    • return: related doctor as a Doctor class
    """
    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        doctors_list = self.doctors_list
        doctor = list(filter(lambda m: m.doctor_id == doctor_id, doctors_list))
        result = doctor[0]
        return result

    """
    Getting a list of all doctors in our database
    • return: list of all doctors list of Doctor class
    """
    def get_all_doctors(self) -> List[Doctor]:
        doctors = self.doctors_list
        return doctors

    """
    Add new patient
    """
    def add_patient(self, patient: Patient):
        self.patients_list.append(patient)

    """
    Getting patient information based on patient ID parameter
    • param: patient_id: Patient uniq identity document
    • return: related patient as a Patient class
    """
    def get_patient_by_id(self, patient_id: int) -> Patient:
        patients_list = self.patients_list
        patient = list(filter(lambda m: m.patient_id == patient_id, patients_list))
        result = patient[0]
        return result

    """
    Remove an patient using the patient id parameter
    • param patient_id: patient uniq identity document
    • return: confirmation of cancellation
    """
    def remove_patient_by_id(self, patient_id: int) -> str:
        patients_list = self.patients_list
        patient = list(filter(lambda m: m.patient_id == patient_id, patients_list))
        self.patients_list.remove(patient[0])
        return "Removed!", 200

    def add_patient_to_waiting_list(self, patient: Patient):
        self.waiting_list.append(patient)


In_Memory_Database = InMemoryDatabase()

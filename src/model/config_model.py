from dataclasses import dataclass, field
from faker import Faker


def fake_dates():  # just try... need to be fixed!!
    fake = Faker()
    return fake.date_time_between(start_date='-30y', end_date='now')


@dataclass
class Doctor:
    doctor_id: int
    doctor_full_name: str
    doctor_phone: str
    doctor_available_status: bool
    doctor_specialty: str


@dataclass
class Patient:
    patient_id: int
    patient_full_name: str
    patient_phone: str
    patient_message: str
    patient_waiting_status: str = None
    patient_arrival_time:str = f"{fake_dates()}"  # with func!!!


@dataclass
class Appointment:
    appointment_id: int
    appointment_date: str
    appointment_type: str
    appointment_doctor_id: int
    appointment_patient_info: Patient
    appointment_doctor_info: Doctor
    appointment_time_slot: int = 5

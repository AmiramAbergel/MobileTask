from datetime import datetime, timedelta
from dataclasses import dataclass
import random
NOW = datetime.now()
Delta = timedelta(days=4)
Delta2 = timedelta(days=7)
t = NOW + Delta
t2 = NOW + Delta + Delta2
time = [NOW, t, t2]

ANS = random.choice(time)


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
    patient_arrival_time: str = f"{ANS}"  # with func!!!


@dataclass
class Appointment:
    appointment_id: int
    appointment_date: str
    appointment_type: str
    appointment_doctor_id: int
    appointment_patient_info: Patient
    appointment_doctor_info: Doctor
    appointment_time_slot: int = 5


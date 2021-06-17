from dataclasses import dataclass


@dataclass
class Doctor:
    doctor_id: int
    doctor_full_name: str
    doctor_phone: str
    doctor_available_status: str


class Patient:
    patient_id: int
    patient_full_name: str
    patient_phone: str
    patient_message: str
    patient_arrival_time: str
    patient_waiting_status: str


class Appointment:
    appointment_date: str
    time_slot: int = 5
    Type: str
    appointment_patient_id: int
    appointment_doctor_id: int
    appointment_doctor_name: str


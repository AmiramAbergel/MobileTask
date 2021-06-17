from dataclasses import dataclass


@dataclass
class Doctor:
    doctor_full_name: str
    doctor_id: int
    doctor_phone: str


class Patient:
    patient_full_name: str
    patient_phone: str
    patient_message: str
    patient_arrival_time: str
    patient_waiting_status: str

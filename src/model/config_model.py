from dataclasses import dataclass, field


@dataclass
class Doctor:
    doctor_id: int
    doctor_full_name: str
    doctor_phone: str
    doctor_available_status: bool
    doctor_available_start_time: str
    doctor_available_end_time: str
    doctor_specialty: str
    waiting_patients_id: list


@dataclass
class Patient:
    patient_id: int
    patient_full_name: str
    doctor_full_name: str
    patient_phone: str
    patient_message: str
    patient_arrival_time: str


@dataclass
class Appointment:
    appointment_id: int
    appointment_start_time: str
    appointment_end_time: str
    appointment_type: str
    appointment_doctor_id: int
    appointment_patient_id: int
    appointment_patient_info: Patient
    appointment_doctor_info: Doctor



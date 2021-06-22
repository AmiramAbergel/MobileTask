from dataclasses import dataclass


@dataclass
class Doctor:
    doctor_id: int
    doctor_full_name: str
    doctor_phone: str
    doctor_available_status: bool
    doctor_available_times: list
    doctor_specialty: str
    doctor_waiting_list: list


@dataclass
class Patient:
    patient_id: int
    patient_full_name: str
    doctor_full_name: str
    patient_phone: str
    patient_message: str
    patient_waiting_status: str = None


@dataclass
class Appointment:
    appointment_index: int
    appointment_start_time: str
    appointment_end_time: str
    appointment_type: str
    appointment_doctor_id: int
    appointment_patient_info: Patient
    appointment_doctor_info: Doctor
    appointment_time_slot: int = 5


@dataclass
class WaitingList:
    doctor_id: int
    patient_id: int
    patient_arrival_time: str

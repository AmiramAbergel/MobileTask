from dal.inmemory_database import In_Memory_Database


class DoctorRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_waiting_patients(self) -> str:
        return self.db.get_waiting_patients()

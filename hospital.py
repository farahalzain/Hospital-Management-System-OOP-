import csv
from datetime import datetime

class Person:
    def __init__(self, person_id, name, age, gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return f"ID: {self.person_id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}"

class Patient(Person):
    def __init__(self, person_id, name, age, gender, disease):
        super().__init__(person_id, name, age, gender)
        self.disease = disease

    def display_info(self):
        return super().display_info() + f"\nDisease: {self.disease}"

class Doctor(Person):
    def __init__(self, person_id, name, age, gender, specialty):
        super().__init__(person_id, name, age, gender)
        self.specialty = specialty

    def display_info(self):
        return super().display_info() + f"\nSpecialty: {self.specialty}"

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display_info(self):
        return (f"Appointment ID: {self.appointment_id}\nDate: {self.date}\n"
                f"Patient: {self.patient.name}\nDoctor: {self.doctor.name}")

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    # --- CRUD Operations ---
    def add_patient(self, patient):
        if any(p.person_id == patient.person_id for p in self.patients):
            raise ValueError("Patient ID already exists!")
        self.patients.append(patient)

    def add_doctor(self, doctor):
        if any(d.person_id == doctor.person_id for d in self.doctors):
            raise ValueError("Doctor ID already exists!")
        self.doctors.append(doctor)

    def create_appointment(self, appointment):
        # Conflict check: same patient or doctor at same date
        for appt in self.appointments:
            if appt.date == appointment.date:
                if appt.patient.person_id == appointment.patient.person_id:
                    raise ValueError("Patient already has an appointment at this date!")
                if appt.doctor.person_id == appointment.doctor.person_id:
                    raise ValueError("Doctor already has an appointment at this date!")
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment_id):
        self.appointments = [appt for appt in self.appointments if appt.appointment_id != appointment_id]

    # --- List & Search ---
    def list_patients(self):
        return [p.display_info() for p in self.patients]

    def list_doctors(self):
        return [d.display_info() for d in self.doctors]

    def list_appointments(self):
        return [a.display_info() for a in self.appointments]

    def search_patient_by_name(self, name):
        return [p.display_info() for p in self.patients if name.lower() in p.name.lower()]

    def search_doctor_by_name(self, name):
        return [d.display_info() for d in self.doctors if name.lower() in d.name.lower()]

    # --- Statistics ---
    def statistics(self):
        stats = {}
        stats['Total Patients'] = len(self.patients)
        stats['Total Doctors'] = len(self.doctors)
        stats['Total Appointments'] = len(self.appointments)
        stats['Average Patient Age'] = round(sum(p.age for p in self.patients)/len(self.patients), 1) if self.patients else 0
        stats['Average Doctor Age'] = round(sum(d.age for d in self.doctors)/len(self.doctors), 1) if self.doctors else 0
        return stats

    # --- Export CSV ---
    def export_patients_to_csv(self, filename="patients.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID","Name","Age","Gender","Disease"])
            for patient in self.patients:
                writer.writerow([patient.person_id, patient.name, patient.age, patient.gender, patient.disease])

    def export_doctors_to_csv(self, filename="doctors.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID","Name","Age","Gender","Specialty"])
            for doctor in self.doctors:
                writer.writerow([doctor.person_id, doctor.name, doctor.age, doctor.gender, doctor.specialty])

    def export_appointments_to_csv(self, filename="appointments.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Appointment ID","Date","Patient ID","Patient Name","Doctor ID","Doctor Name"])
            for appt in self.appointments:
                writer.writerow([
                    appt.appointment_id, appt.date,
                    appt.patient.person_id, appt.patient.name,
                    appt.doctor.person_id, appt.doctor.name
                ])

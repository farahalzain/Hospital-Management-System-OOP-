import csv

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

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def create_appointment(self, appointment):
        self.appointments.append(appointment)

    def cancel_appointment(self, appointment_id):
        self.appointments = [appt for appt in self.appointments if appt.appointment_id != appointment_id]

    def list_patients(self):
        return [p.display_info() for p in self.patients]

    def list_doctors(self):
        return [d.display_info() for d in self.doctors]

    def list_appointments(self):
        return [a.display_info() for a in self.appointments]

    def export_patients_to_csv(self, filename="patients.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Gender", "Disease"])
            for patient in self.patients:
                writer.writerow([patient.person_id, patient.name, patient.age, patient.gender, patient.disease])

    def export_doctors_to_csv(self, filename="doctors.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Gender", "Specialty"])
            for doctor in self.doctors:
                writer.writerow([doctor.person_id, doctor.name, doctor.age, doctor.gender, doctor.specialty])

    def export_appointments_to_csv(self, filename="appointments.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Appointment ID", "Date", "Patient ID", "Patient Name", "Doctor ID", "Doctor Name"])
            for appointment in self.appointments:
                writer.writerow([
                    appointment.appointment_id, appointment.date,
                    appointment.patient.person_id, appointment.patient.name,
                    appointment.doctor.person_id, appointment.doctor.name
                ])


print("Hospital file is done well")

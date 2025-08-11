import os
from datetime import datetime
from hospital import Patient, Doctor, Appointment, HospitalManagementSystem

system = HospitalManagementSystem()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def input_gender():
    while True:
        gender = input("Enter gender (M/F): ").strip().upper()
        if gender in ("M", "F"):
            return gender
        print("Gender must be 'M' or 'F'.")

def input_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Date must be in format YYYY-MM-DD.")

def main_menu():
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Create Appointment")
        print("4. Cancel Appointment")
        print("5. List Patients")
        print("6. List Doctors")
        print("7. List Appointments")
        print("8. Export Patients to CSV")
        print("9. Export Doctors to CSV")
        print("10. Export Appointments to CSV")
        print("0. Exit")

        choice = input("Enter your choice (0 to 10): ").strip()
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            add_doctor()
        elif choice == "3":
            create_appointment()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            list_patients()
        elif choice == "6":
            list_doctors()
        elif choice == "7":
            list_appointments()
        elif choice == "8":
            system.export_patients_to_csv()
            print("Patients exported to patients.csv")
        elif choice == "9":
            system.export_doctors_to_csv()
            print("Doctors exported to doctors.csv")
        elif choice == "10":
            system.export_appointments_to_csv()
            print("Appointments exported to appointments.csv")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose numbers from 0 to 10")

def add_doctor():
    print("\nAdd Doctor")
    d_ID = input_int("Enter Doctor's ID: ")
    name = input("Enter Doctor's name: ").strip().capitalize()
    age = input_int("Enter Doctor's age: ")
    gender = input_gender()
    specialization = input("Enter Doctor's specialization: ").strip().capitalize()
    
    new_doctor = Doctor(d_ID, name, age, gender, specialization)
    system.add_doctor(new_doctor)
    print("Doctor added successfully!")

def add_patient():
    print("\nAdd Patient")
    p_ID = input_int("Enter Patient's ID: ")
    name = input("Enter Patient's name: ").strip().capitalize()
    age = input_int("Enter Patient's age: ")
    gender = input_gender()
    disease = input("Enter Patient's disease: ").strip().capitalize()
    
    new_patient = Patient(p_ID, name, age, gender, disease)
    system.add_patient(new_patient)
    print("Patient added successfully!")

def list_patients():
    print("\n--- Patients List ---")
    if not system.patients:
        print("No patients found.")
    for info in system.list_patients():
        print(info)
        print("**********")

def list_doctors():
    print("\n--- Doctors List ---")
    if not system.doctors:
        print("No doctors found.")
    for info in system.list_doctors():
        print(info)
        print("**********")

def list_appointments():
    print("\n--- Appointments List ---")
    if not system.appointments:
        print("No appointments found.")
    for info in system.list_appointments():
        print(info)
        print("**********")

def create_appointment():
    print("\nCreate Appointment")
    if not system.patients or not system.doctors:
        print("Please add at least one patient and one doctor first.")
        return
    
    appt_id = input_int("Enter Appointment ID: ")
    
    while True:
        patient_id = input_int("Enter Patient ID: ")
        patient = next((p for p in system.patients if p.person_id == patient_id), None)
        if patient:
            break
        print("No patient found with that ID.")
    
    while True:
        doctor_id = input_int("Enter Doctor ID: ")
        doctor = next((d for d in system.doctors if d.person_id == doctor_id), None)
        if doctor:
            break
        print("No doctor found with that ID.")
    
    date = input_date("Enter appointment date (YYYY-MM-DD): ")
    
    appointment = Appointment(appt_id, patient, doctor, date)
    system.create_appointment(appointment)
    print(f"Appointment created between {patient.name} and Dr. {doctor.name} on {date}.")

def cancel_appointment():
    print("\nCancel Appointment")
    appt_id = input_int("Enter Appointment ID: ")
    
    appointment = next((a for a in system.appointments if a.appointment_id == appt_id), None)
    if appointment:
        system.appointments.remove(appointment)
        print("Appointment canceled successfully.")
    else:
        print("No appointment found with that ID.")

if __name__ == "__main__":
    main_menu()

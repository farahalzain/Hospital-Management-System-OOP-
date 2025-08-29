from hospital import Patient, Doctor, Appointment, HospitalManagementSystem
from datetime import datetime

system = HospitalManagementSystem()

def input_int(prompt):
    while True:
        try: return int(input(prompt))
        except: print("Enter a valid number!")

def input_date(prompt):
    while True:
        try: return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except: print("Date must be YYYY-MM-DD!")

def input_gender():
    while True:
        g = input("Enter gender (M/F): ").strip().upper()
        if g in ("M","F"): return g
        print("Gender must be M or F")

def main_menu():
    while True:
        print("\n--- Hospital System ---")
        print("1. Add Patient  2. Add Doctor  3. Create Appointment  4. Cancel Appointment")
        print("5. List Patients  6. List Doctors  7. List Appointments")
        print("8. Search Patient  9. Search Doctor  10. Show Stats  0. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            pid = input_int("Patient ID: "); name = input("Name: "); age = input_int("Age: "); gender = input_gender(); disease = input("Disease: ")
            system.add_patient(Patient(pid,name,age,gender,disease))
            print("Patient added!")
        elif choice == "2":
            did = input_int("Doctor ID: "); name = input("Name: "); age = input_int("Age: "); gender = input_gender(); specialty = input("Specialty: ")
            system.add_doctor(Doctor(did,name,age,gender,specialty))
            print("Doctor added!")
        elif choice == "3":
            appt_id = input_int("Appointment ID: ")
            patient_id = input_int("Patient ID: ")
            doctor_id = input_int("Doctor ID: ")
            date = input_date("Date (YYYY-MM-DD): ")
            patient = next(p for p in system.patients if p.person_id == patient_id)
            doctor = next(d for d in system.doctors if d.person_id == doctor_id)
            try:
                system.create_appointment(Appointment(appt_id,patient,doctor,date))
                print("Appointment created!")
            except Exception as e:
                print("Error:", e)
        elif choice == "4":
            appt_id = input_int("Appointment ID: ")
            system.cancel_appointment(appt_id)
            print("Appointment canceled!")
        elif choice == "5": print("\n".join(system.list_patients()))
        elif choice == "6": print("\n".join(system.list_doctors()))
        elif choice == "7": print("\n".join(system.list_appointments()))
        elif choice == "8":
            name = input("Enter patient name: ")
            print("\n".join(system.search_patient_by_name(name)))
        elif choice == "9":
            name = input("Enter doctor name: ")
            print("\n".join(system.search_doctor_by_name(name)))
        elif choice == "10":
            stats = system.statistics()
            for k,v in stats.items(): print(f"{k}: {v}")
        elif choice == "0": break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main_menu()


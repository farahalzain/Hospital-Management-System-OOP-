# ***Hospital Management System***

**Hospital Management System** is a professional system for managing patients, doctors, and appointments. It supports both a CLI (Terminal) interface and an interactive Streamlit web interface.

---

## Project Files

| File                    | Description                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hospital.py`           | Core classes (`Person`, `Patient`, `Doctor`, `Appointment`) and `HospitalManagementSystem` with all main operations, statistics, and CSV export                |
| `hospital_cli.py`       | CLI interface for running the system in Terminal, including adding patients/doctors, creating/canceling appointments, viewing lists, searching, and statistics |
| `hospital_streamlit.py` | Interactive Streamlit interface with downloadable CSV and statistics, providing a user-friendly experience                                                     |

---

## Features

* Add patients and doctors with automatic ID validation
* Create and cancel appointments while preventing conflicts
* View all patients, doctors, and appointments
* Search patients or doctors by name
* System statistics: total patients, doctors, appointments, average age
* Export data to CSV (patients, doctors, appointments)
* Interactive web interface using Streamlit


---

## Example Workflow

1. Add a patient:

   * ID: 1
   * Name: Ahmad
   * Age: 30
   * Gender: Male
   * Disease: Flu

2. Add a doctor:

   * ID: 101
   * Name: Dr. Sara
   * Age: 45
   * Gender: Female
   * Specialty: Cardiology

3. Create an appointment:

   * Appointment ID: 1001
   * Patient: Ahmad
   * Doctor: Dr. Sara
   * Date: 2025-09-01

4. View all patients, doctors, and appointments, along with system statistics.

---

## Notes

* All data is stored in memory during runtime. Use CSV export for persistent storage.
* IDs are automatically validated to prevent duplicates.
* Streamlit interface enhances user experience with interactive charts, CSV downloads, and easy navigation.

---


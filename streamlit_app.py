import streamlit as st
import pandas as pd
from hospital import Patient, Doctor, Appointment, HospitalManagementSystem
from datetime import datetime

COMMON_DISEASES = ["Flu","Diabetes","Hypertension","Asthma","Covid-19","Allergy","Cancer","Heart Disease","Migraine","Fracture"]
MEDICAL_SPECIALTIES = ["Cardiology","Neurology","Dermatology","Pediatrics","Orthopedics","Psychiatry","Radiology","General Surgery","Internal Medicine","Ophthalmology"]

if 'system' not in st.session_state:
    st.session_state.system = HospitalManagementSystem()
system = st.session_state.system

st.set_page_config(page_title="Hospital Dashboard", layout="centered")
st.title("🏥 Hospital Management System")

menu = st.sidebar.selectbox("Menu", ["Add Patient","Add Doctor","Appointments","Search","Statistics","Export CSV"])

def to_csv(data, columns):
    df = pd.DataFrame(data, columns=columns)
    return df.to_csv(index=False).encode('utf-8')

if menu=="Add Patient":
    with st.form("patient_form"):
        pid = st.text_input("Patient ID"); name = st.text_input("Name")
        age = st.number_input("Age",0,120); gender = st.selectbox("Gender",["Male","Female"])
        disease = st.selectbox("Disease",COMMON_DISEASES); submitted = st.form_submit_button("Add Patient")
        if submitted: system.add_patient(Patient(pid,name,age,gender,disease)); st.success(f"{name} added!")

elif menu=="Add Doctor":
    with st.form("doctor_form"):
        did = st.text_input("Doctor ID"); name = st.text_input("Name")
        age = st.number_input("Age",25,100); gender = st.selectbox("Gender",["Male","Female"])
        specialty = st.selectbox("Specialty",MEDICAL_SPECIALTIES); submitted = st.form_submit_button("Add Doctor")
        if submitted: system.add_doctor(Doctor(did,name,age,gender,specialty)); st.success(f"{name} added!")

elif menu=="Appointments":
    st.subheader("Appointments")
    if system.appointments: st.dataframe([[a.appointment_id,a.patient.name,a.doctor.name,a.date] for a in system.appointments],columns=["ID","Patient","Doctor","Date"])
    else: st.info("No appointments yet.")

elif menu=="Search":
    st.subheader("Search")
    search_type = st.radio("Search for", ["Patient","Doctor"])
    name = st.text_input("Enter Name")
    if name:
        if search_type=="Patient": results = system.search_patient_by_name(name)
        else: results = system.search_doctor_by_name(name)
        if results: st.text("\n\n".join(results))
        else: st.warning("No results found.")

elif menu=="Statistics":
    st.subheader("System Statistics")
    stats = system.statistics()
    for k,v in stats.items(): st.metric(k,v)

elif menu=="Export CSV":
    st.subheader("Export Data")
    if system.patients:
        st.download_button("Patients CSV",to_csv([[p.person_id,p.name,p.age,p.gender,p.disease] for p in system.patients],["ID","Name","Age","Gender","Disease"]),"patients.csv")
    if system.doctors:
        st.download_button("Doctors CSV",to_csv([[d.person_id,d.name,d.age,d.gender,d.specialty] for d in system.doctors],["ID","Name","Age","Gender","Specialty"]),"doctors.csv")
    if system.appointments:
        st.download_button("Appointments CSV",to_csv([[a.appointment_id,a.patient.name,a.doctor.name,a.date] for a in system.appointments],["ID","Patient","Doctor","Date"]),"appointments.csv")

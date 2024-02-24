import streamlit as st
import mysql.connector

# Establish a connection to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="sql.freedb.tech",
            user="freedb_Mennah",
            password="?Fhu@EyzAe5BUPq",
            database="freedb_Rheumatology"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
        return None

# Custom CSS for styling boxes with colors
box_styles = """
    <style>
        .box {
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            background-color: #9370DB; /* Purple */
            margin-bottom: 20px;
        }
        .left-box {
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            background-color: #FFD700; /* Gold */
            margin-bottom: 20px;
        }
    </style>
"""

def main():
    st.title('Rheumatology Patient Checking Chart')

    # Inject custom CSS
    st.markdown(box_styles, unsafe_allow_html=True)

    # Create a sidebar navigation menu
    page = st.sidebar.selectbox("Navigation", ["New Patient", "Past Patient Reports"])

    if page == "New Patient":
        new_patient_page()
    elif page == "Past Patient Reports":
        past_patient_reports_page()

def new_patient_page():
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Patient Information Section
    st.markdown('<div class="box"><h4>Patient Information</h4></div>', unsafe_allow_html=True)
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0, max_value=150, value=0, step=1)
    gender = st.selectbox('Gender', ['Male', 'Female'])

    # Medical History Section
    st.markdown('<div class="box"><h4>Medical History</h4></div>', unsafe_allow_html=True)

    # Define common options
    common_diagnoses = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis', 'Other']
    common_medications = ['NSAIDs', 'Corticosteroids', 'DMARDs', 'Biologics', 'Pain Relievers', 'Immunosuppressants', 'Other']
    common_allergies = ['Pollen', 'Dust', 'Pet Dander', 'Mold', 'Food', 'Medications', 'Other']
    common_surgeries = ['Appendectomy', 'Tonsillectomy', 'Hernia Repair', 'Gallbladder Removal', 'Knee Surgery', 'Cataract Surgery', 'Other']
    common_rheumatologic_diagnoses = ['Rheumatoid Arthritis', 'Ankylosing Spondylitis', 'Systemic Lupus Erythematosus', 'Sjögren\'s Syndrome', 'Psoriatic Arthritis', 'Gout', 'Other']
    common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe', 'Other']
    common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis', 'Other']

    # Previous Diagnoses
    selected_diagnoses = st.multiselect('Common Previous Diagnoses', common_diagnoses)
    for diagnosis in selected_diagnoses:
        cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (diagnosis,))
    conn.commit()

    # Current Medications
    selected_medications = st.multiselect('Common Current Medications', common_medications)
    for medication in selected_medications:
        cursor.execute("INSERT INTO Medication (name) VALUES (%s)", (medication,))
    conn.commit()

    # Allergies Section
    selected_allergies = st.multiselect('Common Allergies', common_allergies)
    for allergy in selected_allergies:
        cursor.execute("INSERT INTO Allergy (name) VALUES (%s)", (allergy,))
    conn.commit()

    # Surgeries Section
    selected_surgeries = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    for surgery in selected_surgeries:
        cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (surgery,))
    conn.commit()

    # Rheumatologic History and Family History Section
    st.markdown('<div class="box"><h4>Rheumatologic and Family History</h4></div>', unsafe_allow_html=True)

    # Previous Rheumatologic Diagnoses
    selected_rheumatologic_diagnoses = st.multiselect('Common Previous Rheumatologic Diagnoses', common_rheumatologic_diagnoses)
    for rheumatologic_diagnosis in selected_rheumatologic_diagnoses:
        cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (rheumatologic_diagnosis,))
    conn.commit()

    # Common Disease Activities
    selected_activity = st.multiselect('Select Disease Activity', common_activities)
    for activity in selected_activity:
        cursor.execute("INSERT INTO Activity (name) VALUES (%s)", (activity,))
    conn.commit()

    # Family History
    selected_family_history = st.multiselect('Common Family History of Rheumatic Diseases', common_family_history)
    for family_history in selected_family_history:
        cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s)", (family_history,))
    conn.commit()

    # Review of Systems Section
    st.markdown('<div class="box"><h4>Review of Systems</h4></div>', unsafe_allow_html=True)

    joint_pain = st.checkbox('Joint Pain')
    joint_stiffness = st.checkbox('Joint Stiffness')
    swelling = st.checkbox('Swelling')
    fatigue = st.checkbox('Fatigue')
    fever = st.checkbox('Fever')
    skin_rashes = st.checkbox('Skin Rashes or Lesions')
    eye_problems = st.checkbox('Eye Problems')

    # Physical Examination Findings Section
    st.markdown('<div class="box"><h4>Physical Examination Findings</h4></div>', unsafe_allow_html=True)

    # Expander for Physical Examination Findings
    joint_swelling = st.checkbox('Joint Swelling')
    joint_tenderness = st.checkbox('Joint Tenderness')
    joint_warmth = st.checkbox('Joint Warmth')
    joint_redness = st.checkbox('Joint Redness')
    limited_range_of_motion = st.checkbox('Limited Range of Motion')
    muscle_weakness = st.checkbox('Muscle Weakness')
    # 'Other' checkbox and text input for other findings
    other_finding = st.checkbox('Other')
    if other_finding:
        other_finding_text = st.text_input('Specify Other Finding')

    # Diagnostic Tests Section
    st.markdown('<div class="box"><h4>Diagnostic Tests</h4></div>', unsafe_allow_html=True)
    diagnostic_tests = st.text_area('Enter Diagnostic Tests')

    # Notes and Comments Section
    st.markdown('<div class="box"><h4>Notes and Comments</h4></div>', unsafe_allow_html=True)
    notes_and_comments = st.text_area('Enter Notes and Comments')
    # Submit Button
    if st.button('Submit'):
        try:
            # You can add code here to save the entered information or perform further actions
            st.success('Patient information submitted successfully.')
            # Display patient information in a box on the left side
            st.sidebar.markdown('<div class="left-box"><h4>Patient Information</h4></div>', unsafe_allow_html=True)
            st.sidebar.write(f"Name: {name}")
            st.sidebar.write(f"Age: {age}")
            st.sidebar.write(f"Gender: {gender}")
        except mysql.connector.Error as e:
            st.error(f"Error inserting data into MySQL database: {e}")

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()


def past_patient_reports_page():
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Text input for searching patient by ID
    patient_id_input = st.text_input("Enter Patient ID:", key="patient_id_input")
    patient_name_input = st.text_input("Enter Patient Name:", key="patient_name_input")

    # Execute SQL query to fetch past patient records if patient ID or name is provided
    if patient_id_input or patient_name_input:
        try:
            if patient_id_input:
                search_type = "ID"
                search_value = int(patient_id_input)
                condition = "Patient.patient_id = %s"
            else:
                search_type = "Name"
                search_value = patient_name_input.strip()
                condition = "Patient.name LIKE %s"

            cursor.execute(f"""
                SELECT 
                    Patient.patient_id,
                    Patient.name,
                    Patient.age,
                    Patient.gender,
                    Diagnosis.name AS diagnosis,
                    Medication.name AS medication,
                    Allergy.name AS allergy,
                    Surgery.name AS surgery,
                    Activity.name AS activity,
                    FamilyHistory.name AS family_history,
                    ReviewOfSystems.joint_pain,
                    ReviewOfSystems.joint_stiffness,
                    ReviewOfSystems.swelling,
                    ReviewOfSystems.fatigue,
                    ReviewOfSystems.fever,
                    ReviewOfSystems.skin_rashes,
                    ReviewOfSystems.eye_problems,
                    PhysicalExamination.joint_swelling,
                    PhysicalExamination.joint_tenderness,
                    PhysicalExamination.joint_warmth,
                    PhysicalExamination.joint_redness,
                    PhysicalExamination.limited_range_of_motion,
                    PhysicalExamination.muscle_weakness,
                    PhysicalExamination.other_finding,
                    DiagnosticTests.test_results,
                    NotesAndComments.notes_and_comments
                FROM 
                    Patient
                LEFT JOIN 
                    PatientMedicalHistory ON Patient.patient_id = PatientMedicalHistory.patient_id
                LEFT JOIN 
                    Diagnosis ON PatientMedicalHistory.diagnosis_id = Diagnosis.diagnosis_id
                LEFT JOIN 
                    PatientCurrentMedication ON Patient.patient_id = PatientCurrentMedication.patient_id
                LEFT JOIN 
                    Medication ON PatientCurrentMedication.medication_id = Medication.medication_id
                LEFT JOIN 
                    PatientAllergy ON Patient.patient_id = PatientAllergy.patient_id
                LEFT JOIN 
                    Allergy ON PatientAllergy.allergy_id = Allergy.allergy_id
                LEFT JOIN 
                    PatientSurgery ON Patient.patient_id = PatientSurgery.patient_id
                LEFT JOIN 
                    Surgery ON PatientSurgery.surgery_id = Surgery.surgery_id
                LEFT JOIN 
                    PatientActivity ON Patient.patient_id = PatientActivity.patient_id
                LEFT JOIN 
                    Activity ON PatientActivity.activity_id = Activity.activity_id
                LEFT JOIN 
                    PatientFamilyHistory ON Patient.patient_id = PatientFamilyHistory.patient_id
                LEFT JOIN 
                    FamilyHistory ON PatientFamilyHistory.history_id = FamilyHistory.history_id
                LEFT JOIN 
                    ReviewOfSystems ON Patient.patient_id = ReviewOfSystems.patient_id
                LEFT JOIN 
                    PhysicalExamination ON Patient.patient_id = PhysicalExamination.patient_id
                LEFT JOIN 
                    DiagnosticTests ON Patient.patient_id = DiagnosticTests.patient_id
                LEFT JOIN 
                    NotesAndComments ON Patient.patient_id = NotesAndComments.patient_id
                WHERE 
                    {condition}
            """, (search_value,))
            records = cursor.fetchall()

            # Display the records if found
            if records:
                st.write(f"Patient Records for {search_type}: {search_value}")
                for record in records:
                    # Filter out None values
                    filtered_record = {key: record[i] for i, key in enumerate(cursor.column_names) if record[i] is not None}
                    # Format the record as a string with HTML line breaks
                    formatted_output = "<br>".join([f"{key}: {value}" for key, value in filtered_record.items()])
                    # Display the formatted output within the colored box
                    st.markdown(f'<div class="box">{formatted_output}</div>', unsafe_allow_html=True)
                     
                

            else:
                st.write(f"No patient records found for {search_type}: {search_value}")
        except ValueError as ve:
            st.error(f"Error: {ve}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.info("Enter a patient ID or name to search.")

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

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

    # Previous Diagnoses
    common_diagnoses = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_diagnoses = st.multiselect('Common Previous Diagnoses', common_diagnoses)
    if 'Other' in selected_diagnoses:
        other_diagnosis = st.text_input('Other Diagnosis')
        cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (other_diagnosis,))
        conn.commit()

    # Current Medications
    common_medications = ['NSAIDs', 'Corticosteroids', 'DMARDs', 'Biologics', 'Pain Relievers', 'Immunosuppressants','Other']
    selected_medications = st.multiselect('Common Current Medications', common_medications)
    if 'Other' in selected_medications:
        other_medication = st.text_input('Other Medication')
        cursor.execute("INSERT INTO Medication (name) VALUES (%s)", (other_medication,))
        conn.commit()

    # Allergies Section
    common_allergies = ['Pollen', 'Dust', 'Pet Dander', 'Mold', 'Food', 'Medications','Other']
    selected_allergies = st.multiselect('Common Allergies', common_allergies)
    if 'Other' in selected_allergies:
        other_allergy = st.text_input('Other Allergy')
        cursor.execute("INSERT INTO Allergy (name) VALUES (%s)", (other_allergy,))
        conn.commit()

    # Surgeries Section
    common_surgeries = ['Appendectomy', 'Tonsillectomy', 'Hernia Repair', 'Gallbladder Removal', 'Knee Surgery', 'Cataract Surgery','Other']
    selected_surgeries = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    if 'Other' in selected_surgeries:
        other_surgery = st.text_input('Other Surgery or Procedure')
        cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (other_surgery,))
        conn.commit()

    # Rheumatologic History and Family History Section
    st.markdown('<div class="box"><h4>Rheumatologic and Family History</h4></div>', unsafe_allow_html=True)

    # Previous Rheumatologic Diagnoses
    common_rheumatologic_diagnoses = ['Rheumatoid Arthritis', 'Ankylosing Spondylitis', 'Systemic Lupus Erythematosus', 'Sjögren\'s Syndrome', 'Psoriatic Arthritis', 'Gout','Other']
    selected_rheumatologic_diagnoses = st.multiselect('Common Previous Rheumatologic Diagnoses', common_rheumatologic_diagnoses)
    if 'Other' in selected_rheumatologic_diagnoses:
        other_rheumatologic_diagnosis = st.text_input('Other Diagnosis')
        cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (other_rheumatologic_diagnosis,))
        conn.commit()

    # Common Disease Activities
    common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe','Other']
    selected_activity = st.multiselect('Select Disease Activity', common_activities)
    if 'Other' in selected_activity:
        other_activities = st.text_input('Common Disease Activities')
        cursor.execute("INSERT INTO Activity (name) VALUES (%s)", (other_activities,))
        conn.commit()

    # Family History
    common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_family_history = st.multiselect('Common Family History of Rheumatic Diseases', common_family_history)
    if 'Other' in selected_family_history:
        other_family_history = st.text_input('Other Family History')
        cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s)", (other_family_history,))
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

def past_patient_reports_page():
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Text input for searching patient by ID
    patient_id_input = st.text_input("Enter Patient ID:")
    patient_name_input = st.text_input("Enter Patient Name:")

    # Execute SQL query to fetch past patient records if patient ID or name is provided
    if patient_id_input or patient_name_input:
        try:
            if patient_id_input:
                search_type = "ID"
                search_value = int(patient_id_input)
                condition = "Patient.patient_id = %s"
            else:
                search_type = "Name"
                search_value = f"%{patient_name_input.strip()}%"
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
                    filtered_record = {cursor.description[i][0]: record[i] for i in range(len(cursor.description)) if record[i] is not None}
                    # Display in a colored box
                    st.markdown(
                        f"""
                        <div style="background-color: #9370DB; padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px; color: white;">
                            <h3>Patient Record</h3>
                            <ul>
                                <li><strong>Patient ID:</strong> {filtered_record['patient_id']}</li>
                                <li><strong>Name:</strong> {filtered_record['name']}</li>
                                <li><strong>Age:</strong> {filtered_record['age']}</li>
                                <li><strong>Gender:</strong> {filtered_record['gender']}</li>
                                <li><strong>Diagnosis:</strong> {filtered_record['diagnosis']}</li>
                                <!-- Add more fields as needed -->
                            </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
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

past_patient_reports_page()


if __name__ == "__main__":
    main()

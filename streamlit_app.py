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

def surgeries_section(common_surgeries):
    selected_surgeries_widget = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    return selected_surgeries_widget

def new_patient_page():
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Initialize variables
    patient_id = None

    try:
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
        common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe', 'Other']
        common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis', 'Other']

        # Diagnosis
        selected_diagnoses = st.multiselect('Diagnosis', common_diagnoses)
        other_diagnosis_name = st.text_input('Enter Other Diagnosis') if 'Other' in selected_diagnoses else None

        # Medication
        selected_medications = st.multiselect('Medication', common_medications)
        other_medication_name = st.text_input('Enter Other Medication') if 'Other' in selected_medications else None

        # Allergy
        selected_allergies = st.multiselect('Allergy', common_allergies)
        other_allergy_name = st.text_input('Enter Other Allergy') if 'Other' in selected_allergies else None

        # Surgery
        selected_surgeries = st.multiselect('Surgery', common_surgeries)
        other_surgery_name = st.text_input('Enter Other Surgery') if 'Other' in selected_surgeries else None

        # Activity
        selected_activities = st.multiselect('Activity', common_activities)
        other_activity_name = st.text_input('Enter Other Activity') if 'Other' in selected_activities else None

        # Family History
        selected_family_history = st.multiselect('Family History', common_family_history)
        other_family_history_name = st.text_input('Enter Other Family History') if 'Other' in selected_family_history else None

        # Physical Examination Findings Section
        st.markdown('<div class="box"><h4>Physical Examination Findings</h4></div>', unsafe_allow_html=True)

        joint_swelling = st.checkbox('Joint Swelling')
        joint_tenderness = st.checkbox('Joint Tenderness')
        joint_warmth = st.checkbox('Joint Warmth')
        joint_redness = st.checkbox('Joint Redness')
        limited_range_of_motion = st.checkbox('Limited Range of Motion')
        muscle_weakness = st.checkbox('Muscle Weakness')
        other_finding_checkbox = st.checkbox('Other')
        other_finding_text = ""
        if other_finding_checkbox:
            other_finding_text = st.text_input('Specify Other Finding')

        # Diagnostic Tests Section
        st.markdown('<div class="box"><h4>Diagnostic Tests</h4></div>', unsafe_allow_html=True)
        diagnostic_tests = st.text_area('Enter Diagnostic Tests')

        # Notes and Comments Section
        st.markdown('<div class="box"><h4>Notes and Comments</h4></div>', unsafe_allow_html=True)
        notes_and_comments = st.text_area('Enter Notes and Comments')

        # Submit Button
        if st.button('Submit'):
            # Insert patient information into the Patient table
            cursor.execute("INSERT INTO Patient (name, age, gender) VALUES (%s, %s, %s)", (name, age, gender))
            conn.commit()

            patient_id = cursor.lastrowid

            # Insert other information into respective tables
            if other_diagnosis_name:
                cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (other_diagnosis_name,))
                conn.commit()
                diagnosis_id = cursor.lastrowid
                cursor.execute("INSERT INTO PatientMedicalHistory (patient_id, diagnosis_id) VALUES (%s, %s)", (patient_id, diagnosis_id))
                conn.commit()
            else:
                for diagnosis in selected_diagnoses:
                    cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (diagnosis,))
                    conn.commit()
                    diagnosis_id = cursor.lastrowid
                    cursor.execute("INSERT INTO PatientMedicalHistory (patient_id, diagnosis_id) VALUES (%s, %s)", (patient_id, diagnosis_id))
                    conn.commit()

            if other_medication_name:
                cursor.execute("INSERT INTO Medication (name) VALUES (%s)", (other_medication_name,))
                conn.commit()
                medication_id = cursor.lastrowid
                cursor.execute("INSERT INTO PatientCurrentMedication (patient_id, medication_id) VALUES (%s, %s)", (patient_id, medication_id))
                conn.commit()
            else:
                for medication in selected_medications:
                    cursor.execute("INSERT INTO Medication (name) VALUES (%s)", (medication,))
                    conn.commit()
                    medication_id = cursor.lastrowid
                    cursor.execute("INSERT INTO PatientCurrentMedication (patient_id, medication_id) VALUES (%s, %s)", (patient_id, medication_id))
                    conn.commit()

            if other_allergy_name:
                cursor.execute("INSERT INTO Allergy (name) VALUES (%s)", (other_allergy_name,))
                conn.commit()
                allergy_id = cursor.lastrowid
                cursor.execute("INSERT INTO PatientAllergy (patient_id, allergy_id) VALUES (%s, %s)", (patient_id, allergy_id))
                conn.commit()
            else:
                for allergy in selected_allergies:
                    cursor.execute("INSERT INTO Allergy (name) VALUES (%s)", (allergy,))
                    conn.commit()
                    allergy_id = cursor.lastrowid
                    cursor.execute("INSERT INTO PatientAllergy (patient_id, allergy_id) VALUES (%s, %s)", (patient_id, allergy_id))
                    conn.commit()

            if other_surgery_name:
                cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (other_surgery_name,))
                conn.commit()
                surgery_id = cursor.lastrowid
                cursor.execute("INSERT INTO PatientSurgery (patient_id, surgery_id) VALUES (%s, %s)", (patient_id, surgery_id))
                conn.commit()
            else:
                for surgery in selected_surgeries:
                    cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (surgery,))
                    conn.commit()
                    surgery_id = cursor.lastrowid
                    cursor.execute("INSERT INTO PatientSurgery (patient_id, surgery_id) VALUES (%s, %s)", (patient_id, surgery_id))
                    conn.commit()

            if other_activity_name:
                cursor.execute("INSERT INTO Activity (name) VALUES (%s)", (other_activity_name,))
                conn.commit()
                activity_id = cursor.lastrowid
                cursor.execute("INSERT INTO PatientActivity (patient_id, activity_id) VALUES (%s, %s)", (patient_id, activity_id))
                conn.commit()
            else:
                for activity in selected_activities:
                    cursor.execute("INSERT INTO Activity (name) VALUES (%s)", (activity,))
                    conn.commit()
                    activity_id = cursor.lastrowid
                    cursor.execute("INSERT INTO PatientActivity (patient_id, activity_id) VALUES (%s, %s)", (patient_id, activity_id))
                    conn.commit()

            if other_family_history_name:
                cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s)", (other_family_history_name,))
                conn.commit()
                family_history_id = cursor.lastrowid
                cursor.execute("INSERT INTO PatientFamilyHistory (patient_id, history_id) VALUES (%s, %s)", (patient_id, family_history_id))
                conn.commit()
            else:
                for family_history in selected_family_history:
                    cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s)", (family_history,))
                    conn.commit()
                    family_history_id = cursor.lastrowid
                    cursor.execute("INSERT INTO PatientFamilyHistory (patient_id, history_id) VALUES (%s, %s)", (patient_id, family_history_id))
                    conn.commit()


            # Insert physical examination findings
            cursor.execute("INSERT INTO PhysicalExamination (patient_id, joint_warmth, other_finding) VALUES (%s, %s, %s)", 
                           (patient_id, 1 if joint_warmth else 0, other_finding_text))
            conn.commit()

            # Insert diagnostic tests
            cursor.execute("INSERT INTO DiagnosticTests (patient_id, test_results) VALUES (%s, %s)", (patient_id, diagnostic_tests))
            conn.commit()

            # Insert notes and comments
            cursor.execute("INSERT INTO NotesAndComments (patient_id, notes_and_comments) VALUES (%s, %s)", (patient_id, notes_and_comments))
            conn.commit()

            st.success('Patient information submitted successfully.')
            st.sidebar.markdown('<div class="left-box"><h4>Patient Information</h4></div>', unsafe_allow_html=True)
            st.sidebar.write(f"Name: {name}")
            st.sidebar.write(f"Age: {age}")
            st.sidebar.write(f"Gender: {gender}")

    except mysql.connector.Error as e:
        st.error(f"Error inserting data into MySQL database: {e}")

    finally:
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

            for record in records:
                # Filter out None values
                filtered_record = {key: record[i] for i, key in enumerate(cursor.column_names) if record[i] is not None}
                # Modify display for fever
                if 'fever' in filtered_record:
                    if filtered_record['fever'] == 1:
                        filtered_record['fever'] = 'had fever: yes'
                    else:
                        del filtered_record['fever']
                # Filter out attributes with zero values (except fever)
                filtered_record = {key: value for key, value in filtered_record.items() if key != 'fever' and value != 0}
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

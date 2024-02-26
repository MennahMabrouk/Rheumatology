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

# Define surgeries_section function outside of new_patient_page function
def surgeries_section(cursor, common_surgeries, patient_id):
    selected_surgeries_widget = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    for surgery in selected_surgeries_widget:
        if surgery == 'Other':
            other_surgery_name = st.text_input('Enter Other Surgery')
            if other_surgery_name:
                # Insert 'Other' surgery into the Surgery table if it doesn't exist
                cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (other_surgery_name,))
                # Retrieve the last auto-generated surgery_id
                cursor.execute("SELECT LAST_INSERT_ID()")
                surgery_id = cursor.fetchone()[0]
                # Insert into PatientSurgery with valid surgery_id
                cursor.execute("INSERT INTO PatientSurgery (patient_id, surgery_id) VALUES (%s, %s)", (patient_id, surgery_id))
        else:
            # Insert selected surgery into the Surgery table if it doesn't exist
            cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (surgery,))
            # Retrieve the last auto-generated surgery_id
            cursor.execute("SELECT LAST_INSERT_ID()")
            surgery_id = cursor.fetchone()[0]
            # Insert into PatientSurgery with valid surgery_id
            cursor.execute("INSERT INTO PatientSurgery (patient_id, surgery_id) VALUES (%s, %s)", (patient_id, surgery_id))

def new_patient_page(common_diagnoses, common_medications, common_allergies, common_activities, common_family_history):
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Initialize empty lists to store data temporarily
    selected_diagnoses_list = []
    selected_medications_list = []
    selected_allergies_list = []
    selected_activity_list = []
    selected_family_history_list = []

    try:
        # Patient Information Section
        st.markdown('<div class="box"><h4>Patient Information</h4></div>', unsafe_allow_html=True)
        name = st.text_input('Name')
        age = st.number_input('Age', min_value=0, max_value=150, value=0, step=1)
        gender = st.selectbox('Gender', ['Male', 'Female'])

        # Medical History Section
        st.markdown('<div class="box"><h4>Medical History</h4></div>', unsafe_allow_html=True)

        # Previous Diagnoses
        selected_diagnoses = st.multiselect('Common Previous Diagnoses', common_diagnoses)
        for diagnosis in selected_diagnoses:
            selected_diagnoses_list.append(diagnosis)

        # Current Medications
        selected_medications = st.multiselect('Common Current Medications', common_medications)
        for medication in selected_medications:
            selected_medications_list.append(medication)

        # Allergies Section
        selected_allergies = st.multiselect('Common Allergies', common_allergies)
        for allergy in selected_allergies:
            selected_allergies_list.append(allergy)

        # Rheumatologic History and Family History Section
        st.markdown('<div class="box"><h4>Rheumatologic and Family History</h4></div>', unsafe_allow_html=True)
        
        # Common Disease Activities
        selected_activity = st.multiselect('Select Disease Activity', common_activities)
        for activity in selected_activity:
            selected_activity_list.append(activity)

        # Family History
        selected_family_history = st.multiselect('Common Family History of Rheumatic Diseases', common_family_history)
        for family_history in selected_family_history:
            selected_family_history_list.append(family_history)

        # Submit Button
        if st.button('Submit'):
            # Insert patient information into the Patient table
            cursor.execute("INSERT INTO Patient (name, age, gender) VALUES (%s, %s, %s)", (name, age, gender))
            conn.commit()
            # Get the auto-generated patient_id
            patient_id = cursor.lastrowid

            # Inserting previous diagnoses
            for diagnosis in selected_diagnoses_list:
                if diagnosis == 'Other':
                    other_diagnosis_name = st.text_input('Enter Other Diagnosis')
                    if other_diagnosis_name:
                        cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s) ON DUPLICATE KEY UPDATE diagnosis_id=LAST_INSERT_ID(diagnosis_id)", (other_diagnosis_name,))
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        diagnosis_id = cursor.fetchone()[0]
                        cursor.execute("INSERT INTO PatientMedicalHistory (patient_id, diagnosis_id) VALUES (%s, %s)", (patient_id, diagnosis_id))
                else:
                    cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s) ON DUPLICATE KEY UPDATE diagnosis_id=LAST_INSERT_ID(diagnosis_id)", (diagnosis,))
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    diagnosis_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO PatientMedicalHistory (patient_id, diagnosis_id) VALUES (%s, %s)", (patient_id, diagnosis_id))

            # Inserting current medications
            for medication in selected_medications_list:
                if medication == 'Other':
                    other_medication_name = st.text_input('Enter Other Medication')
                    if other_medication_name:
                        cursor.execute("INSERT INTO Medication (name) VALUES (%s) ON DUPLICATE KEY UPDATE medication_id=LAST_INSERT_ID(medication_id)", (other_medication_name,))
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        medication_id = cursor.fetchone()[0]
                        cursor.execute("INSERT INTO PatientCurrentMedication (patient_id, medication_id) VALUES (%s, %s)", (patient_id, medication_id))
                else:
                    cursor.execute("INSERT INTO Medication (name) VALUES (%s) ON DUPLICATE KEY UPDATE medication_id=LAST_INSERT_ID(medication_id)", (medication,))
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    medication_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO PatientCurrentMedication (patient_id, medication_id) VALUES (%s, %s)", (patient_id, medication_id))

            # Inserting allergies
            for allergy in selected_allergies_list:
                if allergy == 'Other':
                    other_allergy_name = st.text_input('Enter Other Allergy')
                    if other_allergy_name:
                        cursor.execute("INSERT INTO Allergy (name) VALUES (%s) ON DUPLICATE KEY UPDATE allergy_id=LAST_INSERT_ID(allergy_id)", (other_allergy_name,))
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        allergy_id = cursor.fetchone()[0]
                        cursor.execute("INSERT INTO PatientAllergy (patient_id, allergy_id) VALUES (%s, %s)", (patient_id, allergy_id))
                else:
                    cursor.execute("INSERT INTO Allergy (name) VALUES (%s) ON DUPLICATE KEY UPDATE allergy_id=LAST_INSERT_ID(allergy_id)", (allergy,))
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    allergy_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO PatientAllergy (patient_id, allergy_id) VALUES (%s, %s)", (patient_id, allergy_id))

            # Inserting disease activities
            for activity in selected_activity_list:
                cursor.execute("INSERT INTO PatientActivity (patient_id, activity_id) VALUES (%s, (SELECT activity_id FROM Activity WHERE name = %s LIMIT 1))", (patient_id, activity))
            
            # Inserting family history
            for family_history in selected_family_history_list:
                if family_history == 'Other':
                    other_family_history_name = st.text_input('Enter Other Family History')
                    if other_family_history_name:
                        cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s) ON DUPLICATE KEY UPDATE history_id=LAST_INSERT_ID(history_id)", (other_family_history_name,))
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        family_history_id = cursor.fetchone()[0]
                        cursor.execute("INSERT INTO PatientFamilyHistory (patient_id, history_id) VALUES (%s, %s)", (patient_id, family_history_id))
                else:
                    cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s) ON DUPLICATE KEY UPDATE history_id=LAST_INSERT_ID(history_id)", (family_history,))
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    family_history_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO PatientFamilyHistory (patient_id, history_id) VALUES (%s, %s)", (patient_id, family_history_id))

            # Commit the transaction
            conn.commit()

            # Display success message
            st.success('Patient information submitted successfully.')
            
            # Display patient information in a box on the left side
            st.sidebar.markdown('<div class="left-box"><h4>Patient Information</h4></div>', unsafe_allow_html=True)
            st.sidebar.write(f"Name: {name}")
            st.sidebar.write(f"Age: {age}")
            st.sidebar.write(f"Gender: {gender}")

    except mysql.connector.Error as e:
        # Display error message if an error occurs during data insertion
        st.error(f"Error inserting data into MySQL database: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Call the function with common lists as arguments
new_patient_page(common_diagnoses, common_medications, common_allergies, common_activities, common_family_history)


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

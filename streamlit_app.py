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

def fetch_existing_items(cursor, table_name, column_name):
    cursor.execute(f"SELECT {column_name} FROM {table_name}")
    return set(row[0] for row in cursor.fetchall())

def surgeries_section(cursor, common_surgeries, patient_id):
    existing_surgeries = fetch_existing_items(cursor, "Surgery", "name")

    selected_surgeries_widget = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    for surgery in selected_surgeries_widget:
        if surgery == 'Other':
            other_surgery_name = st.text_input('Enter Other Surgery')
            if other_surgery_name:
                # Insert 'Other' surgery into the Surgery table if it doesn't exist
                if other_surgery_name not in existing_surgeries:
                    cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (other_surgery_name,))
                    existing_surgeries.add(other_surgery_name)
                # Retrieve the surgery_id
                cursor.execute("SELECT surgery_id FROM Surgery WHERE name = %s", (other_surgery_name,))
                surgery_id = cursor.fetchone()[0]
                # Insert into PatientSurgery with valid surgery_id
                cursor.execute("INSERT INTO PatientSurgery (patient_id, surgery_id) VALUES (%s, %s)", (patient_id, surgery_id))
        else:
            # Insert selected surgery into the Surgery table if it doesn't exist
            if surgery not in existing_surgeries:
                cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (surgery,))
                existing_surgeries.add(surgery)
            # Retrieve the surgery_id
            cursor.execute("SELECT surgery_id FROM Surgery WHERE name = %s", (surgery,))
            surgery_id = cursor.fetchone()[0]
            # Insert into PatientSurgery with valid surgery_id
            cursor.execute("INSERT INTO PatientSurgery (patient_id, surgery_id) VALUES (%s, %s)", (patient_id, surgery_id))

def common_section(cursor, common_items, table_name, column_name, patient_id):
    existing_items = fetch_existing_items(cursor, table_name, column_name)

    selected_items = st.multiselect(f'Common {table_name}', common_items)
    for item in selected_items:
        if item == 'Other':
            other_item_name = st.text_input(f'Enter Other {table_name[:-1]}')
            if other_item_name:
                # Insert 'Other' item into the table if it doesn't exist
                if other_item_name not in existing_items:
                    cursor.execute(f"INSERT INTO {table_name} ({column_name}) VALUES (%s)", (other_item_name,))
                    existing_items.add(other_item_name)
                # Retrieve the item_id
                cursor.execute(f"SELECT {table_name[:-1]}_id FROM {table_name} WHERE {column_name} = %s", (other_item_name,))
                item_id = cursor.fetchone()[0]
                # Insert into Patient table with valid item_id
                cursor.execute(f"INSERT INTO Patient{table_name} (patient_id, {table_name[:-1]}_id) VALUES (%s, %s)", (patient_id, item_id))
        else:
            # Insert selected item into the table if it doesn't exist
            if item not in existing_items:
                cursor.execute(f"INSERT INTO {table_name} ({column_name}) VALUES (%s)", (item,))
                existing_items.add(item)
            # Retrieve the item_id
            cursor.execute(f"SELECT {table_name[:-1]}_id FROM {table_name} WHERE {column_name} = %s", (item,))
            item_id = cursor.fetchone()[0]
            # Insert into Patient table with valid item_id
            cursor.execute(f"INSERT INTO Patient{table_name} (patient_id, {table_name[:-1]}_id) VALUES (%s, %s)", (patient_id, item_id))

def new_patient_page():
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Patient Information Section
        st.markdown('<div class="box"><h4>Patient Information</h4></div>', unsafe_allow_html=True)
        name = st.text_input('Name')
        age = st.number_input('Age', min_value=0, max_value=150, value=0, step=1)
        gender = st.selectbox('Gender', ['Male', 'Female'])

        # Insert patient information into the Patient table
        cursor.execute("INSERT INTO Patient (name, age, gender) VALUES (%s, %s, %s)", (name, age, gender))
        conn.commit()
        # Get the auto-generated patient_id
        patient_id = cursor.lastrowid
        
        # Medical History Section
        st.markdown('<div class="box"><h4>Medical History</h4></div>', unsafe_allow_html=True)

        # Define common options
        common_diagnoses = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis', 'Other']
        common_medications = ['NSAIDs', 'Corticosteroids', 'DMARDs', 'Biologics', 'Pain Relievers', 'Immunosuppressants', 'Other']
        common_allergies = ['Pollen', 'Dust', 'Pet Dander', 'Mold', 'Food', 'Medications', 'Other']
        common_rheumatologic_diagnoses = ['Rheumatoid Arthritis', 'Ankylosing Spondylitis', 'Systemic Lupus Erythematosus', 'Sjögren\'s Syndrome', 'Psoriatic Arthritis', 'Gout', 'Other']
        common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe', 'Other']
        common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis', 'Other']

        common_section(cursor, common_diagnoses, "Diagnosis", "name", patient_id)
        common_section(cursor, common_medications, "Medication", "name", patient_id)
        common_section(cursor, common_allergies, "Allergy", "name", patient_id)
        common_section(cursor, common_rheumatologic_diagnoses, "RheumatologicDiagnosis", "name", patient_id)
        common_section(cursor, common_activities, "Activity", "name", patient_id)
        common_section(cursor, common_rheumatologic_diagnoses, "FamilyHistory", "name", patient_id)

        # Surgeries Section
        surgeries_section(cursor, common_surgeries, patient_id)

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
        other_finding_checkbox = st.checkbox('Other')
        other_finding_text = ""  # Initialize other_finding_text variable
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
            # Inserting review of systems, physical examination, diagnostic tests, and notes and comments into respective tables
            cursor.execute("INSERT INTO ReviewOfSystems (patient_id, joint_pain, joint_stiffness, swelling, fatigue, fever, skin_rashes, eye_problems) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (patient_id, joint_pain, joint_stiffness, swelling, fatigue, fever, skin_rashes, eye_problems))
            
            cursor.execute("INSERT INTO PhysicalExamination (patient_id, joint_swelling, joint_tenderness, joint_warmth, joint_redness, limited_range_of_motion, muscle_weakness, other_finding) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (patient_id, joint_swelling, joint_tenderness, joint_warmth, joint_redness, limited_range_of_motion, muscle_weakness, other_finding_text))
            
            cursor.execute("INSERT INTO DiagnosticTests (patient_id, test_results) VALUES (%s, %s)", (patient_id, diagnostic_tests))
            
            cursor.execute("INSERT INTO NotesAndComments (patient_id, notes_and_comments) VALUES (%s, %s)", (patient_id, notes_and_comments))

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

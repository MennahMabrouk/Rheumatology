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

    # Insert Patient Information into the database
    try:
        cursor.execute("INSERT INTO Patient (name, age, gender) VALUES (%s, %s, %s)", (name, age, gender))
        conn.commit()
        print("Patient information inserted successfully")  # Add this line
    except mysql.connector.Error as e:
        st.error(f"Error inserting patient information into database: {e}")
        print("Error inserting patient information:", e)  # Add this line

    # Medical History Section
    st.markdown('<div class="box"><h4>Medical History</h4></div>', unsafe_allow_html=True)

    # Previous Diagnoses
    common_diagnoses = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_diagnoses = st.multiselect('Common Previous Diagnoses', common_diagnoses)
    for diagnosis in selected_diagnoses:
        try:
            cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (diagnosis,))
            conn.commit()
            print("Diagnosis inserted successfully:", diagnosis)  # Add this line
        except mysql.connector.Error as e:
            st.error(f"Error inserting diagnosis into database: {e}")
            print("Error inserting diagnosis:", e)  # Add this line

    # Current Medications
    common_medications = ['NSAIDs', 'Corticosteroids', 'DMARDs', 'Biologics', 'Pain Relievers', 'Immunosuppressants','Other']
    selected_medications = st.multiselect('Common Current Medications', common_medications)
    for medication in selected_medications:
        try:
            cursor.execute("INSERT INTO Medication (name) VALUES (%s)", (medication,))
            conn.commit()
            print("Medication inserted successfully:", medication)  # Add this line
        except mysql.connector.Error as e:
            st.error(f"Error inserting medication into database: {e}")
            print("Error inserting medication:", e)  # Add this line

    # Allergies Section
    common_allergies = ['Pollen', 'Dust', 'Pet Dander', 'Mold', 'Food', 'Medications','Other']
    selected_allergies = st.multiselect('Common Allergies', common_allergies)
    for allergy in selected_allergies:
        try:
            cursor.execute("INSERT INTO Allergy (name) VALUES (%s)", (allergy,))
            conn.commit()
            print("Allergy inserted successfully:", allergy)  # Add this line
        except mysql.connector.Error as e:
            st.error(f"Error inserting allergy into database: {e}")
            print("Error inserting allergy:", e)  # Add this line

    # Surgeries Section
    common_surgeries = ['Appendectomy', 'Tonsillectomy', 'Hernia Repair', 'Gallbladder Removal', 'Knee Surgery', 'Cataract Surgery','Other']
    selected_surgeries = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    for surgery in selected_surgeries:
        try:
            cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (surgery,))
            conn.commit()
            print("Surgery inserted successfully:", surgery)  # Add this line
        except mysql.connector.Error as e:
            st.error(f"Error inserting surgery into database: {e}")
            print("Error inserting surgery:", e)  # Add this line
# Rheumatologic History and Family History Section
st.markdown('<div class="box"><h4>Rheumatologic and Family History</h4></div>', unsafe_allow_html=True)

# Previous Rheumatologic Diagnoses
common_rheumatologic_diagnoses = ['Rheumatoid Arthritis', 'Ankylosing Spondylitis', 'Systemic Lupus Erythematosus', 'Sjögren\'s Syndrome', 'Psoriatic Arthritis', 'Gout','Other']
selected_rheumatologic_diagnoses = st.multiselect('Common Previous Rheumatologic Diagnoses', common_rheumatologic_diagnoses)
for diagnosis in selected_rheumatologic_diagnoses:
    try:
        cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (diagnosis,))
        conn.commit()
        print("Rheumatologic diagnosis inserted successfully:", diagnosis)  # Add this line
    except mysql.connector.Error as e:
        st.error(f"Error inserting rheumatologic diagnosis into database: {e}")
        print("Error inserting rheumatologic diagnosis:", e)  # Add this line

# Common Disease Activities
common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe','Other']
selected_activity = st.multiselect('Select Disease Activity', common_activities)
for activity in selected_activity:
    try:
        cursor.execute("INSERT INTO Activity (name) VALUES (%s)", (activity,))
        conn.commit()
        print("Activity inserted successfully:", activity)  # Add this line
    except mysql.connector.Error as e:
        st.error(f"Error inserting activity into database: {e}")
        print("Error inserting activity:", e)  # Add this line

# Family History
common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
selected_family_history = st.multiselect('Common Family History of Rheumatic Diseases', common_family_history)
for history in selected_family_history:
    try:
        cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s)", (history,))
        conn.commit()
        print("Family history inserted successfully:", history)  # Add this line
    except mysql.connector.Error as e:
        st.error(f"Error inserting family history into database: {e}")
        print("Error inserting family history:", e)  # Add this line

# Review of Systems Section
st.markdown('<div class="box"><h4>Review of Systems</h4></div>', unsafe_allow_html=True)

joint_pain = st.checkbox('Joint Pain')
joint_stiffness = st.checkbox('Joint Stiffness')
swelling = st.checkbox('Swelling')
fatigue = st.checkbox('Fatigue')
fever = st.checkbox('Fever')
skin_rashes = st.checkbox('Skin Rashes or Lesions')
eye_problems = st.checkbox('Eye Problems')

# Insert Review of Systems data into the database
try:
    cursor.execute("INSERT INTO ReviewOfSystems (patient_id, joint_pain, joint_stiffness, swelling, fatigue, fever, skin_rashes, eye_problems) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (patient_id, joint_pain, joint_stiffness, swelling, fatigue, fever, skin_rashes, eye_problems))
    conn.commit()
    print("Review of Systems data inserted successfully")  # Add this line
except mysql.connector.Error as e:
    st.error(f"Error inserting Review of Systems data into database: {e}")
    print("Error inserting Review of Systems data:", e)  # Add this line

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

# Insert Physical Examination Findings data into the database
try:
    cursor.execute("INSERT INTO PhysicalExamination (patient_id, joint_swelling, joint_tenderness, joint_warmth, joint_redness, limited_range_of_motion, muscle_weakness, other_finding) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (patient_id, joint_swelling, joint_tenderness, joint_warmth, joint_redness, limited_range_of_motion, muscle_weakness, other_finding_text))
    conn.commit()
    print("Physical Examination Findings data inserted successfully")  # Add this line
except mysql.connector.Error as e:
    st.error(f"Error inserting Physical Examination Findings data into database: {e}")
    print("Error inserting Physical Examination Findings data:", e)  # Add this line

# Diagnostic Tests Section
st.markdown('<div class="box"><h4>Diagnostic Tests</h4></div>', unsafe_allow_html=True)
diagnostic_tests = st.text_area('Enter Diagnostic Tests')

# Insert Diagnostic Tests data into the database
try:
    cursor.execute("INSERT INTO DiagnosticTests (patient_id, test_results) VALUES (%s, %s)", (patient_id, diagnostic_tests))
    conn.commit()
    print("Diagnostic Tests data inserted successfully")  # Add this line
except mysql.connector.Error as e:
    st.error(f"Error inserting Diagnostic Tests data into database: {e}")
    print("Error inserting Diagnostic Tests data:", e)  # Add this line

# Notes and Comments Section
st.markdown('<div class="box"><h4>Notes and Comments</h4></div>', unsafe_allow_html=True)
notes_and_comments = st.text_area('Enter Notes and Comments')

# Insert Notes and Comments data into the database
try:
    cursor.execute("INSERT INTO NotesAndComments (patient_id, notes_and_comments) VALUES (%s, %s)", (patient_id, notes_and_comments))
    conn.commit()
    print("Notes and Comments data inserted successfully")  # Add this line
except mysql.connector.Error as e:
    st.error(f"Error inserting Notes and Comments data into database: {e}")
    print("Error inserting Notes and Comments data:", e)  # Add this line

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

        # Insert Patient data into the database
        cursor.execute("INSERT INTO Patient (name, age, gender) VALUES (%s, %s, %s)", (name, age, gender))
        conn.commit()
        patient_id = cursor.lastrowid
        print("Patient data inserted successfully with ID:", patient_id)  # Add this line

        # Insert Medical History data into the database
        for diagnosis in selected_diagnoses:
            cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (diagnosis,))
            conn.commit()
            print("Diagnosis inserted successfully:", diagnosis)  # Add this line

        # Insert Current Medications data into the database
        for medication in selected_medications:
            cursor.execute("INSERT INTO Medication (name) VALUES (%s)", (medication,))
            conn.commit()
            print("Medication inserted successfully:", medication)  # Add this line

        # Insert Allergies data into the database
        for allergy in selected_allergies:
            cursor.execute("INSERT INTO Allergy (name) VALUES (%s)", (allergy,))
            conn.commit()
            print("Allergy inserted successfully:", allergy)  # Add this line

        # Insert Surgeries data into the database
        for surgery in selected_surgeries:
            cursor.execute("INSERT INTO Surgery (name) VALUES (%s)", (surgery,))
            conn.commit()
            print("Surgery inserted successfully:", surgery)  # Add this line

        # Insert Rheumatologic History data into the database
        for diagnosis in selected_rheumatologic_diagnoses:
            cursor.execute("INSERT INTO Diagnosis (name) VALUES (%s)", (diagnosis,))
            conn.commit()
            print("Rheumatologic diagnosis inserted successfully:", diagnosis)  # Add this line

        # Insert Common Disease Activities data into the database
        for activity in selected_activity:
            cursor.execute("INSERT INTO Activity (name) VALUES (%s)", (activity,))
            conn.commit()
            print("Activity inserted successfully:", activity)  # Add this line

        # Insert Family History data into the database
        for history in selected_family_history:
            cursor.execute("INSERT INTO FamilyHistory (name) VALUES (%s)", (history,))
            conn.commit()
            print("Family history inserted successfully:", history)  # Add this line

        # Insert Review of Systems data into the database
        cursor.execute("INSERT INTO ReviewOfSystems (patient_id, joint_pain, joint_stiffness, swelling, fatigue, fever, skin_rashes, eye_problems) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (patient_id, joint_pain, joint_stiffness, swelling, fatigue, fever, skin_rashes, eye_problems))
        conn.commit()
        print("Review of Systems data inserted successfully")  # Add this line

        # Insert Physical Examination Findings data into the database
        cursor.execute("INSERT INTO PhysicalExamination (patient_id, joint_swelling, joint_tenderness, joint_warmth, joint_redness, limited_range_of_motion, muscle_weakness, other_finding) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (patient_id, joint_swelling, joint_tenderness, joint_warmth, joint_redness, limited_range_of_motion, muscle_weakness, other_finding_text))
        conn.commit()
        print("Physical Examination Findings data inserted successfully")  # Add this line

        # Insert Diagnostic Tests data into the database
        cursor.execute("INSERT INTO DiagnosticTests (patient_id, test_results) VALUES (%s, %s)", (patient_id, diagnostic_tests))
        conn.commit()
        print("Diagnostic Tests data inserted successfully")  # Add this line

        # Insert Notes and Comments data into the database
        cursor.execute("INSERT INTO NotesAndComments (patient_id, notes_and_comments) VALUES (%s, %s)", (patient_id, notes_and_comments))
        conn.commit()
        print("Notes and Comments data inserted successfully")  # Add this line

    except mysql.connector.Error as e:
        st.error(f"Error inserting data into MySQL database: {e}")


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

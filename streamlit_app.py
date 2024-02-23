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
    </style>
"""

def main():
    st.title('Rheumatology Patient Checking Chart')

    # Inject custom CSS
    st.markdown(box_styles, unsafe_allow_html=True)

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
    common_diagnoses = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_diagnoses = st.multiselect('Common Previous Diagnoses', common_diagnoses)
    if 'Other' in selected_diagnoses:
        other_diagnosis = st.text_input('Other Diagnosis')

    # Insert patient information into the database
    if st.button('Submit'):
        try:
            # SQL query to insert patient information into the Patient table
            insert_patient_query = "INSERT INTO Patient (name, age, gender) VALUES (%s, %s, %s)"
            cursor.execute(insert_patient_query, (name, age, gender))
            conn.commit()

            # Insert medical history information into the PatientMedicalHistory table
            for diagnosis in selected_diagnoses:
                insert_diagnosis_query = "INSERT INTO Diagnosis (name) VALUES (%s)"
                cursor.execute(insert_diagnosis_query, (diagnosis,))
                conn.commit()

                # Get the diagnosis_id for the inserted diagnosis
                diagnosis_id = cursor.lastrowid

                # Insert into the PatientMedicalHistory table
                insert_patient_medical_history_query = "INSERT INTO PatientMedicalHistory (patient_id, diagnosis_id) VALUES (%s, %s)"
                cursor.execute(insert_patient_medical_history_query, (cursor.lastrowid, diagnosis_id))
                conn.commit()

            # If Other Diagnosis is provided, insert it into the Diagnosis table
            if 'Other' in selected_diagnoses:
                insert_other_diagnosis_query = "INSERT INTO Diagnosis (name) VALUES (%s)"
                cursor.execute(insert_other_diagnosis_query, (other_diagnosis,))
                conn.commit()

                # Get the diagnosis_id for the inserted diagnosis
                other_diagnosis_id = cursor.lastrowid

                # Insert into the PatientMedicalHistory table
                insert_patient_medical_history_query = "INSERT INTO PatientMedicalHistory (patient_id, diagnosis_id) VALUES (%s, %s)"
                cursor.execute(insert_patient_medical_history_query, (cursor.lastrowid, other_diagnosis_id))
                conn.commit()

            st.success('Patient information submitted successfully.')
        except mysql.connector.Error as e:
            st.error(f"Error inserting data into MySQL database: {e}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

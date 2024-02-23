import streamlit as st

def main():
    st.title('Rheumatology Patient Checking Chart')

    # Patient Information Section
    st.header('Patient Information')
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0, max_value=150, value=0, step=1)
    gender = st.selectbox('Gender', ['Male', 'Female'])

    # Medical History Section
    st.header('Medical History')
    previous_diagnoses = st.text_area('Previous Diagnoses')
    current_medications = st.text_area('Current Medications')
    
    # Allergies Section
    st.header('Allergies')
    common_allergies = ['Pollen', 'Dust', 'Pet Dander', 'Mold', 'Food', 'Medications']
    selected_allergies = st.multiselect('Common Allergies', common_allergies)
    if 'Other' in selected_allergies:
        other_allergy = st.text_input('Other Allergy')

    surgeries = st.text_area('Past Surgeries or Procedures')
    family_history = st.text_area('Family History of Rheumatic Diseases')

    # Rheumatologic History Section
    st.header('Rheumatologic History')
    previous_rheumatologic_diagnoses = st.text_area('Previous Rheumatologic Diagnoses')
    disease_activity = st.text_area('Disease Activity')
    response_to_treatments = st.text_area('Response to Previous Treatments')

    # Review of Systems Section
    st.header('Review of Systems')
    with st.expander('Click to expand'):
        joint_pain = st.checkbox('Joint Pain')
        joint_stiffness = st.checkbox('Joint Stiffness')
        swelling = st.checkbox('Swelling')
        fatigue = st.checkbox('Fatigue')
        fever = st.checkbox('Fever')
        skin_rashes = st.checkbox('Skin Rashes or Lesions')
        eye_problems = st.checkbox('Eye Problems')

    # Physical Examination Findings Section
    st.header('Physical Examination Findings')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Physical Examination Findings")

    # Diagnostic Tests Section
    st.header('Diagnostic Tests')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Diagnostic Tests")

    # Assessment and Plan Section
    st.header('Assessment and Plan')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Assessment and Plan")

    # Patient Education and Counseling Section
    st.header('Patient Education and Counseling')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Patient Education and Counseling")

    # Documentation of Consent and Referrals Section
    st.header('Documentation of Consent and Referrals')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Documentation of Consent and Referrals")

    # Follow-up Instructions Section
    st.header('Follow-up Instructions')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Follow-up Instructions")

    # Notes and Comments Section
    st.header('Notes and Comments')
    with st.expander('Click to expand'):
        st.write("- Checkboxes for Notes and Comments")

    # Submit Button
    if st.button('Submit'):
        # You can add code here to save the entered information or perform further actions
        st.success('Patient information submitted successfully.')

if __name__ == "__main__":
    main()


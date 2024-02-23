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
    
    # Previous Diagnoses
    common_diagnoses = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_diagnoses = st.multiselect('Common Previous Diagnoses', common_diagnoses)
    if 'Other' in selected_diagnoses:
        other_diagnosis = st.text_input('Other Diagnosis')

    # Current Medications
    common_medications = ['NSAIDs', 'Corticosteroids', 'DMARDs', 'Biologics', 'Pain Relievers', 'Immunosuppressants','Other']
    selected_medications = st.multiselect('Common Current Medications', common_medications)
    if 'Other' in selected_medications:
        other_medication = st.text_input('Other Medication')

    
    # Allergies Section
    common_allergies = ['Pollen', 'Dust', 'Pet Dander', 'Mold', 'Food', 'Medications','Other']
    selected_allergies = st.multiselect('Common Allergies', common_allergies)
    if 'Other' in selected_allergies:
        other_allergy = st.text_input('Other Allergy')

    common_surgeries = ['Appendectomy', 'Tonsillectomy', 'Hernia Repair', 'Gallbladder Removal', 'Knee Surgery', 'Cataract Surgery','Other']
    selected_surgeries = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    if 'Other' in selected_surgeries:
        other_surgery = st.text_input('Other Surgery or Procedure')

    # Rheumatologic History Section
    st.header('Rheumatologic History')
    
    #Previous Rheumatologic Diagnoses
    common_rheumatologic_diagnoses = ['Rheumatoid Arthritis', 'Ankylosing Spondylitis', 'Systemic Lupus Erythematosus', 'Sjögren\'s Syndrome', 'Psoriatic Arthritis', 'Gout','Other']
    selected_rheumatologic_diagnoses = st.multiselect('Common Previous Rheumatologic Diagnoses', common_rheumatologic_diagnoses)
    if 'Other' in selected_rheumatologic_diagnoses:
        other_rheumatologic_diagnosis = st.text_input('Other Diagnosis')

   # Common Disease Activities
    common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe','Other']
    selected_activity = st.multiselect('Select Disease Activity', common_activities)
    if 'Other' in selected_activity:
        other_activities = st.text_input('Common Disease Activities')
        
    # Family History Section
    common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_family_history = st.multiselect('Common Family History of Rheumatic Diseases', common_family_history)
    if 'Other' in selected_family_history:
        other_family_history = st.text_input('Other Family History')

    
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

    # Expander for Physical Examination Findings
    with st.expander('Click to expand'):
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
    st.markdown('<h4>Notes and Comments</h4>', unsafe_allow_html=True)
    Notes_and_Comments = st.text_input

    # Submit Button
    if st.button('Submit'):
        # You can add code here to save the entered information or perform further actions
        st.success('Patient information submitted successfully.')


if __name__ == "__main__":
    main()


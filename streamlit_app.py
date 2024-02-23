import streamlit as st

# Custom CSS for styling the entire page with a purple frame
page_styles = """
    <style>
        .report-container {
            padding: 20px;
            border-radius: 20px;
            border: 2px solid #9370DB; /* Purple */
            background-color: #f0f0f0; /* Light gray */
        }
    </style>
"""

# Custom CSS for styling boxes with colors
box_styles = """
    <style>
        .box {
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            background-color: #9370DB; /* Purple */
            color: white;
            margin-bottom: 20px;
        }
    </style>
"""

def main():
    st.title('Rheumatology Patient Checking Chart')

    # Inject custom CSS for the page
    st.markdown(page_styles, unsafe_allow_html=True)

    # Inject custom CSS for the boxes
    st.markdown(box_styles, unsafe_allow_html=True)

    # Container for the entire report
    st.markdown('<div class="report-container">', unsafe_allow_html=True)

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

    # Surgeries Section
    common_surgeries = ['Appendectomy', 'Tonsillectomy', 'Hernia Repair', 'Gallbladder Removal', 'Knee Surgery', 'Cataract Surgery','Other']
    selected_surgeries = st.multiselect('Common Surgeries or Procedures', common_surgeries)
    if 'Other' in selected_surgeries:
        other_surgery = st.text_input('Other Surgery or Procedure')

    # Rheumatologic History and Family History Section
    st.markdown('<div class="box"><h4>Rheumatologic and Family History</h4></div>', unsafe_allow_html=True)

    # Previous Rheumatologic Diagnoses
    common_rheumatologic_diagnoses = ['Rheumatoid Arthritis', 'Ankylosing Spondylitis', 'Systemic Lupus Erythematosus', 'Sjögren\'s Syndrome', 'Psoriatic Arthritis', 'Gout','Other']
    selected_rheumatologic_diagnoses = st.multiselect('Common Previous Rheumatologic Diagnoses', common_rheumatologic_diagnoses)
    if 'Other' in selected_rheumatologic_diagnoses:
        other_rheumatologic_diagnosis = st.text_input('Other Diagnosis')

    # Common Disease Activities
    common_activities = ['Active', 'Inactive', 'Flaring', 'Remission', 'Mild', 'Moderate', 'Severe','Other']
    selected_activity = st.multiselect('Select Disease Activity', common_activities)
    if 'Other' in selected_activity:
        other_activities = st.text_input('Common Disease Activities')

    # Family History
    common_family_history = ['Arthritis', 'Lupus', 'Fibromyalgia', 'Gout', 'Osteoporosis', 'Rheumatoid Arthritis','Other']
    selected_family_history = st.multiselect('Common Family History of Rheumatic Diseases', common_family_history)
    if 'Other' in selected_family_history:
        other_family_history = st.text_input('Other Family History')

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

    # Close the report-container
    st.markdown('</div>', unsafe_allow_html=True)

    # Submit Button
    if st.button('Submit'):
        # You can add code here to save the entered information or perform further actions
        st.success('Patient information submitted successfully.')


if __name__ == "__main__":
    main()

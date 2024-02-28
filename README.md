# Rheumatology Patient Checking Chart

<img src="https://www.ama-assn.org/sites/ama-assn.org/files/styles/image_ratio_16_9/public/2023-08/2023-08-08-RHEUMATOID_Index-1170x780.jpg?itok=n0-mrzaV" alt="Rheumatoid Arthritis" width="500">

This repository contains a Streamlit web application for managing patient information in a rheumatology clinic. The application allows users to input and retrieve patient data, including personal information, medical history, physical examination findings, diagnostic tests, and notes/comments.

```
## Application Link

You can access the application [here](https://rheumatology-9jcnnpbxcuvcyykbjaegyi.streamlit.app/#patient-information).

## Database

The application uses a MySQL database for storing patient information. The database management system used is [phpMyAdmin](https://www.phpmyadmin.net/).

...

### Requirements

Make sure you have the following dependencies installed:

- `numpy==1.21.0`
- `pandas==1.3.0`
- `scikit-learn==0.24.2`
- `mysql-connector-python`

These dependencies are listed in the `requirements.txt` file. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

### Database Connection

The application requires a MySQL database to store patient information. Update the database connection details in the `connect_to_database` function within `streamlit_app.py`. Replace the placeholder values (`host`, `user`, `password`, `database`) with your actual database credentials.

## Usage

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run streamlit_app.py
```

This command will start a local server, and you can access the application through your web browser.

### Navigation

The application provides two main pages for navigation:

1. **New Patient**: Allows users to input data for a new patient, including personal information, medical history, physical examination findings, diagnostic tests, and notes/comments.
2. **Past Patient Reports**: Enables users to search for past patient records using either the patient ID or name. The application retrieves and displays relevant information for the selected patient.

## Code Explanation

### `streamlit_app.py`

- **Database Connection**: The `connect_to_database` function establishes a connection to the MySQL database using the provided credentials. If an error occurs during the connection attempt, an error message is displayed.

- **Custom CSS**: The `box_styles` variable defines custom CSS styles for styling boxes with different colors.

- **Main Functionality**:
  - The `main` function is the entry point of the Streamlit application. It sets up the application title and navigation menu.
  - Depending on the selected page, either the `new_patient_page` or `past_patient_reports_page` function is called.

- **New Patient Page**:
  - The `new_patient_page` function handles the input of data for a new patient. It includes sections for patient information, medical history, physical examination findings, diagnostic tests, and notes/comments.
  - Data input fields include text inputs, number inputs, select boxes, checkboxes, and multiselect boxes.
  - Upon submission, the patient information is inserted into the database tables, and a success message is displayed.

- **Past Patient Reports Page**:
  - The `past_patient_reports_page` function allows users to search for past patient records based on patient ID or name.
  - If a patient is found, relevant information is fetched from the database and displayed in colored boxes.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

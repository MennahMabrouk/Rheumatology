# Rheumatology Patient Checking Chart

This repository contains a Streamlit web application for managing patient information in a rheumatology clinic. The application allows users to input and retrieve patient data, including personal information, medical history, physical examination findings, diagnostic tests, and notes/comments.

## Setup

### Requirements

Make sure you have the following dependencies installed:

- `numpy==1.21.0`
- `pandas==1.3.0`
- `scikit-learn==0.24.2`
- `mysql-connector-python`

You can install these dependencies using `pip` with the provided `requirements.txt` file.

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

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

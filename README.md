# Docx Date Converter App

This application converts .docx files that have a dynamic date field and saves them with a static date of the data when the .docx was created. It is a solution to the challenge of preserving the integrity of .docx files in archival systems.

## The Challenge

A large portion of data produced within the Canton Administration is created in the .docx format. Despite .docx being the most frequently used format, it's not permitted for archival due to potential inconsistencies across different Word versions and functions (e.g., automatically updated fields) that can lead to mutable content. Therefore, it's recommended to convert every Word document to pdf/A-2u for archival purposes, but this conversion leads to information loss.

We ask the question: "Could we archive documents in .docx, i.e., in their original format, given that Word has been a prominent document format for 40 years and might continue to be for the next 40 years?"

This challenge aims to develop software that performs an analysis of .docx documents, identifies critical elements concerning the mutability of .docx, and creates a new archive-friendly Word document.

## Running the Software

To run the software, you need to have both Python (for the Flask backend) and Node.js (for the React frontend) installed on your machine.

1. First, navigate to the Flask app's directory and activate your virtual environment (if you're using one). Then, run the Flask app:

`cd /path/to/flask`

# Activate your virtual environment here if necessary

`python app.py`

2. In a new terminal window, navigate to the React app's directory and start the React app:

`cd /path/to/react`
`npm start`


Or, you can run both the Flask and React apps at the same time with one command:

`npm run dev`


# Dashboard Application

A web application to upload Excel files and display data in a dashboard with screenshot functionality.

## Features

- **Excel File Upload**: Upload .xlsx or .xls files to display data
- **Dashboard**: View all data from the uploaded Excel file in a table format
- **Landing Page Name Display**: Automatically detects and displays the landing page name above the table (if present in the data)
- **Screenshot**: Take screenshots of the dashboard table for client presentation

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
   - Dashboard: `http://localhost:5000/`

## Usage

1. **Upload Excel File**: Click "Choose File" to select an Excel file (.xlsx or .xls), then click "Upload"
2. **View Data**: The dashboard will automatically display all data from the uploaded file
3. **Take Screenshot**: Click the "Take Screenshot" button to download a PNG image of the dashboard table
4. **Refresh**: Click "Refresh" to reload the data

## File Structure

```
dash/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/                 # Data directory (created automatically)
│   └── uploaded_data.xlsx  # Excel file storing uploaded data
└── templates/            # HTML templates
    └── dashboard.html    # Dashboard with file upload and data table
```

## Excel File Format

The application will display all columns and rows from your Excel file. If your Excel file contains a column with "Landing Page" or "Page" in the name, that value will be displayed above the table.

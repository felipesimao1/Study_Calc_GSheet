# System Information

This Python script is designed to update course information in a Google Sheets spreadsheet. It allows users to input the name of a course, the total number of hours for the course, and the number of hours they plan to study per week. The script then updates the Google Sheets spreadsheet with this information and provides an estimate of the time required to complete all courses based on the user's study schedule.

## Getting Started

To use this script, you'll need to have Python installed on your machine. You'll also need to create a Google Sheets spreadsheet and obtain the necessary credentials to access it via the Google Sheets API.

### Prerequisites

- Python 3.x
- Google Sheets API credentials (`creds.json`)

### Installing

```bash
# Clone the repository to your local machine
git clonehttps://github.com/felipesimao1/Study_Calc_GSheet.git

# Install the required Python packages
pip install gspread oauth2client
```

Follow the on-screen prompts to input the course information. The script will update the Google Sheets spreadsheet with the provided information and display the estimated time required to complete all courses.

### Features
- *Easy Course Management:* Users can easily input course information, including the course name, total hours, and study hours per week.
- *Automatic Spreadsheet Update:* The script automatically updates a Google Sheets spreadsheet with the provided course information.
- *Time Estimation:* The script calculates the total time required to complete all courses based on the user's study schedule.

### Use Cases
- *Student Course Management:* Students can use this script to keep track of their courses and study schedules in a centralized spreadsheet.
- *Training Program Management:* Organizations offering training programs can use this script to manage course details and provide participants with estimated completion times.
- *Personal Development Tracking:* Individuals pursuing personal development goals can use this script to organize their learning activities and track their progress over time.

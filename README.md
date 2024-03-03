# Course Information Update

This Python script is designed to update course information in a Google Sheets spreadsheet. It allows users to input the name of a course, the total number of hours for the course, and the number of hours they plan to study per week. The script then updates the Google Sheets spreadsheet with this information and provides an estimate of the time required to complete all courses based on the user's study schedule.

## Getting Started

To use this script, you'll need to have Python installed on your machine. You'll also need to create a Google Sheets spreadsheet and obtain the necessary credentials to access it via the Google Sheets API.

### Prerequisites

- Python 3.x
- Google Sheets API credentials (`creds.json`)

### Installing

1. Clone the repository to your local machine:
git clone https://github.com/your_username/course-information-update.git

2. Install the required Python packages:
pip install gspread oauth2client

### Usage

1. Run the Python script:
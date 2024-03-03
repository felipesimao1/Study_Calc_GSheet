import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('study_calc')

def get_user_data():
    """
    Gets the user information about the course
    """
    print("Please enter course information:")
    
    course_name = str(input("Insert the name of the course: "))
    course_hours = int(input("Insert the total hours of the course: "))
    hours_study_per_week = int(input("How many hours do you want to study per week? "))
    
    return course_name, course_hours, hours_study_per_week

def update_course_info(course_name, course_hours):
    """
    Updates the course information in the worksheet
    """
    worksheet = SHEET.get_worksheet(0)  # Assuming the first worksheet is used
    
    # Append the new course information to the worksheet
    worksheet.append_row([course_name, course_hours])
    print("Course information updated successfully.")

def calculate_total_weeks(total_hours, hours_per_week):
    """
    Calculates the total weeks needed to finish all courses
    """
    total_weeks = total_hours / hours_per_week
    return total_weeks

def main():
    print("Welcome to Course Information Update")
    
    course_name, course_hours, hours_study_per_week = get_user_data()
    
    # Update course information in the worksheet
    update_course_info(course_name, course_hours)
    
    # Count total number of courses and calculate total hours
    worksheet = SHEET.get_worksheet(0)
    data = worksheet.get_all_values()[1:]  # Exclude header row
    total_courses = len(data)
    total_hours = sum(int(course[1]) for course in data)  # Assuming total hours are in the second column (index 1)
    
    # Calculate total weeks needed to finish all courses
    total_weeks = calculate_total_weeks(total_hours, hours_study_per_week)
    
    print(f"You have {total_courses} courses, with a total of {total_hours} hours.")
    print(f"Studying {hours_study_per_week} hours per week, you will finish all courses in {total_weeks:.1f} weeks.")

if __name__ == "__main__":
    main()

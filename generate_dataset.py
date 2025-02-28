import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define possible values for several factors
departments = ["Engineering", "Sales", "Marketing", "HR", "Finance", "Operations", "IT"]
roles = ["Manager", "Senior Engineer", "Junior Engineer", "Associate", "Intern", "Team Lead", "Director", "Analyst"]
leave_types = ["Sick Leave", "Casual Leave", "Vacation", "Emergency Leave", "Maternity/Paternity Leave"]
approval_statuses = ["Approved", "Rejected", "Pending"]
project_involvements = ["High", "Medium", "Low"]
impact_levels = ["High", "Medium", "Low"]

# Helper function to generate a random date between two given dates
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Assume a current date for our calculations
current_date = datetime(2025, 2, 17)

def generate_employee_record():
    """Generate a unique synthetic employee leave record."""
    # Employee basic details
    employee_id = random.randint(10000, 999999)  # Increased range to avoid uniqueness errors
    employee_name = fake.name()
    department = random.choice(departments)
    role = random.choice(roles)
    
    # Date of Joining between Jan 1, 2010 and Dec 31, 2022
    doj = random_date(datetime(2010, 1, 1), datetime(2022, 12, 31))
    date_of_joining = doj.strftime("%Y-%m-%d")
    
    # Employment Status (most likely active)
    employment_status = random.choices(["Active", "Resigned", "Terminated"], weights=[0.8, 0.15, 0.05])[0]
    
    # Total Work Duration (in years) calculated from DOJ to current_date or resignation date
    if employment_status == "Active":
        work_duration_years = round((current_date - doj).days / 365, 1)
    else:
        resignation_date = random_date(doj, current_date)
        work_duration_years = round((resignation_date - doj).days / 365, 1)
    
    # Leave-related details
    leave_date_obj = random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))
    leave_date = leave_date_obj.strftime("%Y-%m-%d")
    leave_type = random.choice(leave_types)
    leave_approval_status = random.choice(approval_statuses)
    leave_frequency = random.randint(0, 10)
    
    # Policy-related flags
    weekend_leaves = random.choice(["Yes", "No"])
    sandwich_policy = random.choice(["Yes", "No"])
    
    # Task and performance related details
    tasks_assigned = random.randint(10, 100)
    tasks_completed_on_time = random.randint(0, tasks_assigned)
    missed_deadlines = tasks_assigned - tasks_completed_on_time
    employee_performance_score = round(random.uniform(50, 100), 1)
    
    # Team information
    team_size = random.randint(5, 50)
    active_employees = random.randint(1, team_size)
    leaves_in_team = random.randint(0, team_size)
    
    # Additional employee metrics
    skill_rating = round(random.uniform(1, 10), 1)
    past_performance_reviews = round(random.uniform(1, 5), 1)
    project_involvement = random.choice(project_involvements)
    total_leave_days = random.randint(0, 30)
    leave_impact = random.choice(impact_levels)
    performance_rating = round(random.uniform(1, 5), 1)
    eligibility_score = round(random.uniform(0, 100), 1)

    # Create a record dictionary containing all factors
    record = {
        "Employee ID": employee_id,
        "Employee Name": employee_name,
        "Department/Team": department,
        "Designation/Role": role,
        "Date of Joining": date_of_joining,
        "Current Employment Status": employment_status,
        "Total Work Duration (years)": work_duration_years,
        "Leave Date": leave_date,
        "Leave Type": leave_type,
        "Leave Approval Status": leave_approval_status,
        "Leave Frequency": leave_frequency,
        "Weekend Leaves (Sat/Sun Included?)": weekend_leaves,
        "Sandwich Policy Applied?": sandwich_policy,
        "Tasks Assigned": tasks_assigned,
        "Tasks Completed on Time": tasks_completed_on_time,
        "Missed Deadlines": missed_deadlines,
        "Employee Performance Score": employee_performance_score,
        "Team Size": team_size,
        "Active Employees in Team": active_employees,
        "Leaves in Team for Same Period": leaves_in_team,
        "Skill Rating": skill_rating,
        "Past Performance Reviews": past_performance_reviews,
        "Project Involvement": project_involvement,
        "Total Leave Days (per month/year)": total_leave_days,
        "Leave Impact on Work": leave_impact,
        "Performance Rating": performance_rating,
        "Eligibility Score": eligibility_score
    }
    
    return record

def generate_synthetic_dataset(n=10000):
    """Generate a synthetic dataset with 'n' unique records."""
    data = [generate_employee_record() for _ in range(n)]
    return data

# Generate the dataset with 10,000 records
synthetic_data = generate_synthetic_dataset(10000)

# Convert to a DataFrame and save to CSV
df = pd.DataFrame(synthetic_data)
csv_filename = "synthetic_employee_leave_data_10000.csv"
df.to_csv(csv_filename, index=False)

# Display a preview of the generated data
print(df.head())

print(f"✅ 10,000 records generated and saved as '{csv_filename}'")

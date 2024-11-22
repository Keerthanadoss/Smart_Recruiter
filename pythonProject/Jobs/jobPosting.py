# Python Console Application for Job Creation and Publishing Workflow

class JobService:
    def create_job(self):
        print("Job Creation Process")
        job_title = input("Enter the job title: ")
        job_description = input("Enter the job description: ")
        department = input("Select a department (HR, IT, Marketing, Sales): ")
        job_location = input("Enter the job location: ")
        employment_type = input("Select employment type (Full-time, Part-time, Contract, Internship): ")
        salary_range = input("Enter the salary range: ")
        application_deadline = input("Select the application deadline (YYYY-MM-DD): ")
        required_qualifications = input("Enter the required qualifications: ")
        preferred_qualifications = input("Enter the preferred qualifications (optional): ")
        responsibilities = input("Enter the job responsibilities: ")

        # Validate inputs
        if not job_title:
            print("Job title is required.")
            return
        if not job_description or len(job_description) < 50:
            print("Job description is required and must be at least 50 characters.")
            return
        if not department:
            print("Department is required.")
            return
        if not job_location:
            print("Job location is required.")
            return
        if not employment_type:
            print("Employment type is required.")
            return
        if not salary_range.isdigit():
            print("Salary range must be numeric.")
            return
        if not application_deadline:
            print("Application deadline is required.")
            return
        if not required_qualifications:
            print("Required qualifications are required.")
            return
        if not responsibilities:
            print("Responsibilities are required.")
            return

        action = input("Do you want to Save as Draft or Publish? (draft/publish): ").lower()
        if action == "draft":
            print("Job posting saved as draft.")
        elif action == "publish":
            print("Job posting published successfully.")
        else:
            print("Invalid action.")

    def view_drafts(self):
        print("Viewing Draft Job Listings")
        # Simulate draft job listings
        drafts = [
            {"title": "Software Engineer", "department": "IT", "date_created": "2023-10-01"},
            {"title": "Marketing Specialist", "department": "Marketing", "date_created": "2023-10-02"}
        ]
        for draft in drafts:
            print(f"Title: {draft['title']}, Department: {draft['department']}, Date Created: {draft['date_created']}")

        action = input("Do you want to Edit or Delete a draft? (edit/delete): ").lower()
        if action == "edit":
            print("Opening job creation screen with draft details...")
        elif action == "delete":
            print("Draft job posting deleted.")
        else:
            print("Invalid action.")

    def view_published_jobs(self):
        print("Viewing Published Job Listings")
        # Simulate published job listings
        published_jobs = [
            {"title": "Data Analyst", "department": "IT", "date_published": "2023-10-03"},
            {"title": "HR Manager", "department": "HR", "date_published": "2023-10-04"}
        ]
        for job in published_jobs:
            print(f"Title: {job['title']}, Department: {job['department']}, Date Published: {job['date_published']}")

        action = input("Do you want to View, Edit, or Unpublish a job? (view/edit/unpublish): ").lower()
        if action == "view":
            print("Opening job details screen...")
        elif action == "edit":
            print("Opening job creation screen with published job details...")
        elif action == "unpublish":
            print("Job posting unpublished.")
        else:
            print("Invalid action.")

def main():
    job_service = JobService()
    while True:
        print("\nJob Controller")
        print("1. Create Job")
        print("2. View Drafts")
        print("3. View Published Jobs")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            job_service.create_job()
        elif choice == '2':
            job_service.view_drafts()
        elif choice == '3':
            job_service.view_published_jobs()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

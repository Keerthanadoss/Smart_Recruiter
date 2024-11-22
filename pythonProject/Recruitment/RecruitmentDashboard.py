# Python Console Application for Real-time Recruitment Dashboard

class InterviewSchedulingScreen:
    def __init__(self):
        self.total_applications = 100  # Example data
        self.applications_in_progress = 30  # Example data
        self.hired_candidates = 10  # Example data
        self.rejected_candidates = 20  # Example data
        self.applications = [
            {"name": "Alice Johnson", "position": "Project Manager", "source": "Job Board",
             "date_applied": "2023-10-01", "status": "In Progress"},
            {"name": "Bob Smith", "position": "Software Developer", "source": "Referral", "date_applied": "2023-10-02",
             "status": "Hired"}
        ]

    def display_dashboard(self):
        print("Recruitment Dashboard")
        date_range = input("Select date range (e.g., 2023-10-01 to 2023-10-31): ")
        print("Refreshing dashboard data...")
        self.display_key_metrics()
        self.display_charts()
        self.display_applications_table()

    def display_key_metrics(self):
        print("Key Metrics")
        print(f"Total Applications: {self.total_applications}")
        print(f"Applications in Progress: {self.applications_in_progress}")
        print(f"Hired Candidates: {self.hired_candidates}")
        print(f"Rejected Candidates: {self.rejected_candidates}")

    def display_charts(self):
        print("Charts")
        print("Applications Over Time (Line Chart)")
        print("Applications by Source (Pie Chart)")
        print("Applications by Status (Bar Chart)")

    def display_applications_table(self):
        print("Applications Table")
        for app in self.applications:
            print(
                f"Name: {app['name']}, Position: {app['position']}, Source: {app['source']}, Date Applied: {app['date_applied']}, Status: {app['status']}")
        action = input("Do you want to View Details of an application? (yes/no): ").lower()
        if action == "yes":
            self.view_application_details()

    def view_application_details(self):
        name = input("Enter the applicant's name to view details: ")
        for app in self.applications:
            if app['name'] == name:
                print(f"Viewing details for {name}")
                ApplicationDetails(app).view_details()
                return
        print("Application not found.")


class ApplicationDetails:
    def __init__(self, application):
        self.application = application

    def view_details(self):
        print("Application Details")
        print(f"Name: {self.application['name']}")
        print(f"Position: {self.application['position']}")
        print(f"Source: {self.application['source']}")
        print(f"Date Applied: {self.application['date_applied']}")
        print(f"Current Status: {self.application['status']}")
        self.display_status_history()
        action = input("Do you want to Update Status or Send Message? (update/send): ").lower()
        if action == "update":
            RescheduleInterviewScreen(self.application).update_status()
        elif action == "send":
            self.send_message()

    def display_status_history(self):
        print("Status History")
        print("Date: 2023-10-01, Status: Applied, Notes: Initial application")  # Example
        print("Date: 2023-10-02, Status: In Progress, Notes: Under review")  # Example

    def send_message(self):
        print("Compose Message")
        message = input("Enter your message: ")
        print(f"Message sent to {self.application['name']}: {message}")


class RescheduleInterviewScreen:
    def __init__(self, application):
        self.application = application

    def update_status(self):
        print("Update Status")
        print(f"Current Status: {self.application['status']}")
        new_status = input("Select new status (New, In Progress, Hired, Rejected): ")
        notes = input("Enter any notes: ")
        self.application['status'] = new_status
        print(f"Status updated to {new_status}.")


def main():
    dashboard = InterviewSchedulingScreen()
    while True:
        print("nMain Menu")
        print("1. Recruitment Dashboard")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            dashboard.display_dashboard()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Python Console Application for Job Application Management Workflow

class Dashboard:
    def __init__(self):
        self.job_openings = 5  # Example data
        self.applications = 20  # Example data
        self.recent_applications = [
            {"name": "John Doe", "job_title": "Software Engineer", "status": "Applied", "date": "2023-10-01"},
            {"name": "Jane Smith", "job_title": "Data Analyst", "status": "In Review", "date": "2023-10-02"}
        ]

    def display_dashboard(self):
        print("Dashboard")
        print(f"Job Openings: {self.job_openings}")
        print(f"Applications: {self.applications}")
        print("Recent Applications:")
        for app in self.recent_applications:
            print(f"Name: {app['name']}, Job Title: {app['job_title']}, Status: {app['status']}, Date: {app['date']}")
        action = input("Do you want to View All Applications? (yes/no): ").lower()
        if action == "yes":
            ApplicationManagement().manage_applications()

class ApplicationManagement:
    def __init__(self):
        self.applications = [
            {"name": "John Doe", "job_title": "Software Engineer", "status": "Applied", "date": "2023-10-01"},
            {"name": "Jane Smith", "job_title": "Data Analyst", "status": "In Review", "date": "2023-10-02"}
        ]

    def manage_applications(self):
        print("Applications Management")
        self.display_applications()
        action = input("Do you want to View, Move to Next Stage, or Reject an application? (view/move/reject): ").lower()
        if action == "view":
            self.view_application()
        elif action == "move":
            self.move_to_next_stage()
        elif action == "reject":
            self.reject_application()

    def display_applications(self):
        print("Applications List")
        for app in self.applications:
            print(f"Name: {app['name']}, Job Title: {app['job_title']}, Status: {app['status']}, Date: {app['date']}")

    def view_application(self):
        name = input("Enter the applicant's name to view: ")
        for app in self.applications:
            if app['name'] == name:
                print(f"Viewing application for {name}")
                ApplicationDetails(app).view_details()
                return
        print("Application not found.")

    def move_to_next_stage(self):
        name = input("Enter the applicant's name to move to the next stage: ")
        for app in self.applications:
            if app['name'] == name:
                app['status'] = "In Review"  # Example status change
                print(f"Application for {name} moved to the next stage.")
                return
        print("Application not found.")

    def reject_application(self):
        name = input("Enter the applicant's name to reject: ")
        self.applications = [app for app in self.applications if app['name'] != name]
        print(f"Application for {name} rejected.")

class ApplicationDetails:
    def __init__(self, application):
        self.application = application

    def view_details(self):
        print("Application Details")
        print(f"Name: {self.application['name']}")
        print(f"Email: example@example.com")  # Placeholder
        print(f"Phone: 123-456-7890")  # Placeholder
        print(f"Job Title: {self.application['job_title']}")
        print(f"Department: IT")  # Placeholder
        print(f"Location: New York")  # Placeholder
        print(f"Current Status: {self.application['status']}")
        self.change_status()

    def change_status(self):
        new_status = input("Enter new status (Applied, In Review, Interview, Offered, Rejected): ")
        self.application['status'] = new_status
        print(f"Status changed to {new_status}.")

class Notifications:
    def __init__(self):
        self.notifications = [
            {"message": "New application received", "date": "2023-10-01"},
            {"message": "Interview scheduled", "date": "2023-10-02"}
        ]

    def manage_notifications(self):
        print("Notifications")
        self.display_notifications()
        action = input("Do you want to Mark as Read or Delete a notification? (read/delete): ").lower()
        if action == "read":
            self.mark_as_read()
        elif action == "delete":
            self.delete_notification()

    def display_notifications(self):
        print("Notifications List")
        for notification in self.notifications:
            print(f"Message: {notification['message']}, Date: {notification['date']}")

    def mark_as_read(self):
        message = input("Enter the notification message to mark as read: ")
        print(f"Notification '{message}' marked as read.")

    def delete_notification(self):
        message = input("Enter the notification message to delete: ")
        self.notifications = [notif for notif in self.notifications if notif['message'] != message]
        print(f"Notification '{message}' deleted.")

def main():
    dashboard = Dashboard()
    while True:
        print("\nMain Menu")
        print("1. Dashboard")
        print("2. Notifications")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            dashboard.display_dashboard()
        elif choice == '2':
            Notifications().manage_notifications()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

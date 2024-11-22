# Python Console Application for Interview Scheduling Workflow

class InterviewSchedulingDashboard:
    def __init__(self):
        self.upcoming_interviews = 3  # Example data
        self.interviews = [
            {"name": "Alice Johnson", "job_title": "Project Manager", "date": "2023-10-10", "time": "10:00 AM", "status": "Scheduled"},
            {"name": "Bob Smith", "job_title": "Software Developer", "date": "2023-10-11", "time": "2:00 PM", "status": "Scheduled"}
        ]

    def display_dashboard(self):
        print("Interview Scheduling Dashboard")
        print(f"Upcoming Interviews: {self.upcoming_interviews}")
        print("Scheduled Interviews:")
        for interview in self.interviews:
            print(f"Name: {interview['name']}, Job Title: {interview['job_title']}, Date: {interview['date']}, Time: {interview['time']}, Status: {interview['status']}")
        action = input("Do you want to Schedule New Interview, View, Reschedule, or Cancel an interview? (schedule/view/reschedule/cancel): ").lower()
        if action == "schedule":
            InterviewSchedulingScreen().schedule_interview()
        elif action == "view":
            self.view_interview()
        elif action == "reschedule":
            self.reschedule_interview()
        elif action == "cancel":
            self.cancel_interview()

    def view_interview(self):
        name = input("Enter the applicant's name to view: ")
        for interview in self.interviews:
            if interview['name'] == name:
                print(f"Viewing interview for {name}")
                InterviewDetails(interview).view_details()
                return
        print("Interview not found.")

    def reschedule_interview(self):
        name = input("Enter the applicant's name to reschedule: ")
        for interview in self.interviews:
            if interview['name'] == name:
                RescheduleInterviewScreen(interview).reschedule()
                return
        print("Interview not found.")

    def cancel_interview(self):
        name = input("Enter the applicant's name to cancel: ")
        self.interviews = [interview for interview in self.interviews if interview['name'] != name]
        print(f"Interview for {name} canceled.")

class InterviewSchedulingScreen:
    def schedule_interview(self):
        print("Schedule New Interview")
        applicant_name = input("Select applicant: ")
        job_title = input("Select job title: ")
        interview_date = input("Select interview date: ")
        interview_time = input("Select interview time: ")
        interviewers = input("Select interviewers: ")
        interview_mode = input("Select interview mode (In-Person, Video Call, Phone Call): ")
        interview_location = ""
        if interview_mode == "In-Person":
            interview_location = input("Enter interview location: ")
        print(f"Interview scheduled for {applicant_name} on {interview_date} at {interview_time}.")

class InterviewDetails:
    def __init__(self, interview):
        self.interview = interview

    def view_details(self):
        print("Interview Details")
        print(f"Name: {self.interview['name']}")
        print(f"Job Title: {self.interview['job_title']}")
        print(f"Interview Date: {self.interview['date']}")
        print(f"Interview Time: {self.interview['time']}")
        print(f"Interview Mode: In-Person")  # Example
        print(f"Interviewers: John Doe, Jane Doe")  # Example
        action = input("Do you want to Reschedule or Cancel the interview? (reschedule/cancel): ").lower()
        if action == "reschedule":
            RescheduleInterviewScreen(self.interview).reschedule()
        elif action == "cancel":
            InterviewSchedulingDashboard().cancel_interview()

class RescheduleInterviewScreen:
    def __init__(self, interview):
        self.interview = interview

    def reschedule(self):
        print("Reschedule Interview")
        new_date = input("Select new interview date: ")
        new_time = input("Select new interview time: ")
        self.interview['date'] = new_date
        self.interview['time'] = new_time
        print(f"Interview rescheduled to {new_date} at {new_time}.")

def main():
    dashboard = InterviewSchedulingDashboard()
    while True:
        print("\nMain Menu")
        print("1. Interview Scheduling Dashboard")
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

# Python code for a console-based Custom Reports Module

class Report:
    def __init__(self, name, date_created, created_by, data):
        self.name = name
        self.date_created = date_created
        self.created_by = created_by
        self.data = data

class CustomReportsModule:
    def __init__(self):
        self.reports = []

    def display_dashboard(self):
        print("Custom Reports Dashboard")
        print("1. Create New Report")
        print("2. View Saved Reports")
        choice = input("Select an option: ")

        if choice == '1':
            self.create_report()
        elif choice == '2':
            self.view_saved_reports()
        else:
            print("Invalid choice. Returning to dashboard.")
            self.display_dashboard()

    def create_report(self):
        print("Create Report")
        report_name = input("Report Name: ")
        date_created = "2023-10-15"  # Example date
        created_by = "Admin"  # Example user
        data = self.get_report_data()

        new_report = Report(report_name, date_created, created_by, data)
        self.reports.append(new_report)
        print("Report created successfully!")
        self.display_dashboard()

    def get_report_data(self):
        # Simulate data collection based on criteria
        print("Select fields to include in the report:")
        fields = ["Applicant Name", "Date Applied", "Status", "Source"]
        selected_fields = input(f"Choose from {fields}: ")
        return f"Data with fields: {selected_fields}"

    def view_saved_reports(self):
        if not self.reports:
            print("No reports available.")
            self.display_dashboard()
            return

        print("Saved Reports:")
        for idx, report in enumerate(self.reports):
            print(f"{idx + 1}. {report.name} - {report.date_created} by {report.created_by}")

        choice = input("Select a report to view (or 'b' to go back): ")
        if choice.lower() == 'b':
            self.display_dashboard()
        else:
            self.view_report_details(int(choice) - 1)

    def view_report_details(self, index):
        if 0 <= index < len(self.reports):
            report = self.reports[index]
            print(f"Report Name: {report.name}")
            print(f"Date Created: {report.date_created}")
            print(f"Created By: {report.created_by}")
            print(f"Data: {report.data}")
            self.report_actions(index)
        else:
            print("Invalid report selection.")
            self.view_saved_reports()

    def report_actions(self, index):
        print("1. Edit Report")
        print("2. Delete Report")
        print("3. Export Report")
        choice = input("Select an action: ")

        if choice == '1':
            self.edit_report(index)
        elif choice == '2':
            self.delete_report(index)
        elif choice == '3':
            self.export_report(index)
        else:
            print("Invalid choice.")
            self.report_actions(index)

    def edit_report(self, index):
        print("Edit Report")
        report = self.reports[index]
        report.name = input(f"Report Name ({report.name}): ") or report.name
        report.data = self.get_report_data()
        print("Report updated successfully!")
        self.display_dashboard()

    def delete_report(self, index):
        del self.reports[index]
        print("Report deleted successfully!")
        self.display_dashboard()

    def export_report(self, index):
        print("Exporting report...")
        # Simulate export functionality
        print("Report exported successfully!")
        self.display_dashboard()

if __name__ == "__main__":
    module = CustomReportsModule()
    module.display_dashboard()

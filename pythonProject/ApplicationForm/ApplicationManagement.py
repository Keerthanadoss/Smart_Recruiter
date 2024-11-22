# Python Console Application for Customizable Application Forms Workflow

class FormService:
    def __init__(self):
        self.forms = []

    def manage_forms(self):
        print("Application Forms Management")
        self.display_forms()
        action = input("Do you want to Create, Edit, or Delete a form? (create/edit/delete): ").lower()
        if action == "create":
            self.create_form()
        elif action == "edit":
            self.edit_form()
        elif action == "delete":
            self.delete_form()
        else:
            print("Invalid action.")

    def display_forms(self):
        print("Form List")
        for form in self.forms:
            print(f"Form Name: {form['name']}, Associated Job: {form['job']}")

    def create_form(self):
        print("Form Creation")
        form_name = input("Enter the form name: ")
        associated_job = input("Select a job: ")

        # Validate inputs
        if not form_name:
            print("Form name is required.")
            return
        if not associated_job:
            print("Associated job is required.")
            return

        form = {"name": form_name, "job": associated_job, "fields": []}
        while True:
            add_field = input("Do you want to add a field? (yes/no): ").lower()
            if add_field == "yes":
                field_name = input("Enter the field name: ")
                field_type = input("Select field type (Textbox, Dropdown, Checkbox, Radio Button, Date Picker): ")
                field_options = ""
                if field_type in ["Dropdown", "Checkbox", "Radio Button"]:
                    field_options = input("Enter options separated by commas: ")
                form["fields"].append({"name": field_name, "type": field_type, "options": field_options})
            elif add_field == "no":
                break
            else:
                print("Invalid choice.")

        self.forms.append(form)
        print("Form created successfully.")

    def edit_form(self):
        print("Edit Form")
        self.display_forms()
        form_name = input("Enter the form name to edit: ")
        for form in self.forms:
            if form['name'] == form_name:
                new_name = input("Enter new form name: ")
                new_job = input("Select new associated job: ")
                form['name'] = new_name
                form['job'] = new_job
                print("Form updated successfully.")
                return
        print("Form not found.")

    def delete_form(self):
        print("Delete Form")
        self.display_forms()
        form_name = input("Enter the form name to delete: ")
        self.forms = [form for form in self.forms if form['name'] != form_name]
        print("Form deleted successfully.")


def main():
    form_service = FormService()
    while True:
        print("nForm Controller")
        print("1. Manage Forms")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            form_service.manage_forms()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

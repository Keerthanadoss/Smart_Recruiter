# Python Console Application for Job Categorization Workflow

class CategoryService:
    def __init__(self):
        self.categories = []

    def manage_categories(self):
        print("Job Categories Management")
        category_type = input("Select category type (Department, Location, Employment Type): ")
        category_name = input("Enter the category name: ")

        # Validate inputs
        if not category_type:
            print("Category type is required.")
            return
        if not category_name:
            print("Category name is required.")
            return

            # Add new category
        self.categories.append({"type": category_type, "name": category_name})
        print("Category added successfully.")
        self.display_categories()

    def display_categories(self):
        print("Categories List")
        for category in self.categories:
            print(f"Type: {category['type']}, Name: {category['name']}")

    def edit_category(self):
        print("Edit Category")
        self.display_categories()
        category_name = input("Enter the category name to edit: ")
        for category in self.categories:
            if category['name'] == category_name:
                new_type = input("Enter new category type: ")
                new_name = input("Enter new category name: ")
                category['type'] = new_type
                category['name'] = new_name
                print("Category updated successfully.")
                return
        print("Category not found.")

    def delete_category(self):
        print("Delete Category")
        self.display_categories()
        category_name = input("Enter the category name to delete: ")
        self.categories = [category for category in self.categories if category['name'] != category_name]
        print("Category deleted successfully.")


def main():
    category_service = CategoryService()
    while True:
        print("nCategory Controller")
        print("1. Manage Categories")
        print("2. Edit Category")
        print("3. Delete Category")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            category_service.manage_categories()
        elif choice == '2':
            category_service.edit_category()
        elif choice == '3':
            category_service.delete_category()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

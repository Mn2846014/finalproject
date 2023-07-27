import os
#BudgetTracker class to store budget, income, expenses, and savings data
class BudgetTracker:
    def __init__(self):
         # Initialize dictionaries to store data
        self.budget = {}
        self.income = {}
        self.expenses = {}
        self.savings = {}
# Methods to set budget, income, expenses, and savings for a given period
    def set_budget(self, period, amount):
        self.budget[period] = amount

    def set_income(self, period, amount):
        self.income[period] = amount

    def set_expenses(self, period, expense_name, amount):
        if period not in self.expenses:
            self.expenses[period] = {}
        self.expenses[period][expense_name] = amount

    def set_savings(self, period, amount):
        self.savings[period] = amount
   # Methods to update income, expenses, and savings for a given period
    def update_income(self, period, amount):
        if period in self.income:
            self.income[period] = amount

    def update_expenses(self, period, expense_name, amount):
        if period in self.expenses and expense_name in self.expenses[period]:
            self.expenses[period][expense_name] = amount

    def update_savings(self, period, amount):
        if period in self.savings:
            self.savings[period] = amount
    # Methods to get budget, income, expenses, and savings summaries
    def get_budget_summary(self):
        return self.budget

    def get_income_summary(self):
        return self.income

    def get_expenses_summary(self):
        return self.expenses

    def get_savings_summary(self):
        return self.savings
# FinancialSummary class to generate and save financial summaries

class FinancialSummary:
    def __init__(self, budget_tracker):
        self.budget_tracker = budget_tracker
 # Generate a summary text based on the data in BudgetTracker
    def generate_summary_text(self):
        budget_summary = self.budget_tracker.get_budget_summary()
        income_summary = self.budget_tracker.get_income_summary()
        expenses_summary = self.budget_tracker.get_expenses_summary()
        savings_summary = self.budget_tracker.get_savings_summary()

        summary_text = "Financial Summary:\n\n"
  # Create summary for each period (monthly and weekly)
        for period, budget_amount in budget_summary.items():
            summary_text += f"{period.capitalize()} Budget: ${budget_amount}\n"

            if period in income_summary:
                summary_text += f"  Income: ${income_summary[period]}\n"

            if period in expenses_summary:
                summary_text += "  Expenses:\n"
                for expense_name, expense_amount in expenses_summary[period].items():
                    summary_text += f"    {expense_name}: ${expense_amount}\n"

            if period in savings_summary:
                summary_text += f"  Savings: ${savings_summary[period]}\n"

            summary_text += "\n"

        return summary_text
# Save the generated summary to a text file
    def save_summary_to_file(self, filename):
        summary_text = self.generate_summary_text()
        try:
            with open(filename, "w") as file:
                file.write(summary_text)
            print("Summary saved successfully!")
        except Exception as e:
            print(f"Error occurred while saving the summary: {e}")

# Function to get user input as string
def get_user_input(message):
    return input(message)

# Function to get user input as float (handles invalid input)
def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            # Function to save data to a file
def save_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error occurred while saving the data: {e}")
# Function to read data from a file
def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error occurred while reading the data: {e}")
        return ""
# Main function to run the Personal Finance Tracker program
def main():
    budget_tracker = BudgetTracker()
    financial_summary = FinancialSummary(budget_tracker)

    periods = ["monthly", "weekly"]

    print("Welcome to Personal Finance Tracker!")
    while True:
         # Display menu and get user choice
        print("\nChoose an option:")
        print("1. Set Budget")
        print("2. Set Income")
        print("3. Set Expenses")
        print("4. Set Savings")
        print("5. Update Income")
        print("6. Update Expenses")
        print("7. Update Savings")
        print("8. Generate Summary")
        print("9. Save Summary to File")
        print("0. Exit")

        choice = int(get_user_input("Enter your choice: "))

        if choice == 1:
            period = get_user_input("Enter the period (monthly/weekly): ")
            amount = get_float_input("Enter the budget amount: ")
            if period in periods:
                budget_tracker.set_budget(period, amount)
                print(f"{period.capitalize()} budget set to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 2:
            period = get_user_input("Enter the period (monthly/weekly): ")
            amount = get_float_input("Enter the income amount: ")
            if period in periods:
                budget_tracker.set_income(period, amount)
                print(f"{period.capitalize()} income set to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 3:
            period = get_user_input("Enter the period (monthly/weekly): ")
            expense_name = get_user_input("Enter the expense name: ")
            amount = get_float_input("Enter the expense amount: ")
            if period in periods:
                budget_tracker.set_expenses(period, expense_name, amount)
                print(f"{period.capitalize()} {expense_name} expense set to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 4:
            period = get_user_input("Enter the period (monthly/weekly): ")
            amount = get_float_input("Enter the savings amount: ")
            if period in periods:
                budget_tracker.set_savings(period, amount)
                print(f"{period.capitalize()} savings set to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 5:
            period = get_user_input("Enter the period (monthly/weekly): ")
            amount = get_float_input("Enter the updated income amount: ")
            if period in periods:
                budget_tracker.update_income(period, amount)
                print(f"{period.capitalize()} income updated to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 6:
            period = get_user_input("Enter the period (monthly/weekly): ")
            expense_name = get_user_input("Enter the expense name to update: ")
            amount = get_float_input("Enter the updated expense amount: ")
            if period in periods:
                budget_tracker.update_expenses(period, expense_name, amount)
                print(f"{period.capitalize()} {expense_name} expense updated to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 7:
            period = get_user_input("Enter the period (monthly/weekly): ")
            amount = get_float_input("Enter the updated savings amount: ")
            if period in periods:
                budget_tracker.update_savings(period, amount)
                print(f"{period.capitalize()} savings updated to ${amount}")
            else:
                print("Invalid period. Choose either monthly or weekly.")

        elif choice == 8:
            summary_text = financial_summary.generate_summary_text()
            print(summary_text)

        elif choice == 9:
            filename = get_user_input("Enter the filename to save the summary (e.g., summary.txt): ")
            financial_summary.save_summary_to_file(filename)
             
        elif choice == 0:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


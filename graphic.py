import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from equipment_management_system import EquipmentManagementSystem


class EquipmentManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Equipment Management System")

        self.ems = EquipmentManagementSystem("equipment_management.db")

        self.label = tk.Label(master, text="Equipment Management System", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_room_button = tk.Button(master, text="Add Production Room", command=self.add_production_room)
        self.add_room_button.grid(row=1, column=0, padx=5, pady=5)

        self.add_equipment_button = tk.Button(master, text="Add Equipment Type", command=self.add_equipment_type)
        self.add_equipment_button.grid(row=1, column=1, padx=5, pady=5)

        self.add_contract_button = tk.Button(master, text="Add Equipment Contract", command=self.add_equipment_contract)
        self.add_contract_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.show_contracts_button = tk.Button(master, text="Show Contracts", command=self.show_contracts)
        self.show_contracts_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # checks added
    def add_production_room(self):
        description = simpledialog.askstring("Input", "Enter production room description:")
        while description == "":
            messagebox.showinfo("Failure", "Description cannot be empty.")
            description = simpledialog.askstring("Input", "Enter production room description:")

        equipment_area = simpledialog.askstring("Input", "Enter equipment area:")
        while equipment_area is None or not equipment_area.isnumeric() or float(equipment_area) <= 0:
            messagebox.showinfo("Failure", "Enter a positive number.")
            equipment_area = simpledialog.askstring("Input", "Enter equipment area:")

        self.ems.add_production_room(description, equipment_area)
        messagebox.showinfo("Success", "Production room added successfully.")

    # checks added
    def add_equipment_type(self):
        description = simpledialog.askstring("Input", "Enter equipment type description:")
        while description == "":
            messagebox.showinfo("Failure", "Description cannot be empty.")
            description = simpledialog.askstring("Input", "Enter equipment type description:")

        area = simpledialog.askstring("Input", "Enter equipment area:")
        while area is None or not area.isnumeric() or float(area) <= 0:
            messagebox.showinfo("Failure", "Enter a positive number.")
            area = simpledialog.askstring("Input", "Enter equipment area:")

        self.ems.add_equipment_type(description, area)
        messagebox.showinfo("Success", "Equipment type added successfully.")

    def add_equipment_contract(self):
        # check for the code existing
        # check if a number
        # check if such code exists
        production_code = simpledialog.askinteger("Input", "Enter production room code:")
        while production_code is None or production_code < 1 or not self.ems.check_production_room_code(production_code):
            messagebox.showinfo("Failure", "Enter an existing code.")
            production_code = simpledialog.askinteger("Input", "Enter production room code:")

        # check for the code existing
        # check if a number
        # check if such code exists
        equipment_type_code = simpledialog.askinteger("Input", "Enter equipment type code:")
        while equipment_type_code is None or equipment_type_code < 1 or not self.ems.check_equipment_type_code(equipment_type_code):
            messagebox.showinfo("Failure", "Enter an existing code.")
            equipment_type_code = simpledialog.askinteger("Input", "Enter equipment type code:")

        # check for the positive quantity
        quantity = simpledialog.askinteger("Input", "Enter quantity:")
        while quantity is None or int(quantity) <= 0:  # or not quantity.isnumeric()
            messagebox.showinfo("Failure", "Enter a positive number.")
            quantity = simpledialog.askstring("Input", "Enter quantity:")

        self.ems.add_equipment_contract(production_code, equipment_type_code, quantity)
        messagebox.showinfo("Success", "Equipment contract added successfully.")

    def show_contracts(self):
        contracts = self.ems.get_contracts()
        contract_text = "Contracts:\n"
        for contract in contracts:
            contract_text += f"Production: {contract[0]}, Equipment Type: {contract[1]}, Quantity: {contract[2]}\n"
        messagebox.showinfo("Contracts", contract_text)


def main():
    root = tk.Tk()
    app = EquipmentManagementApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

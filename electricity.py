import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        units = float(entry_units.get())
        
        # Calculate amount based on slab
        if units <= 100:
            amount = units * 1.5
        elif units <= 200:
            amount = (100 * 1.5) + (units - 100) * 2.5
        elif units <= 300:
            amount = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
        else:
            amount = (100 * 1.5) + (100 * 2.5) + (100 * 4) + (units - 300) * 5

        fixed_charge = 50
        total = amount + fixed_charge

        # Display the result
        result_text.set(f"Energy Charge: ₹{amount:.2f}\n"
                        f"Fixed Charge: ₹{fixed_charge}\n"
                        f"Total Bill Amount: ₹{total:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for units.")

# Create main window
root = tk.Tk()
root.title("Electricity Bill Estimator")
root.geometry("350x300")
root.config(bg="#e8f0fe")

# Title Label
tk.Label(root, text="Electricity Bill Estimator", font=("Arial", 14, "bold"), bg="#e8f0fe", fg="#0b3d91").pack(pady=10)

# Units Input
tk.Label(root, text="Enter Units Consumed:", font=("Arial", 12), bg="#e8f0fe").pack()
entry_units = tk.Entry(root, font=("Arial", 12), width=15, justify='center')
entry_units.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate Bill", command=calculate_bill, bg="#0b3d91", fg="white", font=("Arial", 12), width=15).pack(pady=10)

# Result Display
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="#e8f0fe", justify="center").pack(pady=10)

# Exit Button
tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", font=("Arial", 12), width=10).pack(pady=10)

root.mainloop()
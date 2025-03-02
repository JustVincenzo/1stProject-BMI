import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height, system):
    if system == "imperial":
        weight = weight * 0.453592  # Pounds to kg
        height = height * 2.54  # Inches to cm
    height_m = height / 100  # cm to m
    return weight / (height_m ** 2)

def classify_bmi(bmi, is_asian, age):
    if age < 18:
        return "BMI calculation may not be accurate for minors."
    if is_asian:
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 23:
            return "Normal weight"
        elif bmi < 27.5:
            return "Overweight"
        else:
            return "Obesity"
    else:
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

def calculate():
    try:
        age = int(entry_age.get())
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        is_asian = var_asian.get()
        follows_diet = var_diet.get()
        system = var_system.get()
        
        bmi = calculate_bmi(weight, height, system)
        classification = classify_bmi(bmi, is_asian, age)
        
        result = f"Your BMI is: {bmi:.2f}\nClassification: {classification}\n"
        result += "It is recommended to follow up with a nutrition specialist." if follows_diet else "Maintain a healthy lifestyle with a balanced diet and exercise."
        
        messagebox.showinfo("BMI Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x350")

# Labels and input fields
tk.Label(window, text="Age:").pack()
entry_age = tk.Entry(window)
entry_age.pack()

tk.Label(window, text="Weight:").pack()
entry_weight = tk.Entry(window)
entry_weight.pack()

tk.Label(window, text="Height:").pack()
entry_height = tk.Entry(window)
entry_height.pack()

var_system = tk.StringVar(value="metric")
tk.Radiobutton(window, text="Metric System (kg, cm)", variable=var_system, value="metric").pack()
tk.Radiobutton(window, text="Imperial System (lbs, in)", variable=var_system, value="imperial").pack()

var_asian = tk.BooleanVar()
tk.Checkbutton(window, text="I am of Asian descent", variable=var_asian).pack()

var_diet = tk.BooleanVar()
tk.Checkbutton(window, text="I follow or have followed a diet", variable=var_diet).pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate)
calculate_button.pack()

# Run window
window.mainloop()

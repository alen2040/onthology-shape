from owlready2 import *
import tkinter as tk
from tkinter import messagebox
# Load the ontology
onto = get_ontology("alan.math_shapes.owl").load()

# Define classes for geometric shapes (if not already defined in Protégé)
class Circle(Thing):
    namespace = onto

class Rectangle(Thing):
    namespace = onto

class Triangle(Thing):
    namespace = onto

# Define data properties (radius, base, height, etc.)
onto.Circle.has_radius = DataProperty(domain=[Circle], range=[float])
onto.Rectangle.has_length = DataProperty(domain=[Rectangle], range=[float])
onto.Rectangle.has_width = DataProperty(domain=[Rectangle], range=[float])
onto.Triangle.has_base = DataProperty(domain=[Triangle], range=[float])
onto.Triangle.has_height = DataProperty(domain=[Triangle], range=[float])

# Function to calculate the area
def calculate_area(shape, dimensions):
    if shape == "Circle":
        radius = dimensions.get("radius", 0)
        return 3.14159 * radius ** 2
    elif shape == "Rectangle":
        length = dimensions.get("length", 0)
        width = dimensions.get("width", 0)
        return length * width
    elif shape == "Triangle":
        base = dimensions.get("base", 0)
        height = dimensions.get("height", 0)
        return 0.5 * base * height
    else:
        return None

# UI Implementation
def calculate():
    shape = shape_var.get()
    dimensions = {}

    try:
        if shape == "Circle":
            dimensions["radius"] = float(entry_radius.get())
        elif shape == "Rectangle":
            dimensions["length"] = float(entry_length.get())
            dimensions["width"] = float(entry_width.get())
        elif shape == "Triangle":
            dimensions["base"] = float(entry_base.get())
            dimensions["height"] = float(entry_height.get())
        
        area = calculate_area(shape, dimensions)
        if area is not None:
            result_label.config(text=f"Area: {area:.2f}")
        else:
            messagebox.showerror("Error", "Unsupported shape selected.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def update_fields(*args):
    # Show/hide input fields based on selected shape
    for widget in [radius_frame, length_frame, width_frame, base_frame, height_frame]:
        widget.grid_forget()
    
    shape = shape_var.get()
    if shape == "Circle":
        radius_frame.grid(row=2, column=0, columnspan=2)
    elif shape == "Rectangle":
        length_frame.grid(row=2, column=0, columnspan=2)
        width_frame.grid(row=3, column=0, columnspan=2)
    elif shape == "Triangle":
        base_frame.grid(row=2, column=0, columnspan=2)
        height_frame.grid(row=3, column=0, columnspan=2)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Geometric Shape Area Calculator")

# Shape Selection
tk.Label(root, text="Select Shape:").grid(row=0, column=0)
shape_var = tk.StringVar(value="Circle")
shape_var.trace("w", update_fields)
tk.OptionMenu(root, shape_var, "Circle", "Rectangle", "Triangle").grid(row=0, column=1)

# Input Fields
radius_frame = tk.Frame(root)
tk.Label(radius_frame, text="Radius:").grid(row=0, column=0)
entry_radius = tk.Entry(radius_frame)
entry_radius.grid(row=0, column=1)

length_frame = tk.Frame(root)
tk.Label(length_frame, text="Length:").grid(row=0, column=0)
entry_length = tk.Entry(length_frame)
entry_length.grid(row=0, column=1)

width_frame = tk.Frame(root)
tk.Label(width_frame, text="Width:").grid(row=0, column=0)
entry_width = tk.Entry(width_frame)
entry_width.grid(row=0, column=1)

base_frame = tk.Frame(root)
tk.Label(base_frame, text="Base:").grid(row=0, column=0)
entry_base = tk.Entry(base_frame)
entry_base.grid(row=0, column=1)

height_frame = tk.Frame(root)
tk.Label(height_frame, text="Height:").grid(row=0, column=0)
entry_height = tk.Entry(height_frame)
entry_height.grid(row=0, column=1)

# Calculate Button
tk.Button(root, text="Calculate Area", command=calculate).grid(row=4, column=0, columnspan=2)
# Result Label
result_label = tk.Label(root, text="Area: ")
result_label.grid(row=5, column=0, columnspan=2)

# Update fields based on the default shape
update_fields()

# Run the UI loop
root.mainloop()
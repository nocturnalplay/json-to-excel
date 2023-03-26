import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
from function import converter as cv

# Create a new instance of Tkinter
root = tk.Tk()

# set the dimensions of the window
window_width = 600
window_height = 200

# get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the x and y coordinates to center the window
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

# set the position of the window to the center of the screen
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# set the window icon
# root.iconbitmap("JTE.ico")
root.title("JSON to EXCEL Converter")

# Define color scheme
bg_color = '#f0f0f0'
label_color = '#303030'
button_color = '#008CBA'
text_color = '#101010'

# Set background color of the root window
root.configure(bg=bg_color)

# Define a function to handle the "Open" button


def open_file():
    file_path = filedialog.askopenfilename()
    file_text.delete('1.0', tk.END)  # clear previous text
    file_text.insert('1.0', file_path)

# Define a function to handle the "Select Destination Folder" button


def select_folder():
    folder_path = filedialog.askdirectory()
    folder_text.delete('1.0', tk.END)  # clear previous text
    folder_text.insert('1.0', folder_path)

# Define a function to handle the "Submit" button


def submit_file():
    src_file_path = file_text.get(
        '1.0', tk.END).strip()  # get selected file path
    file_name = os.path.basename(src_file_path).split(".")  # get the file name

    # get selected destination folder path
    dst_folder_path = folder_text.get('1.0', tk.END).strip()
    number_row = input_field.get().strip()  # get selected number

    if len(number_row) == 0:
        messagebox.showwarning(
            "Warning", "Number of rows must be less than 1000000")
        return

    if int(number_row) > 1000000:
        messagebox.showwarning(
            "Warning", "Number of rows must be less than 1000000")
        return

    if src_file_path and dst_folder_path:
        if cv.Converter(root, src_file_path, file_name, dst_folder_path, int(number_row)):
            messagebox.showinfo(
                title="Success", message="The operation was successful.")
    else:
        messagebox.showwarning(
            "Warning", "Please select both source and destination file paths")


        # Create a label for the "Open" button
file_label = tk.Label(root, text="Select a source file:",
                      bg=bg_color, fg=label_color)
file_label.grid(row=0, column=0, pady=5, padx=5)

# Create a button widget to open file dialog
open_button = tk.Button(root, text="Select Source",
                        command=open_file, bg=button_color, fg='white')
open_button.grid(row=0, column=2, pady=5, padx=5)

# Create a text widget to display the selected file path
file_text = tk.Text(root, height=1, width=40, bg=bg_color, fg=text_color)
file_text.grid(row=0, column=1, pady=5, padx=5)

# ---------------------------------------------------------------------------------------------------

# Create a label for the "Select Destination Folder" button
folder_label = tk.Label(
    root, text="Select a destination folder:", bg=bg_color, fg=label_color)
folder_label.grid(row=1, column=0, pady=5, padx=5)

# Create a button widget to select the destination folder
folder_button = tk.Button(root, text="Select Folder",
                          command=select_folder, bg=button_color, fg='white')
folder_button.grid(row=1, column=2, pady=5, padx=5)

# Create a text widget to display the selected destination folder path
folder_text = tk.Text(root, height=1, width=40, bg=bg_color, fg=text_color)
folder_text.grid(row=1, column=1, pady=5, padx=5)

# ---------------------------------------------------------------------------------------------------

# Create a label for the "Select Destination Folder" button
number_of_rows_text = tk.Label(
    root, text="Select a Number of Rows:", bg=bg_color, fg=label_color)
number_of_rows_text.grid(row=3, column=0, pady=5, padx=5)

# Define a function to validate the input as an integer


def validate_integer(text):
    if text.isdigit():
        return True
    return False


# Create an input field for the integer value
input_field = tk.Entry(root, validate="key", validatecommand=(
    root.register(validate_integer), '%S'))
input_field.insert(0, "300000")
input_field.grid(row=3, column=1, pady=5, padx=5, sticky="W")

# Create a button widget to submit the selected file and copy it to the selected folder
submit_button = tk.Button(root, text="Convert",
                          command=submit_file, bg=button_color, fg='white')
submit_button.grid(row=4, column=1, pady=10, padx=5)

# Start the main loop
root.mainloop()

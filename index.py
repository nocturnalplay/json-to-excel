import tkinter as tk
from tkinter import filedialog
import shutil
import os

# Create a new instance of Tkinter
root = tk.Tk()
root.title("File Copier")

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
    file_text.delete('1.0', tk.END) # clear previous text
    file_text.insert('1.0', file_path)

# Define a function to handle the "Select Destination Folder" button
def select_folder():
    folder_path = filedialog.askdirectory()
    folder_text.delete('1.0', tk.END) # clear previous text
    folder_text.insert('1.0', folder_path)

# Define a function to handle the "Submit" button
def submit_file():
    src_file_path = file_text.get('1.0', tk.END).strip() # get selected file path
    file_name = os.path.basename(src_file_path) # get the file name
    dst_folder_path = folder_text.get('1.0', tk.END).strip() # get selected destination folder path
    dst_file_path = os.path.join(dst_folder_path, file_name) # create destination file path in the selected folder
    shutil.copy2(src_file_path, dst_file_path) # copy file to destination
    result_text.delete('1.0', tk.END) # clear previous text
    result_text.insert('1.0', f"File copied from {src_file_path} to {dst_file_path}")

# Create a label for the "Open" button
file_label = tk.Label(root, text="Select a file:", bg=bg_color, fg=label_color)
file_label.grid(row=0, column=0, pady=5, padx=5)

# Create a button widget to open file dialog
open_button = tk.Button(root, text="Open", command=open_file, bg=button_color, fg='white')
open_button.grid(row=0, column=1, pady=5, padx=5)

# Create a text widget to display the selected file path
file_text = tk.Text(root, height=1, width=50, bg=bg_color, fg=text_color)
file_text.grid(row=0, column=2, pady=5, padx=5)

# Create a label for the "Select Destination Folder" button
folder_label = tk.Label(root, text="Select a destination folder:", bg=bg_color, fg=label_color)
folder_label.grid(row=1, column=0, pady=5, padx=5)

# Create a button widget to select the destination folder
folder_button = tk.Button(root, text="Select Folder", command=select_folder, bg=button_color, fg='white')
folder_button.grid(row=1, column=1, pady=5, padx=5)

# Create a text widget to display the selected destination folder path
folder_text = tk.Text(root, height=1, width=50, bg=bg_color, fg=text_color)
folder_text.grid(row=1, column=2, pady=5, padx=5)

# Create a button widget to submit the selected file and copy it to the selected folder
submit_button = tk.Button(root, text="Copy File", command=submit_file, bg=button_color, fg='white')
submit_button.grid(row=2, column=1, pady=10, padx=5)

# Create a text widget to display the result of the copy operation
result_text = tk.Text(root, height=1, width=50)
result_text.grid(row=3, column=2, pady=5, padx=5)

# Start the main loop
root.mainloop()

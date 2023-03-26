import json
import pandas as pd
from tkinter import ttk
from time import sleep


def Converter(root, filename, output, dst_path, chunk_size=300000):
    try:
        # Open the JSON file and load the data
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

         # create a progress bar widget
        progress = ttk.Progressbar(
            root, orient="horizontal", length=300, mode="determinate")
        progress.grid(row=5, column=1, padx=10, pady=10)

        # create a label to display the percentage
        percentage_label = ttk.Label(root, text="0%")
        percentage_label.grid(row=5, column=2, padx=10, pady=10,sticky="W")

        chunks = [data[i:i + chunk_size]
                  for i in range(0, len(data), chunk_size)]

        # Convert each chunk to a Pandas DataFrame and save as an Excel file
        for i, chunk in enumerate(chunks):
            df = pd.DataFrame(chunk)
            filename = f'\{output[0]}_{i+1}.xlsx'
            df.to_excel(dst_path+filename, index=False)
            percentage = "{:.2f}%".format((i / len(chunks)) * 100)  # format the value as a percentage string with 2 decimal places
            percentage_label.config(text=percentage)  # update the text of the label with the new percentage value
            progress.step(100 / len(chunks))  # increment the progress bar by a certain amount)
            progress.update()

        percentage_label.destroy()
        progress.destroy()
        return True
    except Exception as e:
        print(e)

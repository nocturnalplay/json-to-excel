import json
import pandas as pd
import sys
from termcolor import colored

# filter the args value after the file name provided
args = sys.argv[1:]

# banner for the tool


def Banner():
    banner = colored('''
___________________________   __   _____            _____________  ________________________ 
______  /_  ___/_  __ \__  | / /   __  /______      ___  ____/_  |/ /_  ____/__  ____/__  / 
___ _  /_____ \_  / / /_   |/ /    _  __/  __ \     __  __/  __    /_  /    __  __/  __  /  
/ /_/ / ____/ // /_/ /_  /|  /     / /_ / /_/ /     _  /___  _    | / /___  _  /___  _  /___
\____/  /____/ \____/ /_/ |_/      \__/ \____/      /_____/  /_/|_| \____/  /_____/  /_____/                                                                                        
    ''', 'magenta')
    print(banner)

# helper function for the application


def Help():
    help_text = colored('''
The tool to convert the json data into excel with 
1M rows of data

[options]
   -l,--location  =  location of the json file
   -o,--output    =  output name looks like  
   --help         =  help for how to use the tool
   -q             =  not to show the banner
''', 'green')
    print(help_text)


# find the args length whether something provided in the args
if len(args) > 0:

    # if -q not in the args banner will be shown
    if "-q" not in args:
        Banner()

    # help option to show how to use the application
    if "--help" in args:
        Help()
        sys.exit(0)

    # file path and output text assignment
    path = ""
    output = "output"
    if "-o" in args or "--location" in args:
        output = args[args.index("-o")+1]
    if "-l" in args or "--output" in args:
        path = args[args.index("-l")+1]
    else:
        error_text = colored("use --help for options", 'red')
        print(error_text)
        sys.exit(1)

    # Open the JSON file and load the data
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    chunk_size = 300000

    if "-n" in args:
        chunk_size = int(args[args.index("-n")+1])
    # Split the data into chunks of 1 million rows or less

    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Convert each chunk to a Pandas DataFrame and save as an Excel file
    for i, chunk in enumerate(chunks):
        df = pd.DataFrame(chunk)
        filename = f'{output}_{i+1}.xlsx'
        df.to_excel(filename, index=False)
else:
    error_text = colored("use --help for options", 'red')
    print(error_text)
    sys.exit(1)

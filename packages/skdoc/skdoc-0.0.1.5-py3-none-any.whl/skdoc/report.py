import numpy as np
import pandas as pd
import papermill as pm
import tempfile
import subprocess
import webbrowser
import os

def render_report(
        dataframe: pd.DataFrame, 
        input_file = 'notebooks/report.qmd',
        type = 'quarto'):
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    dataframe.to_csv(temp_file.name, index=False)
    temp_file.close()

    temp_file_path = temp_file.name

    # Define the input file and output format
    params = f'path:{temp_file_path}'

    # Construct the command
    if type == 'quarto':
        command = f'quarto render {input_file} -P {params}'

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Render successful")
        os.remove(temp_file_path)
        print(result.stdout)
        
        # Open the resulting HTML file in the browser
        output_file = os.path.splitext(input_file)[0] + ".html"
        url = f'file://{os.path.abspath(output_file)}'
        webbrowser.open(url, new=2)  # Open in a new tab, if possible
    else:
        print("Render failed")
        os.remove(temp_file_path)
        print(result.stderr)

        
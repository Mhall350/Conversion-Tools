#!/usr/bin/env python3

import json

def json_to_txt(input_json_file, output_txt_file):
    """
    Convert a JSON file to a TXT file.
    
    Args:
        input_json_file (str): Path to the input JSON file
        output_txt_file (str): Path to the output TXT file
    """
    try:
        # Read the JSON file
        with open(input_json_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Write to the TXT file
        with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
            # You can customize how you want to write the data
            # Here we're using json.dumps for pretty printing
            txt_file.write(json.dumps(data, indent=4, ensure_ascii=False))
            
        print(f"Successfully converted {input_json_file} to {output_txt_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_json_file} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {input_json_file} contains invalid JSON.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_file = "input.json"  # Change this to your input JSON file
    output_file = "output.txt"  # Change this to your desired output TXT file
    json_to_txt(input_file, output_file)

import csv
import os

def extract_source_urls(input_filename):
    # Ensure the input file is looked for in the same folder as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_filename)
    output_path = os.path.join(script_dir, "source_urls.csv")

    if not os.path.exists(input_path):
        print(f"Error: File '{input_filename}' not found in {script_dir}")
        return

    with open(input_path, mode='r', encoding='utf-8') as infile, \
         open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['sourceURL'])  # CSV header

        for row in reader:
            if 'sourceURL' in row and row['sourceURL'].strip():
                writer.writerow([row['sourceURL'].strip()])
    
    print(f"✅ Extracted URLs written to: {output_path}")

# Replace with your actual CSV file name in the same folder
extract_source_urls("expanded_ai_services_list2.csv")

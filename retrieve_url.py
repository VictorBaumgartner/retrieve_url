import csv
import os

def extract_source_urls(input_filename):
    cwd = os.getcwd()
    input_path = os.path.join(cwd, input_filename)
    output_path = os.path.join(cwd, "source_urls.csv")

    with open(input_path, mode='r', encoding='utf-8') as infile, \
         open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['sourceURL']) 

        for row in reader:
            if 'sourceURL' in row and row['sourceURL'].strip():
                writer.writerow([row['sourceURL'].strip()])
    
    print(f"Extracted URLs written to: {output_path}")

extract_source_urls("expanded_ai_services_list2.csv")  
import csv
import os

def remove_duplicate_links(input_filename, output_filename="unique_links.csv", column_name="sourceURL"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_filename)
    output_path = os.path.join(script_dir, output_filename)

    seen = set()
    unique_rows = []

    with open(input_path, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if column_name not in fieldnames:
            print(f"Error: Column '{column_name}' not found in the CSV.")
            return

        for row in reader:
            url = row[column_name].strip()
            if url and url not in seen:
                seen.add(url)
                unique_rows.append(row)

    with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows)

    print(f"✅ Removed duplicates. Output saved to: {output_path}")

# Run the function on your CSV
remove_duplicate_links("source_urls.csv")  # or any CSV with links in "sourceURL" column

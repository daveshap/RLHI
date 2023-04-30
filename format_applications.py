import csv
import os

# Read CSV and filter rows with blank fields or 'n/a'
def read_and_filter_csv(file_path):
    filtered_rows = []
    with open(file_path, newline='', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if all(val.strip() and val.lower() != 'n/a' for val in row.values()):
                filtered_rows.append(row)
    return filtered_rows


# Generate HTML content
def generate_html_content(filtered_rows):
    if not filtered_rows:
        return ""

    html_content = ""
    for row in filtered_rows:
        name = row.pop("What is your real, full name?", None)
        row.pop("Timestamp", None)  # Remove Timestamp column

        question_answer_pairs = "".join([f"<p><b>{key}:</b><br>\t{row[key]}</p>" for key in row])

        html_content += f"""
        <div class="resume">
            <h1>{name}</h1>
            {question_answer_pairs}
        </div>
        <hr>
        """

    return html_content


# Main function
def main():
    input_file = 'input.csv'
    output_file = 'output.html'

    filtered_rows = read_and_filter_csv(input_file)
    html_content = generate_html_content(filtered_rows)
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Discord Group Applications</title>
            <style>
                body {{
                    font-family: Tahoma, sans-serif;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """)


if __name__ == "__main__":
    main()

def convert_csv(input_file, output_file):
    """Convert a CSV file with semicolons to commas."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            content = content.replace(';', ',')

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
    except Exception as e:
        print(f"Error occurred: {e}")

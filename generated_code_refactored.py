import pandas as pd

def get_unique_first_names(csv_file):
    """Reads CSV file and returns unique first names."""
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Extract unique values from the 'First Name' column and sort them in ascending order
        unique_first_names = sorted(df['First Name'].unique())

        return unique_first_names

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return []

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file}' is empty.")
        return []

    except pd.errors.ParserError as e:
        print(f"Error parsing the file '{csv_file}': {e}")
        return []

def save_unique_first_names(unique_first_names, csv_file):
    """Saves unique first names to a new CSV file."""
    if not unique_first_names:
        return

    try:
        # Save the unique first names to a new CSV file
        unique_first_names_df = pd.DataFrame({'First Name': unique_first_names})
        unique_first_names_df.to_csv(csv_file, index=False)

    except Exception as e:
        print(f"Error saving the file '{csv_file}': {e}")

def main():
    csv_file = 'data/customers-100000.csv'
    output_file = 'data/unique-first-names.csv'

    unique_first_names = get_unique_first_names(csv_file)
    save_unique_first_names(unique_first_names, output_file)

if __name__ == "__main__":
    main()
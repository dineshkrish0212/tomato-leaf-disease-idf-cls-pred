import os
import string

def clean_filename(filename):
    """Clean the filename by removing any trailing whitespace and non-printable characters."""
    # Strip whitespace and non-printable characters from the end
    return filename.rstrip(string.whitespace + string.printable)

def print_char_codes(filename):
    """Prints the Unicode code points of each character in the filename."""
    print(f"Character codes for '{filename}': {[ord(char) for char in filename]}")

def remove_trailing_whitespace_in_filenames(directory):
    # Walk through each folder, subfolder, and file in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            print(f"Checking file: '{filename}'")  # Debug: See if files are detected
            print_char_codes(filename)  # Print character codes
            
            # Clean the filename
            new_filename = clean_filename(filename)

            # Check if the filename actually has changed
            if new_filename != filename:  # Only rename if different
                old_file_path = os.path.join(root, filename)  # Full old path
                new_file_path = os.path.join(root, new_filename)  # Full new path
                
                # Check if the new file path already exists
                if not os.path.exists(new_file_path):
                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    # Print a message to confirm renaming
                    print(f"Renamed '{old_file_path}' to '{new_file_path}'")
                else:
                    print(f"File already exists, skipping: '{new_file_path}'")
            else:
                print(f"No trailing whitespace found for: '{filename}'")  # Debug: No rename

# Use a raw string for the path
extracted_folder_path = r'C:\Users\dines\Downloads\tomato'
remove_trailing_whitespace_in_filenames(extracted_folder_path)

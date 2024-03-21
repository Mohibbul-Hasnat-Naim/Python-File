import os

def remove_first_word_from_filenames(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        # Split the filename into words
        words = filename.split()

        # Remove the first word
        new_filename = ' '.join(words[1:])

        # Construct the new path
        new_path = os.path.join(folder_path, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"File '{old_path}' renamed to '{new_path}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
folder_path = "C:/Users/NSE Lab/Downloads/Video"

remove_first_word_from_filenames(folder_path)

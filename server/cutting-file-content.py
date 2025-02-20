import os

def delete_first_100_chars(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .md file
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            
            # Read the file content
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            x = content.find("Toggle Light / Dark / Auto color theme")
            if x == -1: x = 0
            # Delete the first 100 characters
            modified_content = content[:]
            
            # Write the modified content back to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(modified_content)
            
            print(f"Processed: {filename}")

# Example usage
if __name__ == "__main__":
    folder_path = "/Users/arnold/dev/cool/cmath/cmath/server/output/scraped"  # Replace with the path to your folder
    delete_first_100_chars(folder_path)
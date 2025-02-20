import os

def remove_otbroskov(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .md file
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            
            # Read the file content
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            x = content.find("Verifying you are human. This may take a few seconds.")
            if x != -1:
                print(f"Removed: {filename}")
                os.remove(f"/Users/arnold/dev/cool/cmath/cmath/server/output/scraped/{filename}")

# Example usage
if __name__ == "__main__":
    folder_path = "/Users/arnold/dev/cool/cmath/cmath/server/output/scraped"  # Replace with the path to your folder
    remove_otbroskov(folder_path)
import os
import re


def remove_links_from_markdown(folder_path):
    # Define regex patterns for different types of links
    patterns = [
        # Inline links: [text](url "title")
        re.compile(r'\[([^\]]+)\]\([^\)]+\)'),
        # Reference-style links: [text][id] or [id]: url "title"
        re.compile(r'\[([^\]]+)\]\[[^\]]+\]'),
        re.compile(r'^\[[^\]]+\]:\s*[^\s]+.*$', re.MULTILINE),
        # Bare URLs: https://example.com
        re.compile(r'https?://[^\s]+'),
        # Complex cases like your example
        re.compile(r'\[[^\]]+\]\(https://docs\.manim\.community[^\)]+\)'),
    ]

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .md file
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            
            # Read the file content
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Remove all link references using regex substitution
            for pattern in patterns:
                content = pattern.sub("", content)
            
            # Clean up extra spaces or empty lines
            content = re.sub(r'\n\s*\n', '\n\n', content)  # Remove empty lines
            content = content.strip()  # Remove leading/trailing whitespace
            
            # Write the modified content back to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            
            print(f"Processed: {filename}")

# Example usage
if __name__ == "__main__":
    folder_path = "/Users/arnold/dev/cool/cmath/cmath/server/output/structured/"  # Replace with the path to your folder
    remove_links_from_markdown(folder_path)
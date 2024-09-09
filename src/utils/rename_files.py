import os
import re

def rename_files(directory):
    pattern = re.compile(r'^(\d+)-([\w-]+)\.py$')
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.py'):
                match = pattern.match(filename)
                if match:
                    number, name = match.groups()
                    new_name = f"{number}_{name.replace('-', '_')}.py"
                    
                    if new_name != filename:
                        old_path = os.path.join(root, filename)
                        new_path = os.path.join(root, new_name)
                        os.rename(old_path, new_path)
                        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    base_directory = os.path.join("Python", "Hard")
    rename_files(base_directory)
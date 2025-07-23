import os
from typing import List, Dict

class FileSystemSimulator:
    def __init__(self, total_blocks: int):
        self.total_blocks = total_blocks
        self.bitmap = [0] * total_blocks  # 0 for free, 1 for occupied
        self.files = {}  # Stores file metadata
        self.directories = {"/": []}  # Root directory

    def allocate_blocks(self, size: int) -> List[int]:
        free_blocks = [i for i, b in enumerate(self.bitmap) if b == 0]
        if len(free_blocks) < size:
            return []
        allocated = free_blocks[:size]
        for block in allocated:
            self.bitmap[block] = 1
        return allocated

    def create_file(self, name: str, size: int, directory: str = "/"):
        if name in self.files or directory not in self.directories:
            return f"Error: File or directory already exists."
        blocks = self.allocate_blocks(size)
        if not blocks:
            return f"Error: Not enough space to create file {name}."
        self.files[name] = {
            "size": size,
            "blocks": blocks,
            "directory": directory
        }
        self.directories[directory].append(name)
        return f"File {name} created with blocks {blocks}."

    def delete_file(self, name: str):
        if name not in self.files:
            return f"Error: File {name} does not exist."
        file_info = self.files[name]
        for block in file_info["blocks"]:
            self.bitmap[block] = 0
        self.directories[file_info["directory"]].remove(name)  # Fixed this line
        del self.files[name]
        return f"File {name} deleted."

    def create_directory(self, path: str):
        if path in self.directories:
            return f"Error: Directory {path} already exists."
        parent_dir = os.path.dirname(path) or "/"  # Root directory if path is "/"
        if parent_dir not in self.directories:
            return f"Error: Parent directory {parent_dir} does not exist."
        self.directories[path] = []
        self.directories[parent_dir].append(path)
        return f"Directory {path} created."

    def list_directory(self, path: str):
        if path not in self.directories:
            return f"Error: Directory {path} does not exist."
        return self.directories[path]

    def show_bitmap(self):
        return self.bitmap

    def show_files(self):
        return self.files

# Example Usage
fs = FileSystemSimulator(total_blocks=100)
print(fs.create_directory("/docs"))
print(fs.create_file("file1.txt", 10, "/docs"))
print(fs.create_file("file2.txt", 20, "/docs"))
print(fs.list_directory("/docs"))
print(fs.show_bitmap())
print(fs.delete_file("file1.txt"))
print(fs.show_bitmap())
print(fs.show_files())

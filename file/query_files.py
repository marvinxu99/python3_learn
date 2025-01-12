import os
from datetime import datetime, timedelta

def run_test():
    # Query for files with a specified attribute or name
    start_folder = r"E:\eDev\HGW\csharp\learning"
    # Or
    # start_folder = "/usr/local/share/dotnet/sdk"

    # Get a list of all files in the directory and its subdirectories
    file_list = []
    for root, _, files in os.walk(start_folder):
        for file in files:
            if file.endswith(('.txt', '.cs')):
                file_path = os.path.join(root, file)
                file_info = {
                    "name": file,
                    "path": file_path,
                    "creation_time": datetime.fromtimestamp(os.path.getctime(file_path)),
                    "last_write_time": datetime.fromtimestamp(os.path.getmtime(file_path))
                }
                file_list.append(file_info)

    # Sort files by name
    file_query = sorted(file_list, key=lambda f: f["name"])

    # Uncomment this block to see the full query
    for file_info in file_query:
        print(file_info["path"])

    # Get the name of the newest file
    newest_file = max(file_query, key=lambda f: f["creation_time"])
    print(f"\nThe newest file is {newest_file['path']}. Creation time: {newest_file['creation_time']}")

    # Get files created or updated in the last 12 hours
    updated_files = [
        f for f in file_query
        if f["last_write_time"] > datetime.now() - timedelta(hours=12)
    ]
    # Sort files by name
    updated_files_sorted = sorted(updated_files, key=lambda f: f["last_write_time"])

    # Print files created in the last 12 hours
    print("\nFiles created or updated in the last 12 hours:")
    for file_info in updated_files_sorted:
        print(file_info["path"])


# Run the function
if __name__ == "__main__":
    run_test()

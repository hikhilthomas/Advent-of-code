import os


def generate_file_name(directory: str, filename: str) -> str:
    # Get the directory of the current script
    script_dir = os.path.dirname(directory)

    # Build the full path to the file
    file_path = os.path.join(script_dir, filename)

    return file_path

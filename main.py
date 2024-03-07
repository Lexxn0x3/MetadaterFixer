import os
from datetime import datetime
from PIL import Image
from moviepy.editor import VideoFileClip
import sys
import re
import ffmpeg

def modify_image_metadata(file_path, new_date):
    try:
        with Image.open(file_path) as img:
            if "exif" in img.info:
                exif_data = img.info["exif"]
                img.save(file_path, exif=exif_data)
    except Exception as e:
        print(f"Error modifying metadata for {file_path}: {e}", file=sys.stderr)


def modify_os_creation_date(file_path, new_date):
    try:
        # Modify the last modification and access times
        os.utime(file_path, (new_date.timestamp(), new_date.timestamp()))
    except Exception as e:
        print(f"Error modifying OS creation date for {file_path}: {e}", file=sys.stderr)


def process_files(directory, date_format, pattern):
    for filename in os.listdir(directory):
        match = re.search(pattern, filename)

        if match:
            date_str = match.group()
            date_object = datetime.strptime(date_str, date_format)
            print("Extracted Date:", date_object)
            try:
                # file_date = datetime.strptime(filename, date_format)
                # print(file_date)
                file_path = os.path.join(directory, filename)

                if filename.lower().endswith('.jpg'):
                    modify_image_metadata(file_path, date_object)

                modify_os_creation_date(file_path, date_object)

                print(f"Modified metadata for {filename}")
            except ValueError:
                # If the filename does not match the date format, skip it
                continue
        else:
            print("No date found in filename.")



# Example usage:
directory = "D:\\Downloads\\Telegram Desktop"
date_format = "%Y-%m-%d_%H-%M-%S"
pattern = r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}"
process_files(directory, date_format, pattern)

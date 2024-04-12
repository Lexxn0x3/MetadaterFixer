# MetaFixer: Metadata Correction Utility 🛠️

## 🌟 Description
MetaFixer is a Python utility designed to correct metadata of files downloaded from various messaging and social media platforms, ensuring accurate organization and archival. It focuses on JPEG images and MP4 videos, common file formats exchanged over these platforms. MetaFixer extracts date and time information embedded in filenames and updates the files' metadata accordingly. 📅🕒

## 🚀 Key Features
- 📸 **JPEG & MP4 Support**: Dandling photos and videos
- 🕵️‍♂️ **Smart Date Parsing**: From human-readable dates to Unix timestamps
- 📅 **Metadata Makeover**: Updates your files' metadata to ensure the "date created" actually reflects when it was really created or shared.
- 👌 **User-Friendly**

## Getting Started 🚀

### Prerequisites 📋

- Python 3.6 or higher 🐍
- Pillow library for image processing 🖼️
- moviepy library for video processing 🎥
- ffmpeg for video file metadata manipulation (Ensure ffmpeg is installed and added to your system's PATH) 🎞️

### Installation 📥

1. Clone the MetaFixer repository to your local machine:

```bash
git clone https://github.com/Lexxn0x3/MetadaterFixer.git
```

2. Navigate to the MetaFixer directory:

```bash
cd MetaFixer
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Usage 🛠️

1. Prepare your files in a directory. Ensure the filenames contain the date and time information in a recognizable pattern. 📁

2. Open `MetaFixer.py` and edit the `directory`, `date_format`, and `pattern` variables to match your setup:
    - `directory`: The path to the directory containing your files. 📂
    - `date_format`: The format in which the date and time are embedded in your filenames (e.g., "%Y-%m-%d_%H-%M-%S"). 📆
    - `pattern`: A regular expression pattern that matches the date and time in your filenames. 🔍

3. Run the script:

```bash
python MetaFixer.py
```

### Defining a Pattern Using Regular Expressions 🧩

Regular expressions (regex) are used to identify the specific part of the filename that contains the date and time information. Defining an appropriate regex pattern is crucial for the script to correctly extract and utilize this information.

- For filenames with dates in the format `YYYY-MM-DD_HH-MM-SS`, you can use the following pattern:

```python
pattern = r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}"
```

- This pattern specifically matches strings that follow the `YYYY-MM-DD_HH-MM-SS` format, where:
    - `\d{4}` matches a four-digit year. 📅
    - `\d{2}` matches a two-digit month, day, hour, minute, or second. ⏲️

Adjust the `pattern` variable in the script to match the format used in your filenames. This flexibility allows MetaFixer to work with a wide range of date and time formats embedded within filenames.

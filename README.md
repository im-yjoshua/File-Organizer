﻿
# File Organizer

This script organizes files in a directory into subdirectories based on their file types (e.g., documents, images, videos).

## Features
- Organizes C++ files (`.cpp`) into `C++ Files` directory
- Organizes image files (`.jpg`, `.png`) into `Images` directory
- Organizes audio files (`.mp3`) into `Audio Files` directory
- Organizes video files (`.mp4`, `.m4a`) into `Videos` directory
- Organizes text files (`.txt`) into `Text Files` directory

## Usage

1. Clone the repository or download the script file.
2. Navigate to the directory containing the script.
3. Run the script using Python.

```sh
python file_organizer.py
```
## Example
If you have the following files in your directory:
```css
script.py
project.cpp
photo.jpg
song.mp3
video.mp4
note.txt
```
After running the script, your directory will be organized as follows:
```
Python Files/
    script.py
C++ Files/
    project.cpp
Images/
    photo.jpg
Audio Files/
    song.mp3
Videos/
    video.mp4
Text Files/
    note.txt
```

## Error Handling
The script includes error handling for:

- File not found errors
- Permission errors
- Other general exceptions
If any error occurs during the file moving process, a relevant message will be printed to the console.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

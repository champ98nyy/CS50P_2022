# CS50P 2022 - PSET 1
# File Extensions

"""
Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name.
For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your
computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download
a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type
for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s
extension, mapping one to the other.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s
name ends, case-insensitively, in any of these suffixes:
    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

# Request user input, remove leading/trailing spaces, convert string to all lowercase, split input on ".", then assign to filename variable
filename = input("File name: ").strip().lower().split(".")

# Assign the last item in the filename list to the extension variable
extension = filename[-1]

# Create a dict mapping extensions to file types
types = {"gif": "image/gif", "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "pdf": "application/pdf", "txt": "text/plain", "zip": "application/zip"}

# Try printing the value of the extension key. If it doesn't exist in the types dict (KeyError), print default file type ("application/octet-stream")
try:
    print(types[extension])
except(KeyError):
    print("application/octet-stream")
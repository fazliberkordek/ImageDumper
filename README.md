# ImageDumper
ImageDumper

ImageDumper is a Python-based desktop application that allows users to easily resize and convert images. It provides several options for resizing images, including resizing by percentage, width, height, and file size. The app supports multiple output formats, including PNG, JPG, BMP, and WebP.

Features:
	•	Select an Image: Choose an image file from your local machine.
	•	Resize Options:
	•	By Percentage: Resize the image based on a percentage.
	•	By Width: Resize the image to a specific width (height is adjusted proportionally).
	•	By Height: Resize the image to a specific height (width is adjusted proportionally).
	•	By File Size: Resize the image to meet a target file size (in KB or MB).
	•	Save in Multiple Formats: Save the resized image in PNG, JPG, BMP, or WebP formats.

Requirements
	•	Python 3.x (Python 3.6 or later recommended)
	•	Pillow: Python Imaging Library (PIL), used to handle image processing.

Installing Dependencies:

To install the required dependencies, you can use pip:

```bash
pip3 install pillow
```
How to Use
	1.	Run the application:
	•	After installing dependencies, run the script with the following command:
```bash
python3 imagedumper.py
```
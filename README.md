# Photo_to_Cartoon_with_Pencilsketch
### My simple photo to cartoon with pencil sketch using image processing

This Python code uses the OpenCV library to convert an input image into a cartoon-like image with a pencil-sketch effect. The code applies various image processing techniques such as median blur, adaptive thresholding, bilateral filtering, bitwise operations, and pencil-sketch effect to achieve the cartoon-like effect.

## Requirements

1.  Python 3
2.  OpenCV library (cv2)
3.  NumPy library (numpy)

## Getting Started

To use this code, you need to have Python and OpenCV installed on your system.

## How to use

1.  Clone this repository to your local machine or download the ZIP file.
2.  Open the command prompt and navigate to the directory where the code is located.
3.  Replace the input image with your own image by changing the filename in the cv2.imread() function.
4.  Run the script using the command "python Photo_to_cartoon.py".
5.  The output will be displayed on the screen with the original and cartoon images side by side.

## Comparison of my code with ChatGPT's code

The chatGPT's code performs the following steps:
1.  Load the image.
2.  Convert the image to grayscale.
3.  Apply median blur to reduce noise.
4.  Detect edges using adaptive thresholding.
5.  Convert the image to color.
6.  Apply bilateral filter to preserve edges while reducing noise.
7.  Combine the color image with the edges mask.
8.  Display the cartoon image.

<img width="1243" alt="Screen Shot 2023-03-21 at 4 08 53 PM" src="https://user-images.githubusercontent.com/126442096/226538899-dd69a2b6-113c-446e-8c08-d5b86b7a7170.png">

Here is the result of the code by ChatGPT.

My upgraded code performs the following steps:
1.  Load the image.
2.  Convert the image to grayscale.
3.  Apply median blur to smooth the image.
4.  Detect edges using adaptive thresholding.
5.  Apply bilateral filter to preserve edges while reducing noise.
6.  Add a solid color background.
7.  Create a mask for the edges.
8.  Apply the mask to the background image.
9.  Apply the mask to the color image.
10. Add a sketch effect.
11. Combine the edge-detected image with the color image and sketch effect.
12. Increase contrast and brightness.
13. Display the original and cartoon images side by side.
<img width="1243" alt="Screen Shot 2023-03-21 at 4 09 52 PM" src="https://user-images.githubusercontent.com/126442096/226539027-c3573296-dc03-43dd-b7d3-f1cf8eb44254.png">

Here is the result of my upgraded code.

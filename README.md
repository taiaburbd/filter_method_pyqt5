# Overview
The project aims to create an image processing application using PyQt5 that allows users to open an image, apply a spatial filter of their choice, and display both the input and output images. The user can select the image to use by browsing their system through a user interface.

The application provides different filter options, including average smoothing, Gaussian, Laplacian, Sobel, and Roberts. If the filter requires a kernel size, the user can provide it through a spin box.

One important note is that the input image should be converted to grayscale as soon as the program starts to ensure that the filter is applied to the image's intensity values rather than its color values.

Overall, this project provides a simple and user-friendly interface for performing basic image processing tasks, allowing users to experiment with different filter options and kernel sizes to achieve the desired output.

# Requirment
- [ ] Create a project to open an image, filter it with some spatial filter that you can choose by the user interface, and show both, input and output images.
- [ ] The image to use should be chosen by the user, by suing the interface.
- [ ] Ideas of filters: average smoothing, gaussian, laplacian, sober, Roberts.
- [ ] When the filter can have different sizes, this value should be provided by the user.

# Application screenshot
![app screenshot](/application.png)

# Application Templete 
<a href="https://github.com/joako1991/MaIAWinterSchoolPyQt5">MaIAWinterSchoolPyQt5</a>

# PyQt5
<a href="https://doc.qt.io/qtforpython/">Documentation</a>
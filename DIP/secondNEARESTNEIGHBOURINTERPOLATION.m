clc;
clear all;
close all;

% Define image dimensions
width = 300;  
height = 200;  

% Create an RGB image matrix
rgbImage = zeros(height, width, 3, 'uint8');

% Fill the first third of rows with red
rgbImage(1:height/3, :, 1) = 255;

% Fill the second third of rows with green
rgbImage((height/3 + 1):(2*height/3), :, 2) = 255;

% Fill the last third of rows with blue
rgbImage((2*height/3 + 1):height, :, 3) = 255;

% Display the image
imshow(rgbImage);

% Save the image (optional)
imwrite(rgbImage, 'rgb_image_rows.png');

% Rotate the image by 45 degrees
rotatedImage = imrotate(rgbImage, 45, 'bilinear', 'crop');

% Display the rotated image
figure;
imshow(rotatedImage);
title('Rotated Image to 45 degree');

% Rotate the image by 60 degrees
rotatedImage = imrotate(rgbImage, 60, 'bilinear', 'crop');

% Display the rotated image
figure;
imshow(rotatedImage);
title('Rotated Image to 60 degree');

% Save the rotated image (optional)
imwrite(rotatedImage, 'rotated_rgb_image.png');

% Increase the size by a factor of 2 using nearest-neighbor interpolation
resizedImage = imresize(rotatedImage, 2, 'nearest');

% Display the resized image
figure;
imshow(resizedImage);
title('Resized Image (Nearest Neighbor)');

% Save the resized image (optional)
imwrite(resizedImage, 'resized_rgb_image.png');

% Increase the size by a factor of 2 using bilinear interpolation
resizedImageBilinear = imresize(rotatedImage, 2, 'bilinear');

% Display the resized image using bilinear interpolation
figure;
imshow(resizedImageBilinear);
title('Resized Image (Bilinear)');

% Save the resized image (optional)
imwrite(resizedImageBilinear, 'resized_rgb_image_bilinear.png');

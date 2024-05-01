clc;
clear all;
close all;

% Load the image from an external source
image_url = 'https://classroomclipart.com/image/static7/preview1/happy-bear-reading-a-red-book-61363.jpg';
image_matrix = imread(image_url);

% Check if the image is RGB, if so, convert it to grayscale
if size(image_matrix, 3) == 3
    image_matrix = rgb2gray(image_matrix);
end

% Extract intensity values and compute their occurrences
intensity_values = image_matrix(:);
counts = zeros(1, 256);
for i = 0:255
    counts(i+1) = sum(intensity_values == i);
end

% Display the original image
figure;
subplot(1, 2, 1);
imshow(image_matrix);
title('Original Image');

% Plot the histogram
subplot(1, 2, 2);
bar(0:255, counts);
xlabel('Intensity Value');
ylabel('Number of Occurrences');
title('Histogram');
grid on;

% Save the original image without the path
imwrite(image_matrix, 'original_image.jpg');

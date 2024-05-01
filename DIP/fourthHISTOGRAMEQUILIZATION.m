clc
clear all
close all
%https://wallpapercave.com/wp/wp4430599.jpg
image_path = 'https://classroomclipart.com/image/static7/preview1/happy-bear-reading-a-red-book-61363.jpg';
image_matrix = imread(image_path);
if size(image_matrix, 3) == 3
    image_matrix = rgb2gray(image_matrix);
end

intensity_values = image_matrix(:);
counts = zeros(1, 256);

for i = 0:255
    counts(i+1) = sum(intensity_values == i);
end

% Display the original image
figure;
subplot(2, 2, 1);
imshow(image_matrix);
title('Original Image');

% Plotting the original histogram
subplot(2, 2, 2);
bar(0:255, counts);
xlabel('Intensity Value');
ylabel('Number of Occurrences');
title('Original Histogram');
grid on;

% Compute cumulative distribution function (CDF)
cdf = cumsum(counts) / numel(intensity_values);

% Perform histogram equalization
equalized_image = uint8(255 * cdf(image_matrix + 1));

% Compute the histogram of the equalized image
equalized_counts = zeros(1, 256);
for i = 0:255
    equalized_counts(i+1) = sum(equalized_image(:) == i);
end

% Display the equalized image
subplot(2, 2, 3);
imshow(equalized_image);
title('Equalized Image');

% Plotting the equalized histogram
subplot(2, 2, 4);
bar(0:255, equalized_counts);
xlabel('Intensity Value');
ylabel('Number of Occurrences');
title('Equalized Histogram');
grid on;

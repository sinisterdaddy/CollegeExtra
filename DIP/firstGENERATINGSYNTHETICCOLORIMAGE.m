clc
close all
clear all
% Create a random matrix of size 1024x1024 with elements in the range [0, 255]
random_matrix = uint8(randi([0, 255], 1024, 1024));

% Display the random matrix
imshow(random_matrix, []);
title('Random Matrix (1024x1024)');

% Extract the (256, 300) column pixel values
column_values = random_matrix(:, 300);

% Display the extracted column values
figure;
plot(column_values);
title('Pixel values in column (256, 300)');
xlabel('Row index');
ylabel('Pixel value');

% Extract the region of interest (100, 100, 500, 500) from the random matrix
roi = random_matrix(100:500, 100:500);

% Display the extracted region of interest as an image
figure;
imshow(roi, []);
title('Extracted Region of Interest (100, 100, 500, 500)');
% Specify the size of the matrix
rows = 1024;
columns = 1024;

% Initialize the matrix with zeros
a= zeros(rows, columns);

% Fill the matrix with the desired pattern
for i = 1:255
    a(:, (i-1)*4+1:i*4) = i-1;
end
% Set the last column in each row to 255
a(:, end) = 255;

% Display the matrix
disp(a);
% Specify the size of the matrix
rows = 1024;
columns = 1024;

% Initialize the matrix with zeros
b = zeros(rows, columns);

% Fill the matrix with the desired pattern for columns
for i = 1:255
    b(:, (i-1)*4+1:i*4) = i-1;
end

% Set the last column in each row to 255
b(:, end) = 255;

% Fill the matrix with the desired pattern for rows
for i = 1:255
    b((i-1)*4+1:i*4, :) = i-1;
end

% Set the last row in each column to 255
b(end, :) = 255;

% Display the matrix
disp(b);

% Specify the size of the matrix
rows = 1024;
columns = 1024;

% Initialize the matrix with zeros
c = zeros(rows, columns);

% Fill the lower part with even numbers starting from 0
for i = 1:rows
    for j = 1:i-1
        c(i, j) = mod((j-1)*2, 256);
    end
end

% Fill the upper part with odd numbers starting from 1
for i = 1:rows
    for j = i+1:columns
        c(i, j) = mod(j*2-1, 256);
    end
end

% Set the diagonal to consecutive values from 0 to 255 using a loop
for i = 1:rows
    c(i, i) = mod((i-1), 256);
end

% Display the matrix
disp(c);
% Display matrix a
figure;
imshow(a, []);
title('Matrix a');

% Display matrix b
figure;
imshow(b, []);
title('Matrix b');

% Display matrix c
figure;
imshow(c, []);
title('Matrix c');
% Assuming a, b, and c are matrices of the same size (1024x1024)
rows = 1024;
columns = 1024;

% Create an RGB image
rgb_image = cat(3, mat2gray(a), mat2gray(b), mat2gray(c));
% Display the RGB image
figure;
imshow(rgb_image);
title('Combined RGB Image');

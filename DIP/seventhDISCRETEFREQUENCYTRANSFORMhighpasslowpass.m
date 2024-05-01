clc;
close all;
clear all;

% (a).
% ideal high pass frequency

% Reading input color image
color_image = imread('bird_color_image.jpg'); 

% Convert color image to grayscale
gray_image = rgb2gray(color_image);

% Saving the size of the gray_image in pixels
[M, N] = size(gray_image); 

% Getting Fourier Transform of the gray_image 
FT_img_high = fft2(double(gray_image)); 

% Assign Cut-off Frequency 
D0_high = 10; % You can change this value accordingly 

% Designing high pass filter 
u = 0:(M-1); 
idx = find(u>M/2); 
u(idx) = u(idx)-M; 
v = 0:(N-1); 
idy = find(v>N/2); 
v(idy) = v(idy)-N; 

% MATLAB library function meshgrid(v, u) returns 2D grid 
% which contains the coordinates of vectors v and u. 
% Matrix V with each row is a copy of v, and matrix U 
% with each column is a copy of u 
[V, U] = meshgrid(v, u); 

% Calculating Euclidean Distance 
D_high = sqrt(U.^2+V.^2); 

% Comparing with the cut-off frequency and 
% determining the filtering mask 
H_high = double(D_high > D0_high); 

% Convolution between the Fourier Transformed image and the mask 
G_high = H_high.*FT_img_high; 

% Getting the resultant image by Inverse Fourier Transform 
% of the convoluted image using MATLAB library function 
% ifft2 (2D inverse fast fourier transform) 
filtered_gray_image_high = real(ifft2(double(G_high))); 

% Displaying Input Image
figure;
imshow(color_image);
title('Original Color Image');

% Displaying Grayscale Image
figure;
imshow(gray_image);
title('Grayscale Image (f(x,y))');

% Displaying Fourier Transform of the Grayscale Image
figure;
imshow(log(1 + abs(fftshift(FT_img_high))), []);
title('Fourier Transform of Grayscale Image (F(u,v)) (Highpass)');

% Displaying Ideal Highpass Filter
figure;
imshow(H_high, []);
title('Ideal Highpass Filter (H(u,v))');

% Displaying Filtered Frequency Domain Image (Highpass)
figure;
imshow(log(1 + abs(fftshift(G_high))), []);
title('Filtered Frequency Domain Image (G(u,v)) (Highpass)');

% Displaying Filtered Image in Spatial Domain (Highpass)
figure;
imshow(filtered_gray_image_high, []);
title('Filtered Grayscale Image (g(x,y)) (Highpass)');


% (b).
% ideal low pass frequency

% Assign Cut-off Frequency for Low Pass Filter
D0_low = 30; % You can change this value accordingly 

% Designing low pass filter 
H_low = double(D_high <= D0_low); 

% Convolution between the Fourier Transformed image and the mask 
G_low = H_low.*FT_img_high; 

% Getting the resultant image by Inverse Fourier Transform 
% of the convoluted image using MATLAB library function 
% ifft2 (2D inverse fast fourier transform) 
filtered_gray_image_low = real(ifft2(double(G_low))); 

% Getting Fourier Transform of the filtered low pass image
FT_img_low = fft2(filtered_gray_image_low);

% Displaying Fourier Transform of the Grayscale Image (Lowpass)
figure;
imshow(log(1 + abs(fftshift(FT_img_low))), []);
title('Fourier Transform of Grayscale Image (F(u,v)) (Lowpass)');

% Displaying Ideal Lowpass Filter
figure;
imshow(H_low, []);
title('Ideal Lowpass Filter (H(u,v))');

% Displaying Filtered Frequency Domain Image (Lowpass)
figure;
imshow(log(1 + abs(fftshift(G_low))), []);
title('Filtered Frequency Domain Image (G(u,v)) (Lowpass)');

% Displaying Filtered Image in Spatial Domain (Lowpass)
figure;
imshow(filtered_gray_image_low, []);
title('Filtered Grayscale Image (g(x,y)) (Lowpass)');

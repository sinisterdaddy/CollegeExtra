clc;
close all;
clear all;

% (1).
% Perform inverse filter 
% take input image
% perform degradation that is blur (11x11)
% get G(x,y)
% blur the image
% restore image
% outputs are inputimage, blur image, G(x,y), blur, restored image


% Read input image (color)
I_color = imread('bird_color_image.jpg');

% Convert color image to grayscale
I_gray = rgb2gray(I_color);
I_gray = im2double(I_gray);

% Perform degradation: Apply blur (11x11 Gaussian kernel)
blurKernel = fspecial('gaussian', 11, 11);
blurredImage = imfilter(I_gray, blurKernel, 'same');

% Obtain G(x,y): Compute the frequency response of the blur kernel
G_xy = fft2(blurKernel, size(I_gray, 1), size(I_gray, 2));

% Display the input image, blurred image, and G(x,y)
figure;
subplot(2, 4, 1), imshow(I_gray), title('Input Image');
subplot(2, 4, 2), imshow(blurredImage), title('Blurred Image');
subplot(2, 4, 3), imagesc(abs(fftshift(G_xy))), colormap('gray'), title('Frequency Response (G(x,y))');
subplot(2, 4, 4), imagesc(blurKernel), colormap('gray'), title('Blur Kernel (11x11)');

% Restore the image using inverse filtering
restoredImage = ifft2(fft2(blurredImage) ./ G_xy);

% Display the restored image
subplot(2, 4, [5, 6, 7, 8]), imshow(abs(restoredImage), []), title('Restored Image with Inverse Filtering');

clc;
close all;
clear all;

% (2).
% Perform Pseudo inverse filter 
% take input image
% perform degradation that is blur (11x11)
% get G(x,y)
% blur the image
% restore image
% outputs are inputimage, blur image, G(x,y), blur, restored image
% Read input image (color)
I_color = imread('bird_color_image.jpg');

% Convert color image to grayscale
I_gray = rgb2gray(I_color);
I_gray = im2double(I_gray);

% Perform degradation: Apply blur (11x11 Gaussian kernel)
blurKernel = fspecial('gaussian', 11, 11);
blurredImage = imfilter(I_gray, blurKernel, 'same');

% Obtain G(x,y): Compute the frequency response of the blur kernel
G_xy = fft2(blurKernel, size(I_gray, 1), size(I_gray, 2));

% Display the input image and the blurred image
figure;
subplot(2, 4, 1), imshow(I_gray), title('Input Image');
subplot(2, 4, 2), imshow(blurredImage), title('Blurred Image');

% Calculate the pseudo-inverse filter
epsilon = 0.01; % Small value to avoid division by zero
H_pseudo_inverse = conj(G_xy) ./ (abs(G_xy).^2 + epsilon);

% Restore the image using pseudo-inverse filtering
restoredImage = ifft2(fft2(blurredImage) .* H_pseudo_inverse);

% Display G(x,y) and blur kernel
subplot(2, 4, 3), imagesc(abs(fftshift(G_xy))), colormap('gray'), title('Frequency Response (G(x,y))');
subplot(2, 4, 4), imagesc(blurKernel), colormap('gray'), title('Blur Kernel (11x11)');

% Display the restored image
subplot(2, 4, [5, 6, 7, 8]), imshow(abs(restoredImage), []), title('Restored Image with Pseudo Inverse Filtering');





For pseudo inverse filter with different epsilon values.
clc;
close all;
clear all;

% (3).
% Perform Pseudo inverse filter for different epsilons 
% Additive White Gaussian Noise(AWGN) is used for noise
% take input image
% perform degradation that is blur (11x11)
% get G(x,y)
% blur the image
% restore image
% outputs are inputimage, blur image, G(x,y), blur, restored image

% Load and display the input image
inputImage = imread('bird_color_image.jpg');

% Define the degradation kernel (11x11 blur)
blurKernel = fspecial('gaussian', [11, 11], 2);

% Perform degradation (blur) on the input image
blurredImage = imfilter(inputImage, blurKernel, 'conv', 'same', 'replicate');

% Add AWGN to the blurred image
SNR = 80; % Signal-to-Noise Ratio (adjust as needed)
blurredImageWithNoise = imnoise(blurredImage, 'gaussian', 0, (std2(blurredImage) / SNR)^2);

% Compute the pseudo-inverse filter (Wiener deconvolution)
psf = fspecial('gaussian', [11, 11], 2); % Point Spread Function (PSF)
estimatedNoiseVariance = (std2(blurredImageWithNoise) / SNR)^2; % Estimate noise variance
restoredImage = deconvwnr(blurredImageWithNoise, psf, estimatedNoiseVariance);

% Calculate the difference images (original vs. restored)
differenceImage = imabsdiff(inputImage, restoredImage);

% Display all images in one figure
figure;

subplot(2, 3, 1);
imshow(inputImage);
title('Input Image');

subplot(2, 3, 2);
imshow(blurredImage);
title('Blurred Image');

subplot(2, 3, 3);
imshow(blurredImageWithNoise);
title('Blurred Image with AWGN');

subplot(2, 3, 4);
imshow(restoredImage);
title('Restored Image');

subplot(2, 3, 5);
imshow(differenceImage);
title('Difference Image (Original vs. Restored)');
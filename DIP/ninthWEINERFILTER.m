clc;
close all;
clear all;

% Weiner Filter
% 1. read the input image
% 2. blur the input image
% 3. add some guassian noise to the blur image
% 4. take that image as degraded image
% 5. apply weiner filter and try to get the original image

% Read the input image
originalImage = imread('bird_color_image.jpg');

% Blur the input image
blurredImage = imgaussfilt(originalImage, 3); % You can adjust the standard deviation for different blur levels

% Add Gaussian noise to the blurred image
noiseSigma = 10; % Standard deviation of the Gaussian noise
noisyImage = imnoise(blurredImage, 'gaussian', 0, (noiseSigma/255)^2);

% Take the noisy image as the degraded image
degradedImage = noisyImage;

% Convert the degraded image and blurred image to double
degradedImage = im2double(degradedImage);
blurredImage = im2double(blurredImage);

% Compute the noise variance
estimatedNoise = degradedImage - blurredImage;
noiseVar = var(estimatedNoise(:)); % Compute the noise variance

% Define the point spread function (PSF) for the blur
PSF = fspecial('gaussian', [5 5], 2); % Gaussian PSF, you can adjust the size and standard deviation

% Apply Wiener filter to get the original image
estimatedSignal = deconvwnr(degradedImage, PSF, noiseVar);

% Display the results
subplot(1, 3, 1), imshow(originalImage), title('Original Image')
subplot(1, 3, 2), imshow(degradedImage), title('Degraded Image')
subplot(1, 3, 3), imshow(estimatedSignal), title('Restored Image')

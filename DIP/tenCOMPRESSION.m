clc;
close all;
clear all;

% Read the input image
input_image = imread('bird_color_image.jpg');

% Convert to grayscale if the input image is RGB
if size(input_image, 3) == 3
    input_image = rgb2gray(input_image);
end

% Convert to double precision for DCT processing
input_image_double = double(input_image);

% Perform 2D DCT on the input image
dct_image = dct2(input_image_double);

% Define the compression threshold based on energy
threshold = 0.1; % Adjust as needed

% Find the threshold value based on energy
total_energy = sum(dct_image(:).^2);
energy_threshold = total_energy * threshold;

% Perform compression by keeping only coefficients above the threshold
compressed_dct_image = dct_image .* (abs(dct_image) > energy_threshold);

% Reconstruct the compressed image using inverse DCT
output_image_double = idct2(compressed_dct_image);

% Convert the output image back to uint8
output_image_uint8 = uint8(output_image_double);

% Calculate PSNR and SSIM between input and output images
psnr_value = psnr(input_image, output_image_uint8);
ssim_value = ssim(input_image, output_image_uint8);

% Compute PSNR and SSIM images comparing input and output
psnr_diff_image = abs(input_image - output_image_uint8);
ssim_diff_image = abs(input_image - output_image_uint8);

% Display the input and output images
subplot(2, 3, 1), imshow(input_image), title('Input Image');
subplot(2, 3, 2), imshow(output_image_uint8), title('Compressed Image');
subplot(2, 3, 3), imshow(psnr_diff_image), title('PSNR Image');
subplot(2, 3, 4), imshow(ssim_diff_image), title('SSIM Image');

% Display PSNR and SSIM values
fprintf('PSNR: %.2f dB\n', psnr_value);
fprintf('SSIM: %.4f\n', ssim_value);


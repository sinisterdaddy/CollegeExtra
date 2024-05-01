clc;
close all;
clear all;

% Download the black and white image locally
image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Sample_of_black_and_white_photography.JPG/2560px-Sample_of_black_and_white_photography.JPG';
image_filename = 'black_and_white.jpg'; % Specify the filename
websave(image_filename, image_url); % Download the image

% Load the black and white image from the local directory
bw_image = imread(image_filename);

% Display and save the original image
figure;
imshow(bw_image);
title('Original Black and White Image');
imwrite(bw_image, 'original_bw_image.jpg');

% Intensity transformations: These techniques are used to change the
% intensities such as darkness and brightness.


% 1. Performing Linear transformation ---- Image Negative
negative_image = 255 - bw_image;

% Display and save the negative image
figure;
imshow(negative_image);
title('Negative Black and White Image');
imwrite(negative_image, 'negative_bw_image.jpg');



% 2. Perform piece wise linear --- here we adjust pixel intensities
piecewise_image = zeros(size(bw_image), 'uint8'); % Initialize the output image

% Define piece-wise linear transformation function

% This is applied for intensity values 0 - 100
slope1 = 1.5;
intercept1 = 0;
%This is applied for intensity values 101 - 200
slope2 = 0.8;
intercept2 = 50;

% Apply piece-wise linear transformation
piecewise_image(bw_image <= 100) = slope1 * bw_image(bw_image <= 100) + intercept1;
piecewise_image(bw_image > 100 & bw_image <= 200) = slope2 * bw_image(bw_image > 100 & bw_image <= 200) + intercept2;
piecewise_image(bw_image > 200) = 255;

% Display and save the piece-wise linear transformed image
figure;
imshow(piecewise_image);
title('Piece-wise Linear Transformed Image');
imwrite(piecewise_image, 'piecewise_linear_image.jpg');


% 3. Perform log transformations --- it enhances the contrast of the image
log_image = log(1 + double(bw_image));
% Normalize the intensity range
log_image = uint8(255 * log_image / max(log_image(:)));
figure;
imshow(log_image);
title('Log Transformed Image');
imwrite(log_image, 'log_transformed_image.jpg');



% 4. exponential transformation ---- it emphasize differences in pixel
% intensities instead of stretching or compressing of pixels
exponential_image = exp(double(bw_image));
% Normalize the intensity range
exponential_image = uint8(255 * exponential_image / max(exponential_image(:))); 
figure;
imshow(exponential_image);
title('Exponential Transformed Image');
imwrite(exponential_image, 'exponential_transformed_image.jpg');



% 5. gamma transforamtions ---- used to correct non linearities in the
% image. It involves power-of-law [s=round(255⋅(r/255​).gamma)]
gamma = 0.9; % value can be adjusted as our will
gamma_image = uint8(255 * (double(bw_image) / 255).^gamma); % Apply gamma transformation
figure;
imshow(gamma_image);
title('Gamma Transformed Image');
imwrite(gamma_image, 'gamma_transformed_image.jpg');



% 6. bit-plane slicing --- it is used to extract bit planes from the image
% for better image visual

% Initialize cell array to store bit planes
bit_planes = cell(8, 1); 

for i = 1:8
    % Extract ith bit plane
    bit_plane = bitget(bw_image, i); 
    % Store the bit plane in the cell array
    bit_planes{i} = uint8(bit_plane) * 255; 
end

% Display and save the bit planes
figure;
for i = 1:8
    subplot(2, 4, i);
    imshow(bit_planes{i});
    title(['Bit Plane ', num2str(i)]);
end
saveas(gcf, 'bit_planes.jpg');

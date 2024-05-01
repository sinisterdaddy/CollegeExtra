clc;
close all;
clear all;

% (a). Perform average filtering for input image and then perform convolution operation 3x3, 5x5, 7x7, 9x9, 15x15 without using conv2 
% Define input image
inputImage = imread('color_image.jpg');
inputImage = double(inputImage); % Convert to double precision

% Define different kernel sizes
kernelSizes = [3, 5, 7, 9, 15];

% Perform average filtering
avgFiltered = imfilter(inputImage, fspecial('average', [3, 3]));

% Perform convolution with different kernel sizes
for i = 1:length(kernelSizes)
    kernelSize = kernelSizes(i);
    kernel = ones(kernelSize) / (kernelSize^2); % Generate average kernel
    
    % Perform convolution without using conv2
    [rows, cols, ~] = size(avgFiltered);
    result = zeros(rows, cols, 3, 'like', avgFiltered); % Initialize result with the same data type as avgFiltered
    
    % Padding input image
    paddedImage = padarray(avgFiltered, [(kernelSize-1)/2, (kernelSize-1)/2]);
    
    % Perform convolution for each color channel
    for channel = 1:3
        for x = 1:rows
            for y = 1:cols
                % Ensure data types match before element-wise multiplication
                paddedRegion = double(paddedImage(x:x+kernelSize-1, y:y+kernelSize-1, channel));
                result(x, y, channel) = sum(sum(paddedRegion .* kernel));
            end
        end
    end
    
    % Display result
    figure;
    subplot(1, 2, 1);
    imshow(uint8(avgFiltered)); % Display average filtered image
    title('Average Filtered Image');
    
    subplot(1, 2, 2);
    imshow(uint8(result)); % Display convolved image
    title(['Convolution with ', num2str(kernelSize), 'x', num2str(kernelSize), ' Kernel']);
end


% (b). Perform Loglation transformation for same input image and then perform convolution operation 3x3, 5x5, 7x7 without using conv2
% Perform Loglation transformation
logTransformed = log(1 + double(inputImage)); 

% Normalize Loglation transformed image to uint8 range
logTransformed = uint8((logTransformed - min(logTransformed(:))) / (max(logTransformed(:)) - min(logTransformed(:))) * 255);

% Perform convolution with different kernel sizes
for i = 1:length(kernelSizes)
    kernelSize = kernelSizes(i);
    kernel = ones(kernelSize) / (kernelSize^2); % Generate average kernel
    
    % Perform convolution without using conv2
    [rows, cols, ~] = size(logTransformed);
    result = zeros(rows, cols, 3, 'like', logTransformed); % Initialize result with the same data type as logTransformed
    
    % Padding input image
    paddedImage = padarray(logTransformed, [(kernelSize-1)/2, (kernelSize-1)/2]);
    
    % Perform convolution for each color channel
    for channel = 1:3
        for x = 1:rows
            for y = 1:cols
                % Ensure data types match before element-wise multiplication
                paddedRegion = double(paddedImage(x:x+kernelSize-1, y:y+kernelSize-1, channel));
                result(x, y, channel) = sum(sum(paddedRegion .* kernel));
            end
        end
    end
    
    % Normalize result to uint8 range
    result = uint8(result / max(result(:)) * 255);
    
    % Display result
    figure;
    subplot(1, 2, 1);
    imshow(uint8(logTransformed)); % Display Loglation transformed image
    title('Loglation Transformed Image');
    
    subplot(1, 2, 2);
    imshow(result); % Display convolved image
    title(['Convolution with ', num2str(kernelSize), 'x', num2str(kernelSize), ' Kernel']);
end

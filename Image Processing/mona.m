
monalisa = imread('elephant.jpg');
grayscale = rgb2gray(monalisa);
imagemat = im2double(grayscale);

%for the image histogram showing color intensity of the matrix
imshow(imagemat);


[U S V] = svd(imagemat);

%PLOTTING THE TOP 10 EIGENVECTORS FO THE IMAGE MATRIX
%WHICH IS OBTAINED BY SINGULAR VALUE DECOMPOSITION

U = U(:,1:640);

%Plotting for the eigenvalues of the grayscale image matrix
%figure(1); clf;
%plot(bi(:,1),bi(:,2),'b.');   % centered data
%hold on;


%plot(U(:,2),'-o-b');   % first eigenvector
%plot(U(:,1),'-xr');   % first eigenvector
%plot(U(:,3),'-xr');   % first eigenvector

%hold off;
%axis equal; % rescale plot
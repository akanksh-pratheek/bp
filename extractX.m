function x = extractX(i)
obj = VideoReader('ball_test.avi');

for j = 1:i
    frame = readFrame(obj);
end

    img = frame(50:480,90:520);
    img = rgb2gray(img);
    imgnew = imbinarize(img,0.38);
 %  imshow(imgnew)
 %  sumrow = sum(imgnew,2);
    sumcol = sum(imgnew);
    [~,x] = min(sumcol);
 %  [~,y] = min(sumrow);


end

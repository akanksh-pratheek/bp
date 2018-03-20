while(1)
  % img = snapshot(cam);
    init = imread('camframe.jpeg');
    img = init(50:480,90:520);
  % img = rgb2gray(img);
    imgnew = imbinarize(img,0.38);
    imshow(imgnew)
    sumrow = sum(imgnew,2);
    sumcol = sum(imgnew);
    [~,x] = min(sumcol);
    [~,y] = min(sumrow);
end


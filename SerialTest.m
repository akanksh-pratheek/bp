    

    clear all
    
       if ~isempty(instrfind)
     fclose(instrfind);
      delete(instrfind);
       end
    rpiserial=serial('COM4','BaudRate',9600, 'DataBits', 8, 'StopBits', 2, 'Parity', 'even')
    fopen(rpiserial);
    out = fscanf(rpiserial,'%s', 6);
    x = str2num(out(1:3))
    y = str2num(out(4:6))
    fclose(rpiserial);
    %disp('done')
    %plot(x,y);
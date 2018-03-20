clear;

t = 0:(1/30):5;
X = 120*ones(1,151);
Y = 200*ones(1,151);

s = tf('s');
H = tf(((-7*9.86)/5)/s^2);
kp = -1.08;
kd = -0.45;
C = pid(kp,0,kd);
T = feedback(C*H,1);

figure('Name','Pole-Zero plot of Open Loop');
pzmap(H);

figure('Name','Step Reponse of Open Loop');
step(H);

figure('Name','Pole-Zero plot of Closed Loop');
pzmap(T);

figure('Name','Step Response of Controller');
step(T);

x = lsim(T,X,t);
y = lsim(T,Y,t);

traj = ones(250);

for i = 2:151
    traj(round(x(i)),round(y(i))) = 0;   
end

figure('Name','Trajectory to (120,200)');
imshow(traj);






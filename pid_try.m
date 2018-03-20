xsp = 100;                  % Goal

umin = -5;               % Minimum beam angle
umax = 5;                % Maximum beam angle 
v = [0,0,0];

Kp = 0.5;                   % Proportional Gain
Kd = 0.1;
Ka = 1;
lastDVal = 0;
lastlastDVal = 0;

for i = 1:3
x = extractX();
error = x-xsp;
Dval = error - lastError;
pterm = Kp*(error);
dTerm = Kd * (((5*DVal) + (3*lastDVal) + (2*lastLastDVal))/10.0);
aTerm = Ka * (((DVal - lastDVal) + (lastDVal - lastLastDVal))/2.0);
u = pterm + dterm + aterm;

v(i) = max(min(u,umax),umin);

lastError = error;
lastLastDVal = lastDVal;
lastDVal = DVal;
end
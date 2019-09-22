year_1950_2045 = 1950:2045;
x = (year_1950_2045 - 1949)./(40.27);
p1 = 0.02192;
p2 = 0.143;
p3 = 0.2594;
p4 = -0.1077;
poly3 = p1*x.^3 + p2*x.^2 + p3*x + p4;

p1 = 0.05731;
p2 = 0.02192;
p3 = -0.003246;
p4 = 0.2594;
p5 = -0.06414;

poly4 = p1*x.^4 + p2*x.^3 + p3*x.^2 + p4*x + p5;

p1 = -0.0295;
p2 = 0.05731;
p3 = 0.1195;
p4 = -0.003246;
p5 = 0.1971;
p6 = -0.06414;
poly5 = p1*x.^5 + p2*x.^4 + p3*x.^3 + p4*x.^2 + p5*x + p6;

a0 = 0.1988;
a1 = -0.288;
b1 = -0.5003;
a2 = -0.2598;
b2 = 0.07944;
a3 = 0.02726;
b3 = 0.06384;
a4 = 0.08401;
b4 = 0.01196;
w = 0.0332;
Fourier4  = a0 + a1*cos(x*w) + b1*sin(x*w) + a2*cos(2*x*w) + b2*sin(2*x*w) + a3*cos(3*x*w) + b3*sin(3*x*w) + a4*cos(4*x*w) + b4*sin(4*x*w);

figure;
hold on;
plot(land_ocean_temperature(:,1), land_ocean_temperature(:,2), 'o', 'color', [134/255 183/255 223/255], 'MarkerFaceColor',[134/255 183/255 223/255]);
plot(land_ocean_temperature(:,1), land_ocean_temperature(:,3), '-', 'color', [246/255 143/255 76/255], 'LineWidth', 3);
% plot(year_1950_2045, poly3, 'gp-');
plot(year_1950_2045, poly4, '-', 'color', [237/255 30/255 36/255], 'LineWidth', 3);
plot(year_1950_2045, poly5, '-', 'color', [57/255 82/255 164/255], 'LineWidth', 3);
plot(year_1950_2045, poly4, 'p-', 'color', [237/255 30/255 36/255]);
plot(year_1950_2045, poly5, 'p-', 'color', [57/255 82/255 164/255]);
% plot(year_1950_2045, Fourier4, 'r+');
grid on
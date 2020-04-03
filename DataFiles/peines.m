
%Measuraments of nanoparticles layer

Z = readmatrix('PAE peines.xlsx','Range','B416:B616');
f = readmatrix('PAE peines.xlsx','Range','C416:C616');
Ph = readmatrix('PAE peines.xlsx','Range','D416:D616');
Z1 = readmatrix('PAE peines.xlsx','Range','E416:E616');
Z2 = readmatrix('PAE peines.xlsx','Range','F416:F616');
C = readmatrix('PAE peines.xlsx','Range','G416:G616');

loglog(f,Z);
grid on;
title('Z(f)');
xlabel('frequency(f)');
ylabel('impedance(Z)');

hold all
figure;
loglog(Z2,Z1, '.');
xlim([1 10^10]);
ylim([1 10^10]);
grid on
title('Z2(Z1)');
xlabel('real(Z1)');
ylabel('imaginay(Z2)');
hold off

hold all
figure;
plot(f,Ph);
grid on
title('Ph(f)');
xlabel('frequency(f)');
ylabel('phase(Ph)');
hold off

hold all
figure;
plot(f,C);
grid on
title('C(f)');
xlabel('frequency(f)');
ylabel('capacity(C)');
hold off


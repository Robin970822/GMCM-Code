figure
axesm('eqdcylin','maplatlimit',[-80 80],'maplonlimit',[0 360]);  % Create a cylindrical equidistant map
pcolorm(Nlt,Nlg,sst_std)           % pseudocolor plot "stretched" to the grid
load coast                                 % add continental outlines
plotm(lat,long)
colorbar

%Plot the SST data without using the MATLAB Mapping Toolbox
 
figure
pcolor(Nlg,Nlt,sst_std);shading interp;
load coast;hold on;plot(long,lat);plot(long+360,lat);hold off
colorbar

figure
axesm('eqdcylin','maplatlimit',[-80 80],'maplonlimit',[0 360]);  % Create a cylindrical equidistant map
pcolorm(Nlt,Nlg,sst_std_1900_1950)           % pseudocolor plot "stretched" to the grid
load coast                                 % add continental outlines
plotm(lat,long)
colorbar

%Plot the SST data without using the MATLAB Mapping Toolbox
 
figure
pcolor(Nlg,Nlt,sst_std_1900_1950);shading interp;
load coast;hold on;plot(long,lat);plot(long+360,lat);hold off
colorbar

figure
axesm('eqdcylin','maplatlimit',[-80 80],'maplonlimit',[0 360]);  % Create a cylindrical equidistant map
pcolorm(Nlt,Nlg,sst_std_1950)           % pseudocolor plot "stretched" to the grid
load coast                                 % add continental outlines
plotm(lat,long)
colorbar

%Plot the SST data without using the MATLAB Mapping Toolbox
 
figure
pcolor(Nlg,Nlt,sst_std_1950);shading interp;
load coast;hold on;plot(long,lat);plot(long+360,lat);hold off
colorbar
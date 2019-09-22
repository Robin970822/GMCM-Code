figure
axesm('eqdcylin','maplatlimit',[-80 80],'maplonlimit',[0 360]);  % Create a cylindrical equidistant map
pcolorm(Nlt,Nlg,model);           % pseudocolor plot "stretched" to the grid
load coast                                 % add continental outlines
plotm(lat,long);
colorbar
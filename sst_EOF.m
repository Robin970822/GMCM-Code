%%
% Ô¤´¦Àí
[nx ny nt] = size(sst);
pre_sst = sst;
% pre_sst(find(isnan(pre_sst)))=0;
pre_sst = reshape(pre_sst, [nx * ny nt]);
%%
% ¾àÆ½
for i = 1:(nx * ny)
    if ~isnan(pre_sst(i, 1))
        mean_sst = mean(pre_sst(i, :));
        std_sst = std(pre_sst(i, :));
        pre_sst(i, :) = (pre_sst(i, :) - mean_sst) / std_sst;
    else
        pre_sst(i, :) = 0;
    end 
end
%%
C = pre_sst * pre_sst' / (nt);
%%
C(find(isnan(C)))=0;
%%
[V lamda] = eig(C);


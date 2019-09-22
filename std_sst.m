[nx ny nt] = size(sst);
for i = 1:nx
    for j = 1:ny
        data = sst(i, j, :);
        data = reshape(data, [1, nt]);
        data_1900 = data(600: nt);
        data_1900_1950 = data(600:1200);
        data_1950 = data(1200: nt);
        if ~isnan(data(1))
            sst_std(i, j) = std(data);
            sst_std_1900(i, j) = std(data(600: nt));
            sst_std_1950(i, j) = std(data(1200: nt));
            sst_std_1900_1950(i, j) = std(data_1900_1950);
        else
            sst_std(i, j) = NaN;
            sst_std_1900(i, j) = NaN;
            sst_std_1950(i, j) = NaN;
            sst_std_1900_1950(i, j) = NaN;
        end
    end
end
function [] = statics_prov(data, provs)
worldmap('canada');
load coast
geoshow(lat, long);
geoshow(provs, 'FaceColor', [1.0 1.0 1.0]);
sorted_data = sort(data);
len = length(data);
p = floor(len / 4);
for i = 1:len
    if data(i) >= sorted_data(len - p + 1)
        color = [249/255 166/255 43/255];
    elseif data(i) >= sorted_data(len - 3 * p)
        color = [77/255 144/255 203/255];
    else
        color = [17/255 59/255 101/255];
    end
    geoshow(provs(i), 'FaceColor', color)
end
end
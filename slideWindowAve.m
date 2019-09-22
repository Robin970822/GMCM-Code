function [ out ] = slideWindowAve( in, window, stride )
%slideWindowAve
%   in
%   window
%   stride
%   out
len = length(in);
out_len = floor((len - window + 1) / stride);
out = [];
for i = 1 : out_len
    left = i + (i - 1) * (stride - 1);
    right = left + window - 1;
    out(i) = sum(in(left : right)) / window;
end
out = out';
end

function [ out ] = slideWindowAve( in, window, stride )
%slideWindowAve 滑窗平均
%   in      输入
%   window  窗口大小
%   stride  滑动步长
%   out     输出
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

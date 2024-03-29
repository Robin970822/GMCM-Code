figure;
hold on;
plot(t, tm, 'bo');
plot(t(length(t)-length(tma5)+1:length(t)), tma5, 'r-', 'LineWidth', 3);
plot(t(length(t)-length(tma7)+1:length(t)), tma7, 'g-', 'LineWidth', 3);
plot(t(length(t)-length(tma10)+1:length(t)), tma10, 'y-', 'LineWidth', 3);
grid on;
legend('魁北克省12月平均气温', '滑动窗口为5', '滑动窗口为7', '滑动窗口为10');
xlabel('年/year', 'FontSize', 24);
ylabel('T_m /℃ ', 'FontSize', 24);
title('魁北克省12月平均气温滑动滤波效果', 'FontSize', 24);
#采用time库的sleep()方法模拟一个持续的进度
import time  # 导入时间库，用于计时和休眠
import random
scale = 50  # 进度条总宽度（字符数）
print("执行开始".center(scale//2,"-"))  # 打印居中的标题，两侧用横线填充
start = time.perf_counter()  # 记录开始时间

# 主循环：从 0% 到 100% 逐步更新进度条
for i in range(scale+1):
    a = '*' * i           # 已完成部分：用 * 表示
    b = '.' * (scale-i-1) # 未完成部分：用 . 表示（原代码此处应为 scale-i，存在小错误）
    c = (i/scale)*100     # 计算百分比
    dur = time.perf_counter() - start  # 计算已耗时
    # 格式化输出：百分比居中显示，已完成→未完成，显示耗时
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(random.uniform(0.05,0.2))  # 暂停 0.05-0.2 秒，控制更新速度
#random.random()不接受任何参数
print("\n"+"执行结束".center(scale//2,"-"))  # 打印居中的结束标记
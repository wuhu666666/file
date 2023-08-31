import time
import tkinter as tk

# 设置常量，每个番茄时钟的时长 (单位：秒)
POMODORO_TIME = 25 * 60

# 初始化计时器
time_remaining = POMODORO_TIME
running = False

# 创建主窗口
root = tk.Tk()
root.title("Pomodoro Timer")

# 在界面上创建计时器标签
text_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
text_label.pack(pady=50)

# 创建启动和停止按钮
start_button = tk.Button(root, text="Start", font=("Helvetica", 20))
start_button.pack(side=tk.LEFT, padx=50)

stop_button = tk.Button(root, text="Stop", font=("Helvetica", 20))
stop_button.pack(side=tk.RIGHT, padx=50)

# 定义启动和停止按钮的回调函数
def start_timer():
    global running, time_remaining
    running = True
    while running and time_remaining > 0:
        # 更新计时器标签
        text_label.config(text="%02d:%02d" % (time_remaining // 60, time_remaining % 60))
        
        # 延迟1秒
        time.sleep(1)
        
        # 减少剩余时间
        time_remaining -= 1
    
    # 如果计时器已经完毕，弹出对话框提示用户
    if time_remaining == 0:
        tk.messagebox.showinfo("Pomodoro Timer", "Time's up!")
        
def stop_timer():
    global running, time_remaining
    running = False
    time_remaining = POMODORO_TIME
    text_label.config(text="25:00")

# 将回调函数与按钮绑定
start_button.configure(command=start_timer)
stop_button.configure(command=stop_timer)

# 进入tkinter事件循环
root.mainloop()

import psutil
import os
import signal

def kill_process_by_name(process_name):
    """
    根据进程名称杀死所有匹配的进程。

    参数:
        process_name (str): 要杀死的进程名称。
    """
    killed = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 检查进程名称是否匹配
            if process_name.lower() in proc.info['name'].lower():
                print(f"Killing process: {proc.info['name']} (PID: {proc.info['pid']})")
                # os.kill(proc.info['pid'], signal.SIGTERM)  # 发送终止信号
                os.kill(proc.info['pid'], signal.SIGKILL)  # 强制杀死进程
                killed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # 忽略无法访问或已终止的进程
            continue

    if not killed:
        print(f"No process named '{process_name}' found.")

if __name__ == "__main__":
    # 输入要杀死的进程名称
    # process_name = input("Enter the process name to kill (e.g., xetex): ")
    process_name = 'tex'
    kill_process_by_name(process_name)
# coding = uft-8
import os
import time

import pyuac
import requests
import win32api
import win32serviceutil
from ping3 import ping


# If your want to other，please change this. | 想刷啥就改啥
colo = "HKG"
# Set the overtime time | 设置超时时间
overtime = 5
# Please set your warp path. | 填入官方WARP软件安装路径
WARP_path = r"C:\Program Files\Cloudflare\Cloudflare WARP\Cloudflare WARP.exe"
# Set the Ping List | 设置Ping网站清单
web_list = ["google.com", "baidu.com"]

warp = "plus"


def check_uac():
    if __name__ == "__main__":
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
            exit()


def ping_test(web):
    try:
        web_ping = int(ping(str(web)) * 1000)
        return web_ping
    except TypeError:
        return "overtime"


def main():
    win32api.ShellExecute(0, 'open', WARP_path, '', '', 1)
    os.system("title WARP-PLUS-HKG")
    x = 0
    os.system('cls')
    print("")
    print("                WARP-PLUS-HKG (script)")
    print("")
    print("[info] 版本: v1.1.0")
    print("[info] 项目: https://github.com/Windla/WARP-PLUS-HKG")
    print("[info] 正在等待Cloudflare WARP启动")
    time.sleep(5)

    while True:
        os.system("cls")
        print(""
              "                WARP-PLUS-HKG (script)"
              "")
        x = x + 1
        print(f"[info] 第{x}次连接 1.1.1.1 trace")
        # trace = str("")
        try:
            trace = requests.get("https://1.1.1.1/cdn-cgi/trace", timeout=overtime).text
        except requests.exceptions.RequestException:  # 蚌埠住了
            print("[warn] 与trace连接超时")
            trace = str("")  # 双保险(?)
        if trace.find(warp) == -1:
            print("[info] WARP+: no")
        else:
            print("[info] WARP+: yes")
        if trace.find(colo) == -1:
            print("[info] isHKG: no")
            if x == 1:
                check_uac()
            try:
                win32serviceutil.RestartService("Cloudflare WARP")
            finally:
                print("[info] 重启Cloudflare WARP服务中")
            time.sleep(5)
        else:
            print("[info] isHKG: yes")
            break

    # End
    print("[info]-------------------- 连接", colo, "成功! --------------------")
    for web in web_list:
        web_ping = ping_test(web)
        print(f"[info] Ping {web}: ", web_ping, "ms")
    print("[info]--------------------------------------------------------")
    print("[info] 3s后窗口将自动关闭")
    time.sleep(3)
    exit()


if __name__ == "__main__":
    main()

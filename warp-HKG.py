# coding = uft-8
from asyncio.windows_events import NULL
import requests
import win32serviceutil
import time
import pyuac
import win32api
import os
from ping3 import ping


#
# ------------Settings------------
# If your want to other，please change this. | 想刷啥就改啥
colo = "HKG"
# Set the overtime time | 设置超时时间
overtime = 5
# Please set your warp path. | 填入官方WARP软件安装路径
WARP_path = "C:\\Program Files\\Cloudflare\\Cloudflare WARP\\Cloudflare WARP.exe"
# Set the Ping List | 设置Ping网站清单
web_list=["google","baidu","bilibili"] #Only www.___.com -> www.<web_list>.com | 仅支持www.___.com的形式
#


# Get UAC
def GetUAC():
    if __name__ == "__main__":
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
            exit()
warp = "plus"
win32api.ShellExecute(0, 'open', WARP_path, '', '', 1)
os.system("title WARP-PLUS-HKG By Wind_la (Bilibili)")
x = 0
os.system('cls' if os.name == 'nt' else 'clear')
print("")
print("                WARP-PLUS-HKG (script)" + " By Wind_la")
print("")
print("[!] 版本: v1.1.0")
print("[!] 项目: https://github.com/Windla/WARP-PLUS-HKG")
print("[!] 正在等待Cloudflare WARP启动")
time.sleep(5)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("                WARP-PLUS-HKG (script)" + " By Wind_la")
    print("")
    x = x + 1
    print(f"[!] 第{x}次连接 1.1.1.1 trace")
    # trace = str("")
    try:
        trace = requests.get("https://1.1.1.1/cdn-cgi/trace", timeout=overtime).text
    except requests.exceptions.RequestException:    # 蚌埠住了
        print("[-] Warning: Overtime!!!")
        trace = str("") # 双保险(?)
    if trace.find(warp) == -1:
        print("[-] WARP+: no")
    else:
        print("[+] WARP+: yes")
    if trace.find(colo) == -1:
        print("[-] isHKG: no")
        if x == 1: # First GetUAC
            GetUAC()
        try:
            win32serviceutil.RestartService("Cloudflare WARP")
        finally:
            print("[!] 重启Cloudflare WARP服务中")
        time.sleep(5)
    else:
        print("[+] isHKG: yes")
        break


# End
print("[!]-------------------- 连接", colo,"成功! --------------------")

def pingtest(web): #Only www.XXX.com -> www.web.com
    try:
        web_ping = int(ping('www.'+str(web)+'.com')*1000)
        return web_ping
    except TypeError:
        return "overtime"

for web in web_list:
    web_ping = pingtest(web)
    print(f"[*] Ping {web}: ", web_ping, "ms")
print("[!]--------------------------------------------------------")
print("[!] 3s后窗口将自动关闭")
time.sleep(3)
exit()

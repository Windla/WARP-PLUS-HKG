# coding = uft-8
import requests
import win32serviceutil
import time
import pyuac
import win32api
import os
from ping3 import ping


# Settings
# If your want to other，please change this.
colo = "HKG"
# Please set your warp path.
WARP_path = "C:\\Program Files\\Cloudflare\\Cloudflare WARP\\Cloudflare WARP.exe"


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
print("[!] 版本: v1.0.0")
print("[!] 正在等待Cloudflare WARP启动")
time.sleep(5)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("                WARP-PLUS-HKG (script)" + " By Wind_la")
    print("")
    x = x + 1
    print(f"[!] 第{x}次连接 1.1.1.1")
    trace = requests.get("https://1.1.1.1/cdn-cgi/trace").text
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
ping_google = int(ping('www.google.com')*1000)
ping_baidu  = int(ping("www.baidu.com")*1000)
print("[*] Ping Google: ", ping_google, "ms")
print("[*] Ping  Baidu: ", ping_baidu, "ms")
print("[!]--------------------------------------------------------")
print("[!] 3s后窗口将自动关闭")
time.sleep(3)
exit()

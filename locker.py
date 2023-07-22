# coding = uft-8
import os

import pyuac

path1 = "C:\ProgramData\Cloudflare\settings.json"
path2 = "C:\ProgramData\Cloudflare\conf.json"
path3 = "C:\ProgramData\Cloudflare\.warp_dns.lock"  # 连接warp时生成

def getUAC():
    if __name__ == "__main__":
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
            exit()


def unlock():
        os.system('echo y|cacls ' + path1 + ' /t /p everyone:f > nul')
        os.system('echo y|cacls ' + path2 + ' /t /p everyone:f > nul')
        os.system('echo y|cacls ' + path3 + ' /t /p everyone:f > nul')

def lock():
        os.system('echo y|cacls ' + path1 + ' /t /p everyone:r > nul')
        os.system('echo y|cacls ' + path2 + ' /t /p everyone:r > nul')
        os.system('echo y|cacls ' + path3 + ' /t /p everyone:r > nul')

def main():
        getUAC()
        print("# https://github.com/Windla/WARP-PLUS-HKG/issues/3\n"
              "# 利用'安全选项卡'功能控制json文件的权限\n"
              "# 该issue暂时无法实现锁定HKG(安全选项卡实现)\n")
        code = int(input("请输入对应数字 unlock:0 lock:1\n"))
        if code == 0:
            unlock()
        else:
            lock()

while True:
        main()

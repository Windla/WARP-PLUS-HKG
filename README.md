# WARP-PLUS-HKG

> 将Cloudflare WARP的主机托管中心锁定为HKG(香港), 以换取低延时warp+或warp(随缘)

## 联动
[WARP-PLUS-FIX](https://github.com/Windla/WARP-PLUS-FIX) | 在原ALIILAPRO大佬的基础上, 加入了超时和速度检测

## 必读(新增)
   近期反馈证实HKG并不是那么容易刷到的, 有些人刷了一晚上都没成功, 需要做好失败的心里准备.
  
   省流: WARP必须赏脸给你来一个HKG的链接才有可能成功(详见 Q&A 1. 刷不到HKG?)
  
   > 截止至2023年7月22日, 该脚本在warp与warp+测试中仍然可用

   > `locker.py` 解锁 锁定配置文件, 但以目前来看, 似乎不能锁定HKG?(重启软件下测试)
   
## 注意 
  0. 仅适用Windows
  1. 臭打游戏的须注意, 游戏流量不一定走warp
     建议食用 ss + warp 代理模式(未测试,有问题issue提)
  2. 更新了超时设定
  
## Q&A
  1. 刷不到HKG?:
  > 四舍五入等于玄学 | 完全看你自己能不能连到(只要成功一次就行,但是有概率掉回非HKG)

  > 请尝试在WARP软件设置中 `重置加密密钥` (刷新账户) 或者 `重置所有设置` (切换到warp)

  2. 网络质量: 
  > 具体看cf&运营商抽不抽风
  
  3. 掉HKG:
  > 重刷就行(有可能是你的网络与HKG连接不好掉的)
  
## 下载
  [Clone](https://github.com/Windla/WARP-PLUS-HKG/archive/refs/heads/main.zip)

## 安装

```
pip install -r requirements.txt
```

or

```
pip install requests
pip install pywin32
pip install pyuac
pip install ping3
```

## 使用
  需要`Python` [下载](https://python.org/) | 安装`Python`后双击运行即可

## 关于UAC
  UAC是为了开关`Cloudflare WARP`服务使用, 无其他用处！
  
## 关注我
  [Bilibili](https://space.bilibili.com/358002685)
## Star!

[![Stargazers over time](https://starchart.cc/Windla/WARP-PLUS-HKG.svg)](https://starchart.cc/Windla/WARP-PLUS-HKG)

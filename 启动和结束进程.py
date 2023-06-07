
import os

os.system('taskkill /IM scrcpy.exe /F')
os.system('taskkill /IM adb.exe /F')
os.system('D:\\ProgramData\\WZCQ\\scrcpy\\adb connect 127.0.0.1:7555')
os.system('D:\ProgramData\WZCQ\scrcpy\scrcpy --max-size 960')
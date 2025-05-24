import serial
import time

ser = serial.Serial('COM17', 9600)  # 替换为你的端口
time.sleep(2)

for speed in range(85, 96):  # 从 85 到 95 逐个测试
    command = f"P{speed}T90\n"  # 固定 MG90S 不动，只调 FS90R
    ser.write(command.encode())
    print(f"Testing FS90R with P{speed}")
    time.sleep(2)

# 最后停下来
ser.write(b"P90T90\n")
print("Stop test")
ser.close()

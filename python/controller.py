import serial
from time import sleep
import sys

COM_PORT = 'COM3'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)

try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        choice = input('按1開紅燈、按2改變紅燈呼吸頻率為10ms、按3改變紅燈呼吸頻率為5ms、輸入10關紅燈、按4開黃燈、按5改變黃燈呼吸頻率為10ms、按6改變黃燈呼吸頻率為5ms、輸入40關黃燈、按7開藍燈、按8改變藍燈呼吸頻率為10ms、按9改變藍燈呼吸頻率為5ms、輸入70關藍燈、按e關閉程式  ').lower()

        if choice == '1':
            print('開紅燈')
            ser.write(b'scr1e')  # 訊息必須是位元組類型
            sleep(0.5)              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        elif choice == '2':
            print('紅燈呼吸頻率100ms')
            ser.write(b'sdr010e')
            sleep(0.5) 
        elif choice == '3':
            print('紅燈呼吸頻率5ms')
            ser.write(b'sdr005e')
            sleep(0.5)     
        elif choice == '4':
            print('開黃燈')
            ser.write(b'scy1e')
            sleep(0.5) 
        elif choice == '5':
            print('黃燈呼吸頻率100ms')
            ser.write(b'sdy010e')
            sleep(0.5) 
        elif choice == '6':
            print('黃燈呼吸頻率5ms')
            ser.write(b'sdy005e')
            sleep(0.5) 
        elif choice == '7':
            print('開藍燈')
            ser.write(b'scb1e')
            sleep(0.5) 
        elif choice == '8':
            print('藍燈呼吸頻率10ms')
            ser.write(b'sdb010e')
            sleep(0.5) 
        elif choice == '9':
            print('藍燈呼吸頻率5ms')
            ser.write(b'sdb005e')
            sleep(0.5)         
        elif choice == '10':
            print('紅燈關')
            ser.write(b'scr0e')
            sleep(0.5)        
        elif choice == '40':
            print('黃燈關')
            ser.write(b'scy0e')
            sleep(0.5)        
        elif choice == '70':
            print('藍燈關')
            ser.write(b'scb0e')
            sleep(0.5)                                 
        elif choice == 'e':
            ser.close()
            print('再見！')
            sys.exit()
        else:
            print('指令錯誤…')
except KeyboardInterrupt:
    ser.close()
    print('再見！')
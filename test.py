# Скрипт для проверки переходника USB - 16 UART.
# Необходимо соеденить вывод TXD c выводом RXD для каждого порта.

import serial
import serial.tools.list_ports

print("Получение списка портов ...")
ports = serial.tools.list_ports.comports()

for port in ports:
    if port.vid != 0x0403 or port.pid != 0x6011:
        continue

    maxBaudRate = 12000000
    ser = serial.Serial(port.device, maxBaudRate, timeout=0.01)
    print("Тест порта " + ser.name + " ... ", end = '')

    testString = "hello\n"
    ser.write(testString.encode())
    answer = ser.readline()
    if answer == testString.encode():
        print("\033[32m" + "пройден" + "\033[0m" + ".")
    else:
        print("\033[31m" + "провален" + "\033[0m" + ".")
    ser.close()

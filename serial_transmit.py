import time
import serial
from bitstring import BitStream, BitArray

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 5
        #parity=serial.PARITY_NONE,
        #stopbits=serial.STOPBITS_ONE,
        #bytesize=serial.EIGHTBITS,
        #timeout=1
)
counter=0

while 1:
        stringnya = "ler"
        byte_str = bytes(stringnya, 'ascii')
        ser.write(byte_str)
        
        string_balik = stringnya[::-1]
        print(string_balik)
        byte_str_balik = bytes(string_balik, 'ascii')
        bit_arr = BitArray(byte_str_balik)
        str_biner = bit_arr.bin
        custom_biner = ""
        hitung = 0
        for biner in str_biner:
            if hitung % 8 == 0 and hitung != 0:
                custom_biner += " "
                custom_biner += "01"
                custom_biner += " "
            custom_biner += str(biner)
            hitung += 1
        custom_biner += " 0"
        print(custom_biner)        
        time.sleep(1)
        counter += 1

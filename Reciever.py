import machine
import time

def listen(ADC):
    while ADC.read_u16() > 50000:
        time.sleep(.01)

def Transcribe(ADC):
    bit_time = .5
    checking_interval = 8
    checking_threshold = 5
    checking = 0
    temp_bin = ""
    while True:
        temp_bin = ""
        for i in range(8):
            # records bits
            checking = 0
            for x in range(checking_interval):
                # Testing if bit is on
                if ADC.read_u16() <= 50000:
                    checking += 1
                time.sleep(bit_time/checking_interval)
            if checking >= checking_threshold:
                temp_bin += "1"
            else:
                temp_bin += "0"
        print(int(temp_bin,2))
        print(chr(int(temp_bin,2)))
            



        



ADC = machine.ADC(machine.Pin(26))

while True:
    listen(ADC)
    Transcribe(ADC)
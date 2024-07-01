import machine
import time
message = "©This cat is a burrito"

char_list = []
bin_list = []
for letter in message:
    char_list.append(letter)

for char in char_list:
    bin_list.append(f"{ord(char):0>8b}")
print(bin_list)

def sending(lst : list[str], led : machine.Pin) -> None:
    for byte in lst:
        for binary in byte:
            if binary is "1":
                led.on()
            else:
                led.off()
            time.sleep(.5)
    led.off()

sending(bin_list,machine.Pin(16, machine.Pin.OUT))

# for byte in bin_list:
#     print(chr(int(byte,2)))
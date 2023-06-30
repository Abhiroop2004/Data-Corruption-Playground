import random
def flip(file): #flips random bytes of the file by the random function
    with open(file, 'rb') as f:
        data = bytearray(f.read())
    
    index = random.randint(0, len(data) - 1)
    bit_position = random.randint(0, 7)
    
    # Flip the selected bit
    data[index] ^= 1 << bit_position
    
    with open(file, 'wb') as f:
        f.write(data)

def modify(file, byte_positions, new_values):   #modifies specific byte positions according to the user input
    with open(file, 'rb') as f:
        data = bytearray(f.read())
    
    for position, value in zip(byte_positions, new_values):
        data[position] = value
    
    with open(file, 'wb') as f:
        f.write(data)

def noise(file, intensity): #introduces noise into the file in the intensity entered by the user
    with open(file, 'rb') as f:
        data = bytearray(f.read())
    
    for i in range(len(data)):
        noise = random.randint(-int(intensity*256),int(intensity*256))
        data[i] = (data[i] + noise) % 256
    
    with open(file, 'wb') as f:
        f.write(data)

def swapfile(file1, file2): #swaps the content of two files
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            data1 = bytearray(f1.read())
            data2 = bytearray(f2.read())
    with open(file1, 'wb') as f1, open(file2, 'wb') as f2:
        f1.write(data2)
        f2.write(data1)
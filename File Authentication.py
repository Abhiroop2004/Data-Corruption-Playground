from Corruption import *
from hashlib import sha256

def input_file():   #inputs file name from the user
    file=input("Enter file name with extension: ")
    return file

def hash(file): #produces the hash of the file
    with open(file,"rb") as f:
        l=[]
        b=f.read(1024)
        while b:
            l.append(b)
            b=f.read(1024)
        h=sha256(l[-1])
        for b in reversed(l[:-1]):
            h=sha256(b+h.digest())
    return (h.hexdigest())

def check(h1,h2):   #checks whether the hashes are unchanged
    if h1==h2:
        print("Hashes are unchanged, file integrity maintained")
    else:
        print("Hashes are changed, file integrity not maintained")

print("\n----Welcome to File Authentication Playground!----\n")
print("\n Choice 1: Flip Random Bites of a file")
print("\n Choice 2: Modify certain Bytes of a file")
print("\n Choice 3: Introduce Noise into a file")
print("\n Choice 4: Swap contents of a file")
print("\n Choice 5: Exit the System\n")

while(True):
    c=int(input("Please Enter your Choice: "))

    if c==1:    #block for fliping random bytes of the file
        file=input_file()
        hinitial=hash(file)
        flip(file)
        hfinal=hash(file)
        check(hinitial,hfinal)

    elif c==2:  #block for modifying bites of the file
        file=input_file()
        hinitial=hash(file)        
        n=int(input("How many positions do you want to modify? "))
        pos=[[0]*2]*n
        for i in range(n):
            print("Position:",i+1)
            pos[i][0]=int(input("Enter position: "))
            pos[i][1]=int(input("Enter new value of position: "))
        modify(file, pos[0],pos[1])
        hfinal=hash(file)
        check(hinitial, hfinal)

    elif c==3:  #block for introducing noise into a file
        file=input_file()
        hinitial=hash(file)
        intensity=int(input("Enter the percentage of noise, range 1-100: "))/100
        noise(file,intensity)
        print("\nSuccesfully introduced noise into the file!\n")
        hfinal=hash(file)
        check(hinitial,hfinal)

    elif c==4:  #block for swapping contents of file
        file1=input_file()
        file2=input_file()
        hash1=hash(file1)
        hash2=hash(file2)
        swapfile(file1, file2)
        hfinal1=hash(file1)
        hfinal2=hash(file2)
        if (hash1==hfinal2 and hash2==hfinal1):
            print("\nFile Swapping Bypassed!")
            print("This shows that SHA 256 checks message integrity and doesn't detect swapping of file contents")

    elif c==5:  #block to exit
        print("\n----Thank you for using our System!----\n")
        break

    else:   #block for wrong choice by user
        print("Sorry! Wrong Choice")


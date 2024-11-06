# python code to demonstrate binart types
#Bytes example
print("Bytes Example")
# creating a byte object
b=bytes([65,66,67,68])
print(b)
#output:b'ABCD'
#accessing elements in a byte objects
print(b[0])
#output:65
#iterating through  byte object
for byte in b:
    print(byte,end='')
#output:65 66 67 68
print("\n")
#binary type example
print("bytearray example")
#craeting a bytearray object
ba=bytearray([65,66,67,68])
print(ba)
# output:bytearray(b'ABCD')
#modifying elemnts in a bytearray
ba[0]=97
#changing 'A' (65) to 'a' (97)
print(ba)
#output;bytearray(b'aBCDE')
#adding elemnts to a bytearray to byte
print("/n")
#memory view example
print("memery view example")
#creating a memeory view obj
b_mv=bytes([65,66,67,69])
#craeting a memory view obj
mv=memoryview(b_mv)
print(mv)
print(mv[0])
mv_slice=mv[1:4]
print(mv_slice.tobytes())
ba_mv=bytearray([65,67,68,69])
mv_ba=memoryview(ba_mv)
mv_ba[0]=97
print(ba_mv)
print("THIS PROGRAM IS WRITTEN BY VAANI, ERP:-162")
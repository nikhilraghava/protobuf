#! /usr/bin/python

import main_pb2 as proto

num = proto.AddNum()
# Ask user for input
num.num_a = int(input('Num_a:'))
num.num_b = int(input('Num_b:'))

# Write
with open('out.bin', 'wb') as f:
    f.write(num.SerializeToString())

# Open and read
with open('out.bin', 'rb') as f:
    num = proto.AddNum()
    num.ParseFromString(f.read())
    # Add both the number from buffer
    sum = num.num_a + num.num_b
    print(sum)
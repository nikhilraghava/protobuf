#! /usr/bin/python

import main_pb2 as proto
import sys

num = proto.AddNum()
# Ask user for input
num.num_a = int(input('Num_a:'))
num.num_b = int(input('Num_b:'))

# Write
with open('src\out.bin', 'wb') as f:
    f.write(num.SerializeToString())

# Open and read
with open('src\out.bin', 'rb') as f:
    num = proto.AddNum()
    num.ParseFromString(f.read())
    # Add both the number from buffer
    ans = num.num_a + num.num_b
    print(ans)

#! /usr/bin/python

import main_pb2 as proto
import sys

num = proto.AddNum()
num.num_a = int(input('Num_a:'))
num.num_b = int(input('Num_b:'))

# Write
with open('src\out.bin', 'wb') as f:
    f.write(num.SerializeToString())

with open('src\out.bin', 'rb+') as f:
    num = proto.AddNum()
    num.ParseFromString(f.read())
    # do something with read_metric
    ans = num.num_a + num.num_b
    num.num_c = ans
    f.write(num.SerializeToString())
    print(ans)

# coding=utf-8
import compute
import time

start_time = time.clock()
ret = compute.pi(20000000)
print(ret)
end_time = time.clock()
print ("pi time: %f s" % (end_time - start_time))


start_time = time.clock()
ret = compute.flb(40)
print(ret)
end_time = time.clock()
print ("flb time: %f s" % (end_time - start_time))
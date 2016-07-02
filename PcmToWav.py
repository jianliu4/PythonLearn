#encoding=utf-8
import wave
import random
import struct
import datetime
noise_output = wave.open('noise.wav', 'w')
noise_output.setparams((1, 2, 16000, 0, 'NONE', 'not compressed'))

d1 = datetime.datetime.now()

sample_len = 1323000
print ('----第一种方法----')
print ('writing')
for i in range(0 , sample_len):
    value = random.randint(-32767, 32767)
    packed_vaule = struct.pack('h', value)
    noise_output.writeframes(packed_vaule)
noise_output.close()

d2 = datetime.datetime.now()
print ('第一种方法所花费的时间：'),(d2-d1)
print ('----第二种方法----')
noise_file = open('noise.pcm','w')
for i in range(0,sample_len):
    value = random.randint(-32767, 32767)
    packed_vaule = struct.pack('h', value)
    noise_file.write(packed_vaule)
d3 = datetime.datetime.now()
print('第二种方法所花费的时间：'), (d3-d2)
noise_file.close()

print ('----第三种方法----')
noise_file3 = wave.open('noise_file3.wav','w')
noise_file3.setparams((1, 2, 16000, 0, 'NONE', 'not compressed'))

values = []
for i in range(0,sample_len):
    value = random.randint(-32767, 32767)
    packed_vaule = struct.pack('h',value)
    values.append(packed_vaule)
value_all = ''.join(values)
noise_file3.writeframes(value_all)
noise_file3.close()
d4 = datetime.datetime.now()
print('第三种方法所花费的时间：'), (d4-d3)
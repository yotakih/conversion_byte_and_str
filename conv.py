#!/usr/bin/python3
#-*-coding: utf-8-*-

#string to byte
print('ab'.encode('utf-8'))
#> b'ab'

#byte to string
print(b'ab'.decode('utf-8'))
#> 'ab'

#bytes to hexstr
print(b'ab'.hex())
#> '6162'

#hexstr to bytes
print(int('6162',16).to_bytes(2,'big'))
#> b'ab'

#byte to int
print(int.from_bytes(b'ab','big'))
#> 24930
print(int.from_bytes(b'ab','little'))
#> 25185

#int to byte
print(int(24930).to_bytes(2,'big'))
#> b'ab'
print(int(25185).to_bytes(2,'little'))
#> b'ab'

#int to hexStr
print('{:0x}'.format(24930))
#> '6162'



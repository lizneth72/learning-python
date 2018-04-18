'''
Prompt a user to enter in an IP address from standard input.
Read the IP address in and break it up into its octets.
Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

$ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------


Four columns, fifteen characters wide, a header column,
 data centered in the column.
'''

from __future__ import print_function
from __future__ import unicode_literals

user_ip = input('Please enter an IP address: ')
octets = user_ip.split('.')
octet1 = int(octets[0])
octet2 = int(octets[1])
octet3 = int(octets[2])
octet4 = int(octets[3])

print('{:^15}{:^15}{:^15}{:^15}'.format('Octet1',
      'Octet2', 'Octet3', 'Octet4'))
print('-' * 60)
print('{:^15}{:^15}{:^15}{:^15}'.format(*octets))
print('{:^15}{:^15}{:^15}{:^15}'.format(bin(octet1),
      bin(octet2), bin(octet3), bin(octet4),))
print('{:^15}{:^15}{:^15}{:^15}'.format(hex(octet1),
      hex(octet2), hex(octet3), hex(octet4),))
print('-' * 60)

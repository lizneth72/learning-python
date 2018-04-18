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

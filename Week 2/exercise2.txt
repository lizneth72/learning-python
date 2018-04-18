"""
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list.
Use the .extend() method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses.
Print out the first IP address in the list.
Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list
 and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'.
Print out the new first IP address in the list.
"""

from __future__ import print_function
from __future__ import unicode_literals


my_ip_addrs = ['10.1.1.1',
               '10.1.2.1',
               '10.1.3.1',
               '172.16.1.1',
               '172.16.2.1',
               '192.168.1.1']


my_ip_addrs.append('224.0.0.1')
my_ip_addrs.extend(['224.0.0.5', '224.0.0.6'])
my_ip_addrs += ['239.0.0.1', '239.0.1.1']

print(my_ip_addrs)
print(my_ip_addrs[0])
print(my_ip_addrs[-1])

print('Removed: ' + my_ip_addrs.pop(0))
print('Removed: ' + my_ip_addrs.pop(-1))
print(my_ip_addrs)

my_ip_addrs[0] = '2.2.2.2'
print('First IP address updated to: ' + my_ip_addrs[0])

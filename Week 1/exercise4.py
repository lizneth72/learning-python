from __future__ import print_function
from __future__ import unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version2 = show_version.strip()
show_version3 = show_version2.split()
print(show_version3)
'Cisco' in show_version3[1].capitalize()
print(f'Is this a Cisco device?: {"Cisco" in show_version3[1].capitalize()}')
print(f'Is this a 881 router?: {"881" in show_version3[1]}')


show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version3 = show_version.split()
print(f'Is this a Cisco device?: {"Cisco" in show_version3[1].capitalize()}')
print(f'Is this a switch?: {"3650" in show_version3[1]}')
print(f'Is this a 881 router?: {"881" in show_version3[1]}')

print(f'The serial number is: {show_version3[2]}')
print(f'The model is: {show_version3[1]}')



import sys
import RN4870_serial
argument = str(sys.argv)
print sys.argv[0]
print sys.argv[1]
test = RN4870_serial.RN4870('test')
test.set_port(sys.argv[1])
test.open_connection()
config = ['command_mode','factory_reset', 'command_mode', 'PZ', 'Reboot','command_mode',
            'PS,11223344556677889900aabbccddeeff', 'PC,10223344556677889900aabbccddeeff,1A,05',
            'Reboot', 'command_mode', 'A']
for command in config:
    if command is 'command_mode':
        test.command_mode()
    elif command is 'factory_reset':
        test.factory_reset()
    elif command is 'Reboot':
        test.reboot()
    else:
        test.send_command(command)

test.close_connection()




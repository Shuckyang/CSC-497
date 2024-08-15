from pythonosc import udp_client
from pyjoycon import JoyCon, get_L_id, get_R_id
import time

joycon_r = get_R_id()
joy_r = JoyCon(*joycon_r)

joycon_l = get_L_id()
joy_l = JoyCon(*joycon_l)



# Set the IP address and port of your Max/MSP instance
max_ip = '127.0.0.1'  # IP address of your Max/MSP instance
max_port = 9000  # Port number Max/MSP is listening on for OSC messages

# Create an OSC client
client = udp_client.SimpleUDPClient(max_ip, max_port)

# Define the OSC address you want to send messages to in Max/MSP
left_accel_add = '/l_switch/accel'
left_gyro_add = '/l_switch/gyro'
left_butt_add = '/l_switch/butt'

left_stick_add = '/l_switch/stick'


right_accel_add = '/r_switch/accel'
right_gyro_add = '/r_switch/gyro'
right_butt_add = '/r_switch/butt'

right_stick_add = '/r_switch/stick'




# Send the OSC message to Max/MSP
while True:
#Left Joy-Con
    dataL = joy_l.get_status()
    x = dataL.get('accel').get('x')
    y = dataL.get('accel').get('y')
    z = dataL.get('accel').get('z')
    l_accel = [x,y,z]

    x = dataL.get('gyro').get('x')
    y = dataL.get('gyro').get('y')
    z = dataL.get('gyro').get('z')
    l_gyro = [x,y,z]

    up = dataL.get('buttons').get('left').get('up')
    down = dataL.get('buttons').get('left').get('down')
    left = dataL.get('buttons').get('left').get('left')
    right = dataL.get('buttons').get('left').get('right')

    minus = dataL.get('buttons').get('shared').get('minus')

    zl = dataL.get('buttons').get('left').get('zl')

    l_buttons = [up,down,left,right,minus,zl]

    l_hor = dataL.get('analog-sticks').get('left').get('horizontal')
    l_ver = dataL.get('analog-sticks').get('left').get('vertical')
    l_stick = [l_hor,l_ver]


# #Right Joy-Con
    dataR = joy_r.get_status()
    x = dataR.get('accel').get('x')
    y = dataR.get('accel').get('y')
    z = dataR.get('accel').get('z')
    r_accel = [x,y,z]

    x = dataR.get('gyro').get('x')
    y = dataR.get('gyro').get('y')
    z = dataR.get('gyro').get('z')
    r_gyro = [x,y,z]

    y = dataR.get('buttons').get('right').get('y')
    x = dataR.get('buttons').get('right').get('x')
    a = dataR.get('buttons').get('right').get('a')
    b = dataR.get('buttons').get('right').get('b')

    plus = dataR.get('buttons').get('shared').get('plus')
    zr = dataR.get('buttons').get('right').get('zr')

    r_buttons = [y,x,a,b,plus,zr]

    r_hor = dataR.get('analog-sticks').get('right').get('horizontal')
    r_ver = dataR.get('analog-sticks').get('right').get('vertical')
    r_stick = [r_hor,r_ver]        



   # print(dataR.get('buttons').get('right'))    
#     # hor = dataL.get('analog-sticks').get('left').get('horizontal')
#     # ver = dataL.get('analog-sticks').get('left').get('vertical')
#     # analog_sticks_left = [hor,ver]

#     # hor = dataL.get('analog-sticks').get('right').get('horizontal')
#     # ver = dataL.get('analog-sticks').get('right').get('vertical')
#     # analog_sticks_right = [hor,ver]
    
    client.send_message(left_accel_add, l_accel)
    client.send_message(left_gyro_add, l_gyro)
    client.send_message(left_butt_add, l_buttons)
    client.send_message(left_stick_add, l_stick)



    client.send_message(right_accel_add, r_accel)
    client.send_message(right_gyro_add, r_gyro)
    client.send_message(right_butt_add, r_buttons)
    client.send_message(right_stick_add, r_stick)


    time.sleep(0.075)
#     #client.send_message(left_gyro_add, analog_sticks)
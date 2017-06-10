import subprocess
import os
import configparser
import sys
sys.path.append('./src/')
from motor import Motor
from file_operator import FileOperator

print('-------------------------------------')
print('Starting Project Pathfinder Initation')
print('-------------------------------------')
try:
    import RPi.GPIO as GPIO
except ImportError:
    print('Note: Imported fake gpio because we are not on a Raspberry Pi')
    from fake_gpio import FakeGPIO as GPIO

print('')
print('( 1 )  Getting latest gcode files from github.com/nikonoll/gcodefiles')
print('       git pull says:')
subprocess.call('chmod +x ./gcodepull.sh', shell=True)
subprocess.call('./gcodepull.sh', shell=True)

print('')
print('( 2 )  Reading Config File for GPIO Info')
config = configparser.ConfigParser()
config.read('config.ini')
xdir = int(config['motor_x']['direction_pin'])
xstep = int(config['motor_x']['step_pin'])
ydir = int(config['motor_y']['direction_pin'])
ystep = int(config['motor_y']['step_pin'])
zdir = int(config['motor_z']['direction_pin'])
zstep = int(config['motor_z']['step_pin'])
enable_pin = int(config['motor_enable']['pin'])
sleep_time = float(config['motor_enable']['sleep'])
x_mil = int(config['grid']['x_step_p_millimeter'])
y_mil = int(config['grid']['y_step_p_millimeter'])
z_mil = int(config['grid']['z_step_p_millimeter'])

print('        xdir: ' + str(xdir) + ' xstep:  ' + str(xstep))
print('        ydir: ' + str(ydir) + ' ystep:  ' + str(ystep))
print('        zdir: ' + str(zdir) + ' zstep:  ' + str(zstep))
print('        enable pin: ' + str(enable_pin))
print('        sleep time: ' + str(sleep_time))
print('        ---------------------')
print('        x_mil: ' + str(x_mil))
print('        y_mil: ' + str(y_mil))
print('        z_mil: ' + str(z_mil))

inputok = input('-      Looks good? Keep going? (y/n)  ')
if inputok != 'y':
    sys.exit('( ! )     Okay. Stopping ...')

motor = Motor(xdir, xstep, ydir, ystep, zdir, zstep, enable_pin, sleep_time)
motor.setup
import code; code.interact(local=dict(globals(), **locals()))
operator = FileOperator(motor, x_mil, y_mil, z_mil)

print('')
print('( 3 )  Choosing GCODE File')
files = os.listdir('./gcodefiles/')
filnum = -1
for file in files:
    filnum += 1
    print('      ' + str(filnum) + ' : ' + file)

inputfile = input('-      Choose file by entering (0...' + str(filnum) + '): ')
filename = files[int(inputfile)]
filepath = './gcodefiles/' + filename

print('')
print('( 4 )  Ok. Ready for Printing: ' + filename)

operator.printfile(filepath)

print('')
print('( 5 )  Done. Cleaning up')
motor.cleanup

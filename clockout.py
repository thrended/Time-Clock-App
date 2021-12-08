
####################                     ####################
###############                              ################
############                                     ############
########            LINE BEAR PRODUCTIONS            ########
############                                     ############
###############                              ################
####################                     ####################

# Clock-In/Out App
# Default Usage: Hours:Minutes
# Alt Usage ('n'): Hours.decimal

from datetime import datetime, time, timedelta
import math

print('Are we calculating by hours:minutes? Enter "n" if calculating by decimal hours')
flag = input()
flag = flag.lower()

print('Enter the current number of hours:')
currentHrs = float(input())

if flag != 'n':
    currentHrs = math.floor(currentHrs)
    print('Enter the current number of minutes:')
    currentMin = float(input())
    currentHrs += currentMin/60

print('Total current hours =', currentHrs)
    
print('Enter the desired number of hours:')
goalHrs = float(input())

x = goalHrs - currentHrs
y = round(60 * (x - math.floor(x)))
x = math.floor(x)
print('You need', x, 'hours and', y, 'minutes more')

print('Enter your clock-in time (hour hand):')
startHr = int(input())
print('Enter your clock-in time (minute hand):')
startMin = int(input())
#startTime = time(startHr, startMin)
startTime = datetime.now()
startTime = startTime.replace(hour=startHr, minute=startMin)
endTime = startTime + timedelta(hours=x, minutes=y)
print('You need to clock-out at ' + endTime.strftime('%I:%M %p') + ' to attain ' + str(goalHrs) + ' total hours.')


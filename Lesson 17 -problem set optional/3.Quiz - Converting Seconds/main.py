# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(time):
    # There are 3600 seconds in an hour
    # 60 minutes in an hour
    # and 60 seconds in a minute
    
    hour = int(time/3600)
    
    seconds_after_hour = time - (hour * 3600)
    
    minute = int(seconds_after_hour/60)
    
    second = seconds_after_hour - (minute * 60)
    
    hours = ''
    
    minutes = ''
    
    seconds = ''
    
    if hour != 1:
        hours = 's'
    
    if minute != 1:
        minutes = 's'
    
    if second != 1:
        seconds = 's'
    
    #if hours or minutes or seconds == 1:
    return str(hour) + ' ' + 'hour' + hours + ',' + ' ' + str(minute) + ' ' + 'minute' + minutes + ',' + ' ' + str(second) + ' ' + 'second' + seconds

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

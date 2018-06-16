# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def bits(s):
    assert s in ['kb','kB','Mb','MB','Gb','GB','Tb','TB']
    prefix = {'k': 2 ** 10, 'M': 2 ** 20, 'G': 2 ** 30, 'T': 2 ** 40}
    return prefix[s[0]] * (8 if s[1] == 'B' else 1)

def output(number, unit):
    return "{0} {1}{2}".format(number, unit, "s" if number != 1 else "")

def convert_seconds(n):
    h, remainder = divmod(int(n), 3600)
    m = remainder / 60
    return "{0}, {1}, {2}".format(output(h, "hour"), output(m, "minute"),
                                  output(n - (3600*h + 60*m), "second"))

def download_time(file_size, fs_unit, bandwidth, bw_unit):
    fs = file_size * bits(fs_unit)
    bw = bandwidth * bits(bw_unit)
    return convert_seconds(fs/bw if fs==(fs/bw)*bw else 1.0*fs/bw)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

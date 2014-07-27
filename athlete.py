class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_times(self, times):
        self.times.extend(times)

    def add_time(self, time):
        self.times.append(time)
                                     
def sanitize(time):
    if '-' in time:
        splitter = '-'
    elif ':' in time:
        splitter = ':'
    else:
        return (time)
    (mins, secs) = time.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        tmpl = data.strip().split(',')
        return (Athlete(tmpl.pop(0), tmpl.pop(0), tmpl))
    
    except IOError as ioerr:
        print ("File error" + str(ioerr))
        return (None)
    
james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))

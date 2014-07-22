'''head first exercise'''

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
        return ({'Name':tmpl.pop(0),
                 'dob':tmpl.pop(0),
                 'times':[sanitize(t) for t in tmpl]})
    except IOError as ioerr:
        print ("File error" + str(ioerr))
        return (None)

sarah = get_coach_data('sarah2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
james = get_coach_data('james2.txt')

print ("James score is: " + str(sorted(set(james['times']))[0:3]))
print ("Julie score is: " + str(sorted(set(julie['times']))[0:3]))
print ("Mikey score is: " + str(sorted(set(mikey['times']))[0:3]))
print ("Sarah score is: " + str(sorted(set(sarah['times']))[0:3]))

import sys

def printProgress(iteration, total, seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    barLength = 50
    percents = int(round(100 * (iteration / float(total))))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '+' * filledLength + '-' * (barLength - filledLength)

    sys.stdout.write('\r%s |%s| %+3s%s %s %02d:%02d:%02d' % ('PROGRESS:', bar, percents, '%', '  Time:', h, m, s)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

from time import sleep

items = list(range(0, 20))
i = 0
l = len(items)

printProgress(i, l,0)
for item in items:
    n = 1
    sleep(n)
    i += 1
    printProgress(i, l, n*i)

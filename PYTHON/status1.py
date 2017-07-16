import sys

def printProgress(iteration, total, prefix='', suffix='', barLength=100):
    percents = "%d" % (100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '¦' * filledLength + '-' * (barLength - filledLength)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

from time import sleep

items = list(range(0, 100))
i = 0
l = len(items)

printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
for item in items:
    sleep(0.1)
    i += 1
    printProgress(i, l, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
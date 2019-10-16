from timeit import Timer


for iteration in range(10):
    s = "rec_fib(%s)"%str(iteration)
    t1 = Timer(s, "from rec_fibonacci import fibonacci as rec_fib")
    time1 = t1.timeit(3)
    s = "iter_fib(%s)" % str(iteration)
    t2 = Timer(s, "from iter_fibonacci import fibonacci as iter_fib")
    time2 = t2.timeit(3)
    s = "mem_fib(%s)" % str(iteration)
    t3 = Timer(s, "from mem_fibonacci import fibonacci as mem_fib")
    time3 = t3.timeit(3)
    print("n=%2d, rec_fib: %8.7f, iter_fib: %8.7f, mem_fib: %8.7f" % (iteration, time1, time2, time3))
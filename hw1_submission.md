Mateo Cantagallo mateocantagallo@gmail.com

## Data of 100 runs:

Numbers of threads 16
The average of algorithm 1 is: 0.614
The average of algorithm 2 is: 0.482
The average of algorithm 3 is: 0.433
The average of algorithm 4 is: 0.428
The average of algorithm 5 is: 0.249
The average of algorithm 6 is: 0.243

Numbers of threads 8
The average of algorithm 1 is: 0.56
The average of algorithm 2 is: 0.474
The average of algorithm 3 is: 0.467
The average of algorithm 4 is: 0.45
The average of algorithm 5 is: 0.153
The average of algorithm 6 is: 0.153

Numbers of threads 4
The average of algorithm 1 is: 0.539
The average of algorithm 2 is: 0.448
The average of algorithm 3 is: 0.45
The average of algorithm 4 is: 0.434
The average of algorithm 5 is: 0.118
The average of algorithm 6 is: 0.114

Numbers of threads 2
The average of algorithm 1 is: 0.598
The average of algorithm 2 is: 0.428
The average of algorithm 3 is: 0.427
The average of algorithm 4 is: 0.412
The average of algorithm 5 is: 0.152
The average of algorithm 6 is: 0.153



Speed up one thread vs 16
The average of algorithm 1 is:  2.252
The average of algorithm 2 is:  2.568
The average of algorithm 3 is:  2.894
The average of algorithm 4 is:  3.234
The average of algorithm 5 is:  5.522
The average of algorithm 6 is:  5.679

- Question 1: Is more or less the same ass we can see in the data.
- Question 2:
    - a) No, we can see that its almost the same until we reach 16 threads, that the performance drops.
    - b) For only one thread the average time for algorithm 6 is 1.38, so the speedup: is on the table

- Question 3:
    - a)The most important optimization is adding padding between the result addresses.
    This is evident in Algorithm 5, where it consistently shows the best performance across all runs.
    - b) The hardware optimization works by ensuring that all threads write to
    different locations in memory that are on separate cache lines.
    This approach prevents cache line contention and invalidation, as each thread
    operates on a distinct cache line, avoiding interference with others.



# Gem5

Data for 16 threads

Time Simulated
Taccesshe average of algorithm 1 is: 0.000917
The average of algorithm 2 is: 0.000915
The average of algorithm 3 is: 0.000686
The average of algorithm 4 is: 0.000687
The average of algorithm 5 is: 0.000145
The average of algorithm 6 is: 0.000114

Read shearing
The average of algorithm 1 is: 2380
The average of algorithm 2 is: 599
The average of algorithm 3 is: 2385
The average of algorithm 4 is: 610
The average of algorithm 5 is: 2404
The average of algorithm 6 is: 650

Write shearing
The average of algorithm 1 is: 32906
The average of algorithm 2 is: 32863
The average of algorithm 3 is: 32814
The average of algorithm 4 is: 32776
The average of algorithm 5 is: 192
The average of algorithm 6 is: 245

Hits ratio
The average of algorithm 1 is:  0.859
The average of algorithm 2 is:  0.933
The average of algorithm 3 is:  0.868
The average of algorithm 4 is:  0.941
The average of algorithm 5 is:  0.932
The average of algorithm 6 is:  0.994


SpeedUp from 1 core to 16 with 16 threads:
The average of algorithm 1 is:  0.088
The average of algorithm 2 is:  0.089
The average of algorithm 3 is:  0.118
The average of algorithm 4 is:  0.118
The average of algorithm 5 is:  0.559
The average of algorithm 6 is:  2.816

- Question 4:
    - a) The speed up is 2.816.
    - b) Is similar, excepts that here the algorithm 2 is similar to 1 and not to algorithms 3 and 4 like in the real hardware.
- Question 5:
    - a) In this case the biggest impact was chunking.
        This can be seen in the comparison of 1 and 2, and
- Question 6:
    - The algorithms that reduce read shearing are the ones that use chunk arrays, this
    can be seen in the table, with algorithms 2,4 and 6, that use this technique.
    This happens because in those algorithms that don't use chunking, one core
    brings the line from memory and all others cores access addresses in that line.
- Question 7:
    - the algorithms that reduce writing shearing are the ones that use padding in the result.
    This can be seen in the table, with algorithms 5 and 6.
    This happens because now all cores are not writing in the same lines.
- Question 8:
    - a) the most important hardware characteristic is write sharing, we can see this because
    the biggest drop in time is in algorithm 5 and 6 which are those that significantly reduce
    write sharing.
    - b) The hardware reason why write shearing is the most important factor when optimizing, is because
        the protocol used, MESI, make it that when a core writes a line, this entired line gets invalidated
        in all other cores, so every core needs to mantein coherence every time it writes.
        Meanwhile, the fact that MESI allows for core to core shearing of addresses when read, mitigates the performance
        loss from cache misses.

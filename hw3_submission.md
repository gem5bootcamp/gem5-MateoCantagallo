# HomeWork 3: Secure memory Mateo Cantagallo mateocantagallo@gmail.com


-  A) What were you able to get working and why do you think that you couldn't get the final objective?
    - I was able to implement the basic secure memory described in the slides, including additional functions that were not originally provided.
    The code compiled successfully; however, I was not able to get it to run.
    I couldn't complete the task primarily because I spent too much time trying to get the base model to work.
    Additionally, I believe I needed more context and time to fully understand the secure memory implementation.
-  B) Describe the experiment that you would run if everything was working.
    - If I had been able to implement the full secure memory along with its cache for metadata, I would first run a script with a traffic generator,
    using the base secure memory as a baseline and then comparing it to the secure memory with metadata caching.
    The focus of the experiment would be on analyzing the differences in memory requests for each CPU request and the simulated execution time.
- C) Run some applications (getting started suite works, or matrix multiply) using the baseline and discuss
     the impact that you believe the secure memory changes will have.
    - Using the workload suite already implemented in homework 2, it is logical to assume that running the same workload with secure memory would have a substantial impact on performance, particularly in workloads with frequent memory accesses.
    This performance impact should be mitigated to some extent with the inclusion of a metadata cache.
    However, there would still be an overhead compared to the baseline.

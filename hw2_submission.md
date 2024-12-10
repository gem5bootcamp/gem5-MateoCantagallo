# Homework 2: Design space exploration
Mateo Cantagallo
mateocantagallo@gmail.com

## NAS Parallel Benchmarks

- BT: Block Tridiagonal
    - Solve a synthetic system of nonlinear PDEs
- FT: Fast Fourier Transform
    - Solve a three-dimensional partial differential equation (PDE) using the fast Fourier transform (FFT)
- CG: Conjugate Gradient
    - Estimate the smallest eigenvalue of a large sparse symmetric positive-definite matrix using the inverse iteration with the conjugate gradient method as a subroutine for solving systems of linear equations

## Answers

- Performance Comparison:
    - Compare the performance of the Big core and Little core configurations. What are the key differences in IPC and execution time?
        - As we can see in the data the IPC and execution time difference between the big and little core
        is almost 2 to 3x in all cases.
    - How do the two configurations perform across different workloads?
        - As we can see in the data, the performance between cores with the BT workload is almost a 3x in iPC and execution time and with
        CG and FT is a little more than 2x.
    - When changing the cache and memory configurations, does the performance gap between the Big and Little cores change?
        - No, the performance gap does not change
- Cache Impact:
    - How does changing the cache configuration affect performance? Discuss the trade-offs observed between your three-level cache and the alternative cache.
        - We can see that the only workload that make a difference between cache type (a L4 cache), is with FT.
        The explanation of this is because this workload fill up the L3 having a lot of L3 cache misses, in comparison to the other
        workload. This can be see in the data below.
- Insights and Conclusions:
    - Summarize your findings. What architectural choices led to the best performance? What recommendations would you make for future designs?
        - As observed, the big core performs better across all three workloads, as expected.
        However, in BT and CG, adding an L4 cache does not impact performance.
        Therefore, depending on the application, an L4 cache can be omitted to save chip space and reduce costs.

### IPC
| Processor Type | Cache Type | Workload | IPC      |
|----------------|------------|----------|----------|
| Big            | L3         | BT       | 3.102892 |
| Big            | L3         | CG       | 2.027297 |
| Big            | L3         | FT       | 2.001440 |
| Big            | L4         | BT       | 3.101280 |
| Big            | L4         | CG       | 2.026320 |
| Big            | L4         | FT       | 2.718968 |
| Little         | L3         | BT       | 0.921771 |
| Little         | L3         | CG       | 0.942454 |
| Little         | L3         | FT       | 0.837150 |
| Little         | L4         | BT       | 0.921546 |
| Little         | L4         | CG       | 0.942212 |
| Little         | L4         | FT       | 0.936042 |

### Sim seconds
| Processor Type | Cache Type | Workload | Time     |
|----------------|------------|----------|----------|
| Big            | L3         | BT       | 0.045368 |
| Big            | L3         | CG       | 0.065844 |
| Big            | L3         | FT       | 0.091457 |
| Big            | L4         | BT       | 0.045391 |
| Big            | L4         | CG       | 0.065876 |
| Big            | L4         | FT       | 0.067322 |
| Little         | L3         | BT       | 0.152718 |
| Little         | L3         | CG       | 0.141636 |
| Little         | L3         | FT       | 0.218653 |
| Little         | L4         | BT       | 0.152756 |
| Little         | L4         | CG       | 0.141672 |
| Little         | L4         | FT       | 0.195552 |

### L3 Misses
| Processor Type | Cache Type | Workload | L3 Misses |
|----------------|------------|----------|---------|
| Big            | L3         | BT       | 9191    |
| Big            | L3         | CG       | 22932   |
| Big            | L3         | FT       | 1990524 |
| Big            | L4         | BT       | 9192    |
| Big            | L4         | CG       | 22951   |
| Big            | L4         | FT       | 1992218 |
| Little         | L3         | BT       | 8945    |
| Little         | L3         | CG       | 22805   |
| Little         | L3         | FT       | 1989100 |
| Little         | L4         | BT       | 8946    |
| Little         | L4         | CG       | 22808   |
| Little         | L4         | FT       | 1991272 |


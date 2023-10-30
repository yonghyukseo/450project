from run import gem5Run
import os
import sys
from uuid import UUID
from itertools import starmap
from itertools import product
import multiprocessing as mp
import argparse

def worker(run):
    run.run()
    json = run.dumpsJson()
    print(json)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('N', action="store",
                      default=1, type=int,
                      help = """Number of cores used for simulation""")
    args  = parser.parse_args()

    # cpu_types = ['Simple','DefaultO3','Minor4', 'O3_W2K', 'O3_W256']
    cpu_types = ['Minor4']
    # mem_types = ['Inf', 'SingleCycle', 'Slow']
    mem_types = ['Slow', 'SingleCycle']
    L1_sizes = ['4kB','8kB','32kB','64kB']
    L2_sizes = ['128kB','256kB','512kB','1MB']
    dram_type = 'DDR3_1600_8x8()'
    dram_types = ['DDR3_2133_8x8()', 'LPDDR2_S4_1066_1x32()', 'HBM_1000_4H_1x64()']
    frequency = '4GHz'
    frequencies = ['1GHz','2GHz']

    bm_list = []

    # iterate through files in microbench dir to
    # create a list of all microbenchmarks

    for filename in os.listdir('microbenchmark'):
        if os.path.isdir(f'microbenchmark/{filename}') and filename != '.git':
            bm_list.append(filename)

    # For Experiment 2
    # jobs = []
    # for bm in bm_list:
    #     for cpu in cpu_types:
    #         for mem in mem_types:
    #             for L1Size in L1_sizes:
    #                 for L2Size in L2_sizes:
    #                     run = gem5Run.createSERun(
    #                         'microbench_tests',
    #                         os.getenv('M5_PATH')+'/build/X86/gem5.opt',
    #                         'gem5-config/run_micro.py',
    #                         'results/X86/run_micro/{}/{}/{}/L1_Size_{}_L2_Size_{}'.format(bm,cpu,mem,L1Size,L2Size),
    #                         cpu,mem,L1Size,L2Size,os.path.join('microbenchmark',bm,'bench.X86'))
    #                     jobs.append(run)
    
    # For Experiment 3
    # jobs = []
    # for bm in bm_list:
    #     for cpu in cpu_types:
    #         for mem in mem_types:
    #             # for fr in frequencies:
    #             for dr in dram_types:
    #                 run = gem5Run.createSERun('microbench_tests',
    #                     os.getenv('M5_PATH')+'/build/X86/gem5.opt',
    #                     'gem5-config/run_micro.py',
    #                     'results/X86/run_micro/{}/{}/{}/{}_{}'.format(bm,cpu,mem,dr,frequency),
    #                     frequency,cpu,mem,dr,os.path.join('microbenchmark',bm,'bench.X86'))
    #                 jobs.append(run)

    # For Experiment 4
    jobs = []
    for bm in bm_list:
        for cpu in cpu_types:
            for mem in mem_types:
                for fr in frequencies:
                    run = gem5Run.createSERun('microbench_tests',
                        os.getenv('M5_PATH')+'/build/X86/gem5.opt',
                        'gem5-config/run_micro.py',
                        'results/X86/run_micro/{}/{}/{}/{}'.format(bm,cpu,mem,fr),
                        fr,cpu,mem,os.path.join('microbenchmark',bm,'bench.X86'))
                    jobs.append(run)

    with mp.Pool(args.N) as pool:
        pool.map(worker,jobs)


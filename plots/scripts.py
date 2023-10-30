# Set the absolute path in 

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

if not os.getenv("LAB_PATH"):
    print("Set Lab Path\n")
    exit(1)


datadir = os.getenv("LAB_PATH") + '/results/X86/run_micro'

def gem5GetStat(filename, stat):
    filename = os.path.join(datadir, '', filename, 'stats.txt').replace('\\','/')
    with open(filename) as f:
        r = f.read()
        if len(r) < 10: return 0.0
        if (r.find(stat) != -1) :
            start = r.find(stat) + len(stat) + 1
            end = r.find('#', start)
            print(r[start:end])
            return float(r[start:end])
        else:
            return float(0.0)
all_arch = ['X86']
plt_arch = ['X86']


all_memory_models = ['SingleCycle', 'Slow', 'Inf']
plt_memory_models = ['Slow', 'SingleCycle']


all_gem5_cpus = ['Simple','DefaultO3','Minor4', 'O3_W2K', 'O3_W256']
plt_gem5_cpus = ['Minor4']

L1_sizes = ['4kB','8kB','32kB','64kB']
L2_sizes = ['128kB','256kB','512kB','1MB']

dram_type = 'DDR3_1600_8x8()'
dram_types = ['DDR3_2133_8x8()', 'LPDDR2_S4_1066_1x32()', 'HBM_1000_4H_1x64()']
frequency = '4GHz'
frequencies = ['1GHz','2GHz']

benchmarks = ['CCa',   'CCl',   'DP1f',  'ED1',  'EI', 'MI']

if len(plt_memory_models) > 1 and len(plt_gem5_cpus) > 1:
    print("Cannot vary both CPU models and memory models")
    exit(0)

# For Experiment 3
# rows = []
# for bm in benchmarks: 
#     for cpu in plt_gem5_cpus:
#         for mem in plt_memory_models:
#             # for fr in frequency:
#             for dr in dram_types:
#                 rows.append([bm,cpu,mem,dr,frequency,
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency, 'system.cpu.numCycles'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency, 'sim_insts'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency, 'sim_ops'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency, 'sim_ticks')/1e9,
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency, 'host_op_rate'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency,'system.mem_ctrl.dram.avgMemAccLat'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency,'system.mem_ctrl.dram.busUtil'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency,'system.mem_ctrl.dram.bw_total::total'),
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency,'system.mem_ctrl.dram.totBusLat'),
#                                                                         # memory with store
#                     gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+dr+"_"+frequency,'system.mem_ctrl.dram.avgWrBW')
#                 ])

# df = pd.DataFrame(rows, columns=['benchmark','cpu', 'mem', 'dram' , 'frequency' ,'cycles','instructions', 'Ops', 'Ticks','Host', 'avgmemaccesslatency','busutilit','bandwidthtotal','totalbuslatency',                                       'averagewritebandwidth'])

# For Experiment 2
# rows = []
# for bm in benchmarks: 
#     for cpu in plt_gem5_cpus:
#         for mem in plt_memory_models:
#             for L1Size in L1_sizes:
#                 for L2Size in L2_sizes:
#                     cache = "L1_Size: " + L1Size + " L2_Size: " + L2Size
#                     rows.append([bm,cpu,mem,cache,
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size, 'system.cpu.numCycles'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size, 'sim_insts'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size, 'sim_ops'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size, 'sim_ticks')/1e9,
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size, 'host_op_rate'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size,'system.mem_ctrl.dram.avgMemAccLat'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size,'system.mem_ctrl.dram.busUtil'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size,'system.mem_ctrl.dram.bw_total::total'),
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size,'system.mem_ctrl.dram.totBusLat'),
#                                                                         # memory with store
#                         gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/L1_Size_"+L1Size+"_L2_Size_"+L2Size,'system.mem_ctrl.dram.avgWrBW')
#                     ])

# df = pd.DataFrame(rows, columns=['benchmark','cpu', 'mem', 'cache', 'cycles','instructions', 'Ops', 'Ticks','Host', 'avgmemaccesslatency','busutilit','bandwidthtotal','totalbuslatency',                                       'averagewritebandwidth'])

# For Experiment 4
rows = []
for bm in benchmarks: 
    for cpu in plt_gem5_cpus:
        for mem in plt_memory_models:
            for fr in frequencies:
                rows.append([bm,cpu,mem,fr,
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr, 'system.cpu.numCycles'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr, 'sim_insts'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr, 'sim_ops'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr, 'sim_ticks')/1e9,
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr, 'host_op_rate'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr,'system.mem_ctrl.dram.avgMemAccLat'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr,'system.mem_ctrl.dram.busUtil'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr,'system.mem_ctrl.dram.bw_total::total'),
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr,'system.mem_ctrl.dram.totBusLat'),
                                                                        # memory with store
                    gem5GetStat(datadir+"/"+bm+"/"+cpu+"/"+mem+"/"+fr,'system.mem_ctrl.dram.avgWrBW')
                ])

df = pd.DataFrame(rows, columns=['benchmark','cpu', 'mem', 'frequency' ,'cycles','instructions', 'Ops', 'Ticks','Host', 'avgmemaccesslatency','busutilit','bandwidthtotal','totalbuslatency',                                       'averagewritebandwidth'])

df['ipc'] = df['instructions']/df['cycles']
df['cpi']= 1/df['ipc']
print(df)
df.to_csv('Experiment4.txt', sep='\t', index=False)

# def draw_vertical_line(ax, xpos, ypos):
#     line = plt.Line2D([xpos, xpos], [ypos + .1, ypos],
#                       transform=ax.transAxes, color='black', lw = 1)
#     line.set_clip_on(False)
#     ax.add_line(line)

# def doplot_benchmarks(benchmarks,stat,norm=True):
#     fig = plt.figure()
#     ax = fig.add_subplot(1,1,1)
#     i = 0
#     for bm in benchmarks:
#         base = df[(df['benchmark']==bm)][stat].iloc[0] if norm else 1
#         # models = plt_gem5_cpus if len(plt_memory_models) == 1 else plt_memory_models
#         models = all_memory_models
#         for j,sys in enumerate(models):
#             # if len(plt_memory_models) > 1:
#             d = df[(df['mem']==sys) & (df['benchmark']==bm)]
#             # else:
#             #     d = df[(df['cpu']==sys) & (df['benchmark']==bm)]
#             # print(d)
#             ax.bar(i, d[stat].iloc[0]/base, color='C'+str(j))
#             i += 1
#         i += 1
#     for i,sys in enumerate(models):
#         plt.bar(0,0,color='C'+str(i), label=sys)
#     new_names = benchmarks 
#     # Arranging ticks on the X axis
#     plt.xticks(np.arange(len(new_names))*(len(models)+1)+i/2, new_names, rotation=40, ha='right')


# fig_size = plt.rcParams["figure.figsize"]
# fig_size[0] = 10
# fig_size[1] = 5
# plt.rcParams["figure.figsize"] = fig_size
# fig1 = doplot_benchmarks(benchmarks,"ipc",norm=False)
# plt.ylabel('')
# plt.legend(loc=2, prop={'size': 8})
# plt.title('experiment2')
# plt.tight_layout()
# plt.savefig('O3_W2K_CPU_vs_Memories.png', format='png', dpi=600)




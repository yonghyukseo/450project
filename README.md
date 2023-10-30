[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/A8b79HZz)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11900561&assignment_repo_type=AssignmentRepo)
## README

Experiment 1
<p></p>
Modified the value of the variable plt_gem5_cpus in scripts.py and plot all memory configurations and benchmark combinations for each of the CPU. Everytime when changed the value of plt_gem5_cpus to each of CPU, ran the below commands to generate result and plot. 

python3 scripts.py

Experiment 2
<p></p>
sbatch submit.sh to generate the stat.txt file for all the different Cache configurations. (After added some code in system.py, run_micro.py, launch.py to parse the sizes of L1 and L2 cashes)

python3 scripts.py to generate the Experiment2_Q1.txt that contains 'benchmark','cpu', 'mem', 'cache', 'cycles','instructions', 'Ops', 'Ticks','Host', 'avgmemaccesslatency','busutilit','bandwidthtotal','totalbuslatency','averagewritebandwidth'. (After added some code that writing df data into txt file)

Experiment 3
<p></p>
sbatch submit.sh to generate the stats.txt file for all the configurations in experiment 3.1 and 3.2 after adding codes in run_micro.py, launch.py and run.py  . Also, generate the data table from scripts.py.

Experiment 4
<p></p>
After commented out all the ROI instructions from bench.c files, ran make to build the benchmark and then also made change in the run_micro.py. Ran sbatch submit.sh and generated the result.

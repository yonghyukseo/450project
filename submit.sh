#!/bin/bash
#
#SBATCH --cpus-per-task=8
#SBATCH --time=10:00
#SBATCH --mem=1G
export M5_PATH=/data/gem5-baseline
export LAB_PATH=$PWD
srun python3 launch.py 8

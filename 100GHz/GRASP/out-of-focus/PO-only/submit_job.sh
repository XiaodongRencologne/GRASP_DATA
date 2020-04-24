#!/bin/bash
#PBS -N CCAT-noauto2
#PBS -k eo
#PBS -q newton
#PBS -l nodes=1:ppn=40
#PBS -l walltime=320:00:00
#PBS -m bea
#PBS -M rpuddu@auc.puc.cl
#################################
### Switch to the working directory;
cd /home/rpuddu/CCAT_noautoconv_onaxis2

### Run:
module load openmpi-1.10.4
#mpirun -n 3 grasp-analysis batch.gxp
grasp-analysis batch.gxp

echo "done"

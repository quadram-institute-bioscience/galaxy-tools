#!/bin/bash
#SBATCH -p qib-short                                                   # partition
#SBATCH -c 8                                                           # 1 CPU per task
#SBATCH -t 0-02:00                                                     # 2 hour max. time-limit
#SBATCH --mail-type=ALL                                                # mail me everything
#SBATCH --mail-user=leviet@nbi.ac.uk                                   # the email
#SBATCH -o /dev/null                                                   # snub the output
#SBATCH -e /hpc-home/leviet/data/pacbio_subsample_ccs-%j.err   # print errors


srun singularity exec ~/transfer/outgoing/singularity/pacbio/pacbio.sif ccs -j 8 --logFile ccs.log --reportFile ccs.report pacbio.bam ccs.bam 

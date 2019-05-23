#!/bin/bash

chip=$1
control=$2
n_reads=$3
chip_lines=$4
control_lines=$5
noise=$6

control_subsample_lines=$(bc -l <<< $n_reads*$noise/$control_lines/10)
if [[ $control_subsample_lines = 0 ]]
  then 
    chip_subsample_lines=$(bc -l <<< $n_reads/$chip_lines)
    $sambamba_path/sambamba-0.6.9 -q view --subsampling-seed=42 -f bam -o merged$i.bam -t 4 -s $chip_subsample_lines $chip
  else
    $sambamba_path/sambamba-0.6.9 -q view --subsampling-seed=42 -f bam -o tmp_control.bam -t 4 -s $control_subsample_lines $control
    control_lines_new=$($sambamba_path/sambamba-0.6.9 -q view -t 4 -c tmp_control.bam)
    chip_subsample_lines=$(bc -l <<< $n_reads/$chip_lines-$control_lines_new/$chip_lines)
    $sambamba_path/sambamba-0.6.9 -q view --subsampling-seed=42 -f bam -o tmp_chip.bam -t 4 -s $chip_subsample_lines $chip
    $sambamba_path/sambamba-0.6.9 -q merge -t 4 merged$noise.bam tmp_chip.bam tmp_control.bam
fi

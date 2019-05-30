#!/bin/bash


sambamba_path="sambamba"

if [[ $1 == "-h" || $1 == "--help" ]]; then
  echo "Program to mix ChIP-seq and control aligned reads.
  Usage: [chip_file (.bam)] [control_file (.bam)] [n_reads]
         [n_lines_chip] [n_lines_control] [noise rate (0..9)]"
  exit 0
fi

if [[ "$#" -ne 6 ]]; then
  echo "Incorrect number of arguments (use -h for help)"
  exit 1
fi

chip=$1
control=$2
n_reads=$3
chip_lines=$4
control_lines=$5
noise=$6

control_subsample_lines=$(bc -l <<< ${n_reads}*${noise}/${control_lines}/10)

if [[ ${control_subsample_lines} = 0 ]]; then
  chip_subsample_lines=$(bc -l <<< ${n_reads}/${chip_lines})
  ${sambamba_path} view --subsampling-seed=42 -f bam -o merged${noise}.bam -t 4 -s ${chip_subsample_lines} ${chip}
else
  ${sambamba_path} view --subsampling-seed=42 -f bam -o tmp_control.bam -t 4 -s ${control_subsample_lines} ${control}
  control_lines_new=$(${sambamba_path} view -t 4 -c tmp_control.bam)
  chip_subsample_lines=$(bc -l <<< ${n_reads}/${chip_lines}-${control_lines_new}/${chip_lines})
  ${sambamba_path} view --subsampling-seed=42 -f bam -o tmp_chip.bam -t 4 -s ${chip_subsample_lines} ${chip}
  ${sambamba_path} merge -t 4 merged${noise}.bam tmp_chip.bam tmp_control.bam
fi

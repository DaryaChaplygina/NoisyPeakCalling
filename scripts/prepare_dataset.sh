#!/bin/bash


if [[ $1 == "-h" || $1 == "--help" ]]; then
  echo "Program to align data to the reference.
  Usage: [data_folder (with .fastq files)] [reference (should be in a data_folder)]"
  exit 0
fi

data_folder=$1
ref=$2

if [[ ! -d ${data_folder} ]]; then
  echo "Data folder not found! Please provide existing directory (use -h for help)"
  exit 1
fi

cd ${data_folder}

if [[ ! -f ${ref} ]]; then
  echo "Reference not found! Please check if your file exists and is in provided folder
  (use -h for help"
  exit 1
fi

bowtie2-build ${ref} ref

for f in *.fastq
  do
    echo $f
    name=$(echo ${f} | cut -d'.' -f 1)
    echo $name
    bowtie2 -x ref -U ${f} -S ${name}_aln.sam
    samtools view -bhS ${name}_aln.sam > ${name}_aln.bam
    samtools sort ${name}_aln.bam > ${name}.bam
    samtools index ${name}.bam

    rm -rf ${name}_aln.sam
    rm -rf ${name}_aln.bam
  done
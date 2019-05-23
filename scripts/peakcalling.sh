#!/bin/bash


sambamba_path="/home/dario/bioinf/tools"
sicer_path="home/dario/bioinf/tools/SICER_V1.1/SICER/SICER.sh"
span_path="/home/dario/bioinf/tools/span/span-0.11.0.build.jar"
out_dir="../data/"
span_cs="/home/dario/bioinf/tools/span/hg38.chrom.sizes"
chip=$1
control=$2
n_reads=$3
name=$4
peak_caller=$5
fdr=$6
chip_lines=$($sambamba_path/sambamba-0.6.9 -q view --subsampling-seed=42 -t 4 -c $1)
control_lines=$($sambamba_path/sambamba-0.6.9 -q view --subsampling-seed=42 -t 4 -c $2)
echo $chip_lines $control_lines

# touch result_h3k4me1.txt

for i in {0..9}
  do
    ./join_files.sh $chip $control $n_reads $chip_lines $control_lines $i
    
    if [[ $peak_caller = macs2 ]]
      then
        macs2 callpeak -t merged$i.bam -c $control -n $name_$i --outdir $out_dir$name/$peak_caller_fdr$fdr --broad -q $fdr --broad-cutoff $fdr
      elif [[ $peak_caller = sicer ]]
        bedtools bamtobed -i merged$i.bam > merged$i.bed
        control=$(echo $control | cut -d'.' -f 1)
        sh $sicer_path . merged$i.bed $control.bed . hg38 1 200 150 0.75 400 $fdr
        rm -rf merged$i.bed
        rm -rf merged$i-1-removed.bed
        rm -rf huv-1-removed.bed
      else
        java -Xmx6G -jar $span_path analyze -t merged$i.bam -c $control -f $fdr --threads 4 --cs $span_cs -p $name_$i.peak
        rm -rf logs/ 
        rm -rf cache/ 
        rm -rf fit/
        
    rm -rf *.bam
    rm -rf *.bai
  done 

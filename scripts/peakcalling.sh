#!/bin/bash


sicer_path="SICER.sh"
span_path="/home/dario/bioinf/tools/span/span-0.11.0.build.jar"
out_dir="../data/"
span_cs="/home/dario/bioinf/tools/span/hg38.chrom.sizes"

if [[ $1 == "-h" || $1 == "--help" ]]; then
  echo "Program to perform peakcalling on noisy data.
  Usage: [chip_file (.bam)] [control_file (.bam)] [n_reads]
         [name] [peakcaller (macs2|sicer|span)] [fdr]"
  exit 0
fi

if [[ "$#" -ne 6 ]]; then
  echo "Incorrect number of arguments (use -h for help)"
  exit 1
fi

chip=$1
control=$2
n_reads=$3
name=$4
peak_caller=$5
fdr=$6

case ${peak_caller} in
  macs2|sicer)
    ;;
  span)
    if [[ ! -f ${span_path} ]]; then
      echo "SPAN not found! Please check if span_path is set to existing file"
      exit 1
    elif [[ ! -f ${span_cs} ]]; then
      echo "CS file not found! Please check if span_cs is set to existing file"
      exit 1
    fi
    ;;
  *)
    echo "Unknown peak caller! Now available only MACS2, SICER and SPAN"
    exit 1
    ;;
esac

chip_lines=$(wc -l ${chip} | cut -d' ' -f 1)
control_lines=$(wc -l ${control} | cut -d' ' -f 1)

for i in {0..9}
  do
    ./join_files.sh ${chip} ${control} ${n_reads} ${chip_lines} ${control_lines} ${i}
    
    if [[ ${peak_caller} == "macs2" ]] ; then
        macs2 callpeak -t merged${i}.bam -c ${control} -n ${name}_${i} --outdir ${out_dir}${name}/${peak_caller}_fdr${fdr} --broad -q ${fdr} --broad-cutoff ${fdr}
    elif [[ ${peak_caller} == "sicer" ]] ; then
        bedtools bamtobed -i merged${i}.bam > merged${i}.bed
        control=$(echo ${control} | cut -d'.' -f 1)
        sh ${sicer_path} . merged${i}.bed ${control}.bed ${out_dir}${name}/${peak_caller}_fdr${fdr}/ hg38 1 200 150 0.75 400 ${fdr}
        rm -rf merged${i}.bed
        rm -rf merged${i}-1-removed.bed
        rm -rf huv-1-removed.bed
    else
      java -Xmx6G -jar ${span_path} analyze -t merged${i}.bam -c ${control} -f ${fdr} --threads 4 --cs ${span_cs} -p ${out_dir}${name}/${peak_caller}_fdr${fdr}/${name}_${i}.peak
      rm -rf logs/
      rm -rf cache/
      rm -rf fit/
    fi

    rm -rf *.bam
    rm -rf *.bai
  done 

# NoisyPeakCalling

## Project description

ChIP-sequencing is a method used to analyze protein interactions with DNA. The reads obtained from sequencing are mostly aligned on a regions where a protein interacts with DNA. The goal of __peak calling__ algorithm is to identify such enriched areas (__peaks__) in a genome.

According to Jung2014[$$\small{^{[1]}}$$](#jung), derived set of peaks could vary depending on sequencing depth and specific algorithm. In the paper only sequencing depth was considered; here we analyze an impact of noise in ChIP-seq data on peak calling algorithms performance.   

## Goals and objectives

The aims of the project:
1. To study ChIP-seq protocol and Jung2014 paper.
2. To acquire noisy data for an experiment.
3. To analyse the influence of noise on __MACS2__, __SICER__ and __SPAN__ peak calling algorithms.

## Methods

### Data

For experiment we choose five H3 histone modifications: [__H3K4me1__](https://www.encodeproject.org/files/ENCFF076WOE/), [__H3K4me3__](https://www.encodeproject.org/files/ENCFF001FYS/), [__H3K27ac__](https://www.encodeproject.org/files/ENCFF000CEN/), [__H3K27me3__](https://www.encodeproject.org/files/ENCFF001FYR/), [__H3K36me3__](https://www.encodeproject.org/files/ENCFF000CFB/), control files [ENCFF825XKT](https://www.encodeproject.org/files/ENCFF825XKT/) (for H3K4me1), [ENCFF001HUV](https://www.encodeproject.org/files/ENCFF001HUV/) (for H3K4me3 and H3K27me3), [ENCFF692GVG](https://www.encodeproject.org/files/ENCFF692GVG/) (for H3K27ac and H3K36me3) and [reference](https://www.encodeproject.org/files/GRCh38_no_alt_analysis_set_GCA_000001405.15/) for alignment. All the files were obtained from the ENCODE project[$$\small{^{[2]}}$$](#encode) site. Biosample is human CD14-positive monocyte cells. 

We use:
- bowtie2 (version 2.3.4.3) for reads alignment;
- samtools (1.9) for sorting and filtering;
- bamCoverage from deeptools package (version 3.2.1) to obtain bigWig files;
- bamtobed from bedtools package (version 2.26.0) to obtain bed files from alignment.

All the commands have standart settings.

### Project scripts

`peakcalling.sh`  takes as input _[chip]_ _[control]_ _[n_reads]_ _[name]_ _[peakcaller]_ _[fdr]_, where
- _chip_ is aligned chip-seq reads
- _control_ is aligned control reads
- _n_reads_ is number of reads to choose for experiment (should be less then number of reads both in chip and control)
- _name_ is a name for output file (recommended to be a modification name)
- _peakcaller_ is a peakcalling algorithm (now available macs2, sicer and span)

It mixes the reads from _chip_ and _control_ in proportion from 0% to 90% of control and runs _peakcaller_ on mixed file. Now it is possible to choose only _fdr_ parameter for running. 

`signal_to_noise_estimation.py` takes as input _[file]_ _[-d fragment_size]_  _[OPTIONS]_, where
- _[file]_ is a path to file in .bam format
- _-d_ is a size of chip fragment (you could obtain it from macs2 logs, for example)

The script counts signal-to-noise ratio as ratio of 90 to 10 percentiles of genome bin coverage distribution (90 to 10 is default settings, but I recommend you to set first number to larger value, like 95% or 99%).

`result_visualization.py` is a set of functions that draw plots with different statistics of result data. Running `$ python3  result_visualization.py` would draw the main results graphs. All the pictures available in /result/ folder

`project_structure.py` and `jbr_gb_data.py` are necessary for result visualisation and contains structure of folders with peak calling data and tracks overlapping data from JBR Genome browser respectively.

`peaks_dynamics.py` contains the set of functions for calculating different statistics, necessary for result visualization.

`join_files.sh` is a supplementary script, that is runned by `peakcalling.sh` to mix chip and control with specified proportion.

## Results

## References 

<a name="jung">[1]</a>  Jung YL, Luquette LJ, Ho JW, et al. Impact of sequencing depth in ChIP-seq experiments. Nucleic Acids Res. 2014;42(9):e74. doi:10.1093/nar/gku178

<a name="encode">[2]</a>  Encyclopedia of DNA Elements. https://www.encodeproject.org/

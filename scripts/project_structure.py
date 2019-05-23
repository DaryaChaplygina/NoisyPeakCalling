"""
contains the pathes to data of noisy peak calling
files could be obtained via ./peakcalling.sh script
"""

fdr_05_path = {
    'h3k4me1' : [['../data/h3k4me1/macs2_fdr_0.05/', '.broadPeak'],
                 ['../data/h3k4me1/sicer_fdr_0.05/', 'summary-FDR0.05.bed'],
                 ['../data/h3k4me1/span_fdr_0.05/', '.peak']],
    'h3k4me3' : [['../data/h3k4me3/macs2_fdr_0.05/', '.broadPeak'],
                 ['../data/h3k4me3/sicer_fdr_0.05/', 'summary-FDR0.05.bed'],
                 ['../data/h3k4me3/span_fdr_0.05/', '.peak']],
    'h3k27ac' : [['../data/h3k27ac/macs2_fdr_0.05/', '.broadPeak'],
                 ['../data/h3k27ac/sicer_fdr_0.05/', 'summary-FDR0.05.bed'],
                 ['../data/h3k27ac/span_fdr_0.05/', '.peak']],
    'h3k27me3' : [['../data/h3k27me3/macs2_fdr_0.05/', '.broadPeak'],
                  ['../data/h3k27me3/sicer_fdr_0.05/', 'summary-FDR0.05.bed'],
                  ['../data/h3k27me3/span_fdr_0.05/', '.peak']],
    'h3k36me3' : [['../data/h3k36me3/macs2_fdr_0.05/', '.broadPeak'],
                  ['../data/h3k36me3/sicer_fdr_0.05/', 'summary-FDR0.05.bed'],
                  ['../data/h3k36me3/span_fdr_0.05/', 'peak']]
}

fdr_e6_path = {
    'h3k4me1' : [['../data/h3k4me1/h3k4me1_macs2_fdr_1e-6/', '.broadPeak'],
                 ['../data/h3k4me1/sicer_fdr_-6/', 'summary-FDR0.000001.bed'],
                 ['../data/h3k4me1/span_fdr_-6/', '.peak']],
    'h3k4me3' : [['../data/h3k4me3/h3k4me3_macs2_fdr_1e-6/', '.broadPeak'],
                 ['../data/h3k4me3/sicer_fdr_1e-6/', 'summary-FDR0.000001.bed'],
                 ['../data/h3k4me3/span_fdr_1e-6/', '.peak']],
    'h3k27ac' : [['../data/h3k27ac/h3k27ac_macs2_fdr_1e-6/', '.broadPeak'],
                 ['../data/h3k27ac/sicer_fdr-6/', 'summary-FDR0.000001.bed'],
                 ['../data/h3k27ac/span_fdr-6/', '.peak']],
    'h3k27me3' : [['../data/h3k27me3/h3k27me3_macs2_fdr_1e-6/', '.broadPeak'],
                  ['../data/h3k27me3/sicer_fdr_1e-6/', 'summary-FDR0.000001.bed'],
                  ['../data/h3k27me3/span_fdr_1e-6/', '.peak']],
    'h3k36me3' : [['../data/h3k36me3/h3k36me3_macs2_fdr_1e-6/', '.broadPeak'],
                  ['../data/h3k36me3/sicer_fdr_1e-6/', 'summary-FDR0.000001.bed'],
                  ['../data/h3k36me3/span_fdr_1e-6/', 'peak']]
} 

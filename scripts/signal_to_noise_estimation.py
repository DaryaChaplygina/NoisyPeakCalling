import pysam
import numpy as np
import argparse 


bin_default = 200


def SNR_count(filepath, fragment_size, bin_size, percentiles):
    counts = bin_coverage(filepath, fragment_size, bin_size)[1:]
    snrs = []
    for i in range(0, len(percentiles), 2):
        noise = get_quantie_from_freqs(percentiles[i], counts) + 1
        signal = get_quantie_from_freqs(percentiles[i + 1], counts) + 1
        snrs.append(signal / noise)
    
    return snrs
    

def bin_coverage(filepath, fragment_size, bin_size):
    bins = []
    counts = [0 for _ in range(1000)]
    curr_ref = ''
    
    bf = pysam.AlignmentFile(filepath, 'rb')

    for read in bf.fetch():
        if read.reference_name != curr_ref:
            bins_lens = [len(b) for b in bins]
            cs, ns = np.unique(bins_lens, return_counts=True)
            for i in range(len(cs)):
                if cs[i] >= len(counts):
                    for j in range(cs[i] - len(counts) + 1):
                        counts.append(0)
                counts[cs[i]] += ns[i]
            
            curr_ref = read.reference_name
            bins = [set() for _ in range(
                    bf.lengths[bf.references.index(read.reference_name)] // bin_size + 1)]
            
    #     skipped = len(read.seq) - read.query_alignment_start
    #     pos = read.reference_start - skipped
        pos = 0
        if read.is_reverse:
            pos = read.reference_end - fragment_size // 2
        else:
            pos = read.reference_start + fragment_size // 2
            
        try:
            bins[pos // bin_size].add(pos % bin_size)
        except:
            continue 
    
    return counts


def get_quantie_from_freqs(q, freqs):
    idx = 0
    for c in range(len(freqs)):
        if freqs[c] != 0:
            idx = c
            
    sum_ = sum(freqs[:idx + 1])
    k = int(q * (sum_ - 1))
    i = -1
    
    curr_sum = 0
    while curr_sum / sum_ < q and i < idx:
        i += 1 
        curr_sum += freqs[i]
        
    return i


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count signal-to-noise ratio in given bam file (index required)")
    parser.add_argument(dest='filepath', type=str, help='file in .bam format')
    parser.add_argument('-d', dest='fragment_size', type=int, help='fragment size')
    parser.add_argument('--bin_size', dest='bin_size', type=int, default=200,
                        help=f'bin size for coverage counting (DEFAULT: {bin_default})')
    parser.add_argument('--percentiles', dest='percentiles', nargs='+', type=float, default=[0.1,0.9],
                        help=f'comma-separated list of p1,p2 - quantiles for estimating SNR, p1<p2. Must have length 2N.'
                             f'In case of N > 1 SNR will be returned as space-separated list of values.'
                             f'(DEFAULT: [0.1, 0.9])')
    args = parser.parse_args()
    
    if args.fragment_size is None:
        raise Exception("fragment size is required")
    if len(args.percentiles) % 2 != 0:
        raise Exception("you should provide 2N percentiles")
    for i in range(0, len(args.percentiles), 2):
        if args.percentiles[i] >= args.percentiles[i + 1]:
            raise Exception("all pairs of percentiles should be in ascending order")
        
   # print(args.filepath, args.fragment_size, args.bin_size, args.percentiles)
    res = SNR_count(args.filepath, args.fragment_size, args.bin_size, args.percentiles)
    print(res)
    

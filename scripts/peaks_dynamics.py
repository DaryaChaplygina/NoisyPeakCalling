import os
import numpy as np

def full_peak_dynamics(files):
    # takes list of files in .bed format and returns summary peak statistics for each
    n_peaks = []
    mean_len = []
    n_splitted = []
    n_united = []
    
    prev_peaks = read_peaks(files[0])
    n_peaks.append(prev_peaks.shape[0])
    mean_len.append(np.mean(prev_peaks[:, 2] - prev_peaks[:, 1]))
    
    for i in range(1, len(files)):
        peaks = read_peaks(files[i])
        mean_len.append(np.mean(peaks[:, 2] - peaks[:, 1]))
        n_peaks.append(peaks.shape[0])
        
        curr_splitted = 0
        curr_united = 0
        splitted = cover(prev_peaks, peaks)
        n_splitted.append(np.count_nonzero(splitted > 1))
        united = cover(peaks, prev_peaks)
        n_united.append(np.count_nonzero(united > 1))
        
        prev_peaks = peaks.copy()
        
    if len(mean_len) < 10:
        for _ in range(len(mean_len), 10):
            n_splitted.append(0)
            n_united.append(0)
            n_peaks.append(0)
            mean_len.append(0)
    
    return n_splitted, n_united, n_peaks, mean_len


def peak_dynamics(folder, file_end, ind):
    # returns only statistics of number of peaks and average peak length dynamics 
    filenames = get_filenames(folder, file_end, ind)
    
    ns, mean_lens = [], []
    for f in filenames:
        p = read_peaks(f)
        ns.append(p.shape[0])
        mean_lens.append(np.mean(p[:, 2] - p[:, 1]))
    
    return ns, mean_lens

def read_peaks(fname):
    # takes file in .bed format as input and returns array of [chrom, peak_start, peak_end] 
    peaks = []
    line_splitted = []
    lens = []
    
    with open(fname) as f:
        chr_ = ''
        for line in f:
            line_splitted = line.split('\t')
            if line_splitted[0][3:].isdigit() or line_splitted[0][3:] in ['X', 'Y']:
                if line_splitted[0][3:].isdigit():
                    chr_ = int(line_splitted[0][3:])
                else:
                    chr_ = 23 if line_splitted[0][3:] == 'X' else 24
                peaks.append([chr_, int(line_splitted[1]), int(line_splitted[2])])
    return np.asarray(peaks)

def cover(peaks1, peaks2):
    # returns array of shape (peaks1.shape[0], ) with number of peaks from peaks2 that are embedded in peak from peaks1
    curr_chr = peaks1[0][0]
    idx1 = 0
    N1 = peaks1.shape[0]
    res = np.zeros(peaks1.shape[0])
    
    def __move_chrom(idx, peak):
        while peaks1[idx, 0] != peak[0] and idx + 1 < N1:
            if peaks1[idx, 0] > int(peak[0]):
                break
            
            idx += 1
        if idx + 1 == N1:
            return -1
        else:
            return idx
        
    def __move_start(idx, thr, chrom):
        while peaks1[idx, 0] == chrom and idx + 1 < N1 and peaks1[idx, 1] <= thr:
            idx += 1
            
        if idx + 1 == N1:
            return -1
        else:
            return idx
        
    def __move_end(idx, thr, chrom):
        while peaks1[idx, 0] == chrom and idx + 1 < N1 and peaks1[idx, 2] < thr:
            idx += 1
        if idx + 1 == N1:
            return -1
        else:
            return idx
    
    for peak in peaks2:
        if peak[0] == peaks1[idx1, 0]:
            if peaks1[idx1, 1] <= peak[1] and peaks1[idx1, 2] >= peak[2]:
                res[idx1] += 1
            
            elif peaks1[idx1, 1] > peak[1]:
                if peaks1[idx1, 1] <= peak[2]:
                    idx1 = __move_start(idx1, peak[2], peak[0])
                    if idx1 == -1:
                        break
                        
            else:
                if peaks1[idx1, 2] < peak[1]:
                    idx1 = __move_end(idx1, peak[2], peak[0])
                    if idx1 == -1:
                        break
                    if peaks1[idx1, 1] <= peak[1]:
                        res[idx1] += 1
                    else:
                        __move_start(idx1, peak[2], peak[0])
        else:
            idx1 = __move_chrom(idx1, peak)
            if idx1 == -1:
                break
    return res


def get_filenames(folder, file_end, ind=[i for i in range(10)]):
    filenames = []
    for f in os.listdir(folder):
        if f.endswith(file_end):
            if not '10' in f:
                filenames.append(folder + f)
                
    filenames = sorted(filenames)
    filenames_ = []
    for i in ind:
        filenames_.append(filenames[i])
    
    return filenames_

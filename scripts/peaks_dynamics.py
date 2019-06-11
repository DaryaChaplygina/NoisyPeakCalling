import os
import re
import numpy as np
import pandas as pd


def full_peak_dynamics(files):
    """
    Takes list of files in .bed format and returns 4 arrays with
    summary peaks statistics:
    number of peaks, splitted with increasing level of noise
    number of peaks, united with increasing level of noise
    number of peaks
    average peak length
    """
    n_peaks = np.zeros(10)
    mean_len = np.zeros(10)
    n_splitted = np.zeros(10)
    n_united = np.zeros(10)

    prev_peaks = read_peaks(files[0])
    prev_peaks = prev_peaks[np.lexsort((prev_peaks[:, 1], prev_peaks[:, 0]))]
    n_peaks[0] = prev_peaks.shape[0]
    mean_len[0] = np.mean(prev_peaks[:, 2] - prev_peaks[:, 1])

    for i, file in enumerate(files):
        peaks = read_peaks(file)
        peaks = peaks[np.lexsort((peaks[:, 1], peaks[:, 0]))]
        mean_len[i] = np.mean(peaks[:, 2] - peaks[:, 1])
        n_peaks[i] = peaks.shape[0]

        splitted = cover(prev_peaks, peaks)
        n_splitted[i] = np.count_nonzero(splitted > 1)
        united = cover(peaks, prev_peaks)
        n_united[i] = np.count_nonzero(united > 1)

        prev_peaks = peaks.copy()

    return n_splitted, n_united, n_peaks, mean_len


def peak_dynamics(folder, file_end, ind):
    """
    Takes list of files in .bed format and returns 2 arrays with
    summary peaks statistics:
    number of peaks
    average peak length
    """
    filenames = get_filenames(folder, file_end, ind)

    ns, mean_lens = np.zeros(len(ind)), np.zeros(len(ind))
    for i, file in enumerate(filenames):
        peaks = read_peaks(file)
        ns[i] = peaks.shape[0]
        mean_lens[i] = np.mean(peaks[:, 2] - peaks[:, 1])

    return ns, mean_lens


def read_peaks(fname):
    """
    Takes file in .bed format as input and
    returns array of [chrom, peak_start, peak_end]
    """
    bed_file = pd.read_csv(fname, sep='\t', header=None)

    def chrom_parser(s):
        m = re.match('chr([0-9]+|[XY])', s)
        if m is None:
            return None
        else:
            if m.group(1).isdigit():
                return int(m.group(1))
            else:
                return 23 if m.group(1) == 'X' else 24

    bed_file[0] = bed_file[0].apply(chrom_parser)
    bed_file.dropna(how='any', inplace=True)

    peaks = bed_file[[0, 1, 2]].values
    return peaks


def cover(peaks1, peaks2):
    """
    Returns array of shape (peaks1.shape[0], ) res,
    where res[i] = n means that ith peak from peaks1
    contains n peaks from peaks2
    """
    curr_chr = peaks1[0][0]
    idx1 = 0
    N1 = peaks1.shape[0]
    res = np.zeros(peaks1.shape[0])

    def move_chrom(idx, peak):
        while peaks1[idx, 0] != peak[0] and idx + 1 < N1:
            if peaks1[idx, 0] > peak[0]:
                break
            idx += 1

        if idx + 1 == N1:
            return -1
        else:
            return idx

    def move_peak_coord(idx, other_chrom, thr, coord, comp):
        while (peaks1[idx, 0] == other_chrom and idx + 1 < N1 and
                comp(peaks1[idx, coord], thr)):
            idx += 1

        if idx + 1 == N1:
            return -1
        else:
            return idx

    for peak in peaks2:
        if peak[0] < peaks1[idx1, 0]:
            idx1 = move_chrom(idx1, peak)
            if idx1 == -1:
                break

        if peak[0] == peaks1[idx1, 0]:
            if peaks1[idx1, 1] <= peak[1] and peaks1[idx1, 2] >= peak[2]:
                # peaks1 : |..........|
                # peaks2 :  |........|
                res[idx1] += 1

            elif peaks1[idx1, 1] > peak[1]:
                # peaks1 :    |.....
                # peaks2 : |........
                if peaks1[idx1, 1] <= peak[2]:
                    idx1 = move_peak_coord(idx1, peak[0], peak[2], 1, lambda x, y: x <= y)
                    if idx1 == -1:
                        break

            else:
                # peaks1 : ...|
                # peaks2 : ......|
                if peaks1[idx1, 2] < peak[1]:
                    idx1 = move_peak_coord(idx1, peak[0], peak[2], 2, lambda x, y: x < y)
                    if idx1 == -1:
                        break
                    if peaks1[idx1, 1] <= peak[1]:
                        res[idx1] += 1
                    else:
                        move_peak_coord(idx1, peak[0], peak[2], 1, lambda x, y: x <= y)
                else:
                    move_peak_coord(idx1, peak[0], peak[2], 1, lambda x, y: x <= y)
    return res


def get_filenames(folder, file_end, ind=range(10)):
    """
    Returns list of noisy peak calling files from folder
    in order of increasing noise rate
    """
    filenames = []
    for f in os.listdir(folder):
        if f.endswith(file_end):
            if "10" not in f:
                filenames.append(folder + f)

    filenames = sorted(filenames)
    filenames_ = []
    for i in ind:
        filenames_.append(filenames[i])

    return filenames_

class AlgorithmsStats:
    """
    This class holds the data from overlapping tracks in JBR Genome Browser.
    The data could be obtained by loading output from ./peakcalling.sh
    into JBR Genome Browser.
    To get pc_stability_data one should select tracks from the same
    algorithm and histone modification with noise level from 0% to 90%
    and choose "Overlap info for N track...".
    pc_similarity_data could be obtained from overlapping tracks of
    three algorithms for the same histone modification and
    level of noise (0% and 50% separately).
    The source pictures with overlapping percent could be found
    in folder /pics/.
    """

    pc_stability_data = {
        "FDR 1E-6": {
            "macs2": {
                "h3k4me1": [
                    100, 90.03, 77.89, 66.78, 54.08,
                    41.12, 27.28, 12.96, 3.54, 0,
                ],
                "h3k4me3": [
                    100, 95.62, 91.24, 86.3, 81.51,
                    76.31, 70.56, 63.13, 52.4, 27.9,
                ],
                "h3k27ac": [
                    100, 89.18, 79.25, 69.52, 59.73,
                    49.53, 38.25, 26.28, 12.73, 0,
                ],
                "h3k27me3": [
                    100, 78.04, 60.18, 43.68, 26.32,
                    13.24, 2.79, 0.1, 0.01, 0,
                ],
                "h3k36me3": [
                    100, 81.23, 64.14, 46.59, 27.0,
                    12.89, 4.48, 0, 0, 0,
                ],
            },
            "sicer": {
                "h3k4me1": [
                    100, 95.05, 90.03, 84.1, 77.61,
                    69.56, 59.33, 46.04, 29.3, 10.15,
                ],
                "h3k4me3": [
                    100, 94.66, 89.96, 84.81, 79.94,
                    74.92, 69.87, 63.72, 56.45, 43.1,
                ],
                "h3k27ac": [
                    100, 91.14, 83.89, 76.32, 68.6,
                    51.38, 41.91, 30.49, 14.9, 0,
                ],
                "h3k27me3": [
                    100, 81.4, 67.25, 55.33, 44.43,
                    34.77, 26.55, 18.97, 10.56, 1.3,
                ],
                "h3k36me3": [
                    100, 91.98, 85.14, 77.82, 69.3,
                    59.6, 49.15, 36.99, 23.0, 5.04,
                ],
            },
            "span": {
                "h3k4me1": [
                    100, 97.13, 92.97, 87.57, 83.61,
                    79.76, 79.39, 63.68, 53.55, 33.68,
                ],
                "h3k4me3": [
                    100, 96.61, 93.92, 91.42, 88.44,
                    84.58, 80.3, 75.09, 67.96, 59.69,
                ],
                "h3k27ac": [
                    100, 91.09, 84.85, 80.29, 74.38,
                    66.58, 62.25, 52.37, 46.99, 32.62,
                ],
                "h3k27me3": [
                    100, 87.78, 79.07, 70.02, 59.73,
                    53.52, 38.02, 30.42, 24.92, 13.73,
                ],
                "h3k36me3": [
                    100, 93.91, 89.68, 84.31, 78.38,
                    71.3, 64.38, 57.45, 47.97, 28.43,
                ],
            },
        },
        "FDR 0.05": {
            "macs2": {
                "h3k4me1": [
                    100, 93.18, 87.09, 80.56, 73.12,
                    63.53, 52.98, 36.58, 19.32, 0,
                ],
                "h3k4me3": [
                    100, 94.88, 90.37, 85.33, 80.35,
                    74.93, 69.4, 62.79, 54.96, 40.57,
                ],
                "h3k27ac": [
                    100, 86.91, 75.75, 63.52, 54.47,
                    45.69, 36.99, 27.8, 16.84, 0.59,
                ],
                "h3k27me3": [
                    100, 79.59, 62.82, 48.61, 35.61,
                    22.65, 13.34, 5.94, 0.36, 0,
                ],
                "h3k36me3": [
                    100, 88.36, 70.29, 60.99, 49.36,
                    37.36, 26.67, 0.32, 0, 0
                ],
            },
            "sicer": {
                "h3k4me1": [
                    100, 95.46, 90.98, 86.0, 80.24,
                    73.59, 65.1, 54, 39.34, 19.73,
                ],
                "h3k4me3": [
                    100, 95.3, 91.58, 86.89, 82.67,
                    77.82, 72.89, 67.82, 61.57, 51.9,
                ],
                "h3k27ac": [
                    100, 91.48, 84.41, 77.45, 70.47,
                    62.85, 54.45, 45.39, 34.22, 19.06,
                ],
                "h3k27me3": [
                    100, 83.28, 71.11, 61.14, 51.62,
                    42.38, 34.2, 26.21, 18.13, 6.51,
                ],
                "h3k36me3": [
                    100, 92.3, 85.85, 78.94, 71.24,
                    62.39, 52.75, 41.01, 27.18, 9.83,
                ],
            },
            "span": {
                "h3k4me1": [
                    100, 96.23, 93.64, 90.36, 87.12,
                    83.58, 78.74, 73.61, 71.05, 59.04,
                ],
                "h3k4me3": [
                    100, 96.28, 93.26, 90.56, 87.45,
                    83.54, 79.48, 74.45, 67.34, 59.51,
                ],
                "h3k27ac": [
                    100, 91.82, 86.21, 82.69, 77.95,
                    71.22, 66.89, 59.25, 59.7, 49.74,
                ],
                "h3k27me3": [
                    100, 90.86, 83.77, 75.34, 64.36,
                    57.27, 45.16, 35.57, 34.41, 33.07,
                ],
                "h3k36me3": [
                    100, 94.7, 91.44, 88.35, 85.25,
                    82.62, 79.68, 78.48, 70.2, 64.13,
                ],
            },
        },
    }

    pc_similarity_data = {
        "FDR 0.05": {
            "macs2": {
                "sicer": {
                    "h3k4me1": [97.85, 93.01],
                    "h3k4me3": [91.8, 92.68],
                    "h3k27ac": [88.36, 82.86],
                    "h3k27me3": [59.3, 44.92],
                    "h3k36me3": [93.56, 77.63],
                },
                "span": {
                    "h3k4me1": [81.03, 67.05],
                    "h3k4me3": [77.18, 71.91],
                    "h3k27ac": [78.68, 64.8],
                    "h3k27me3": [40.62, 23.8],
                    "h3k36me3": [79.97, 49.09],
                },
            },
            "sicer": {
                "macs2": {
                    "h3k4me1": [92.51, 92.27],
                    "h3k4me3": [96.18, 95.89],
                    "h3k27ac": [92.33, 94.32],
                    "h3k27me3": [93.83, 98.39],
                    "h3k36me3": [93.67, 96.92],
                },
                "span": {
                    "h3k4me1": [73.96, 64.23],
                    "h3k4me3": [79.94, 73.88],
                    "h3k27ac": [76.6, 68.66],
                    "h3k27me3": [56.09, 44.25],
                    "h3k36me3": [73.1, 56.36],
                },
            },
            "span": {
                "macs2": {
                    "h3k4me1": [99.99, 100],
                    "h3k4me3": [99.99, 100],
                    "h3k27ac": [99.28, 99.93],
                    "h3k27me3": [99.89, 100],
                    "h3k36me3": [99.56, 100],
                },
                "sicer": {
                    "h3k4me1": [99.99, 99.98],
                    "h3k4me3": [99.41, 99.86],
                    "h3k27ac": [98.49, 98.84],
                    "h3k27me3": [98.38, 99.11],
                    "h3k36me3": [99.39, 99.79],
                },
            },
        },
        "FDR 1E-6": {
            "macs2": {
                "sicer": {
                    "h3k4me1": [69.82, 46.47],
                    "h3k4me3": [82.54, 88.38],
                    "h3k27ac": [52.92, 51.36],
                    "h3k27me3": [23.1, 13.59],
                    "h3k36me3": [41.7, 16.53],
                },
                "span": {
                    "h3k4me1": [68.48, 38.81],
                    "h3k4me3": [73.93, 69.92],
                    "h3k27ac": [61.76, 51.23],
                    "h3k27me3": [24.53, 8.15],
                    "h3k36me3": [40.03, 11.71],
                },
            },
            "sicer": {
                "macs2": {
                    "h3k4me1": [99.94, 99.96],
                    "h3k4me3": [99.72, 98.94],
                    "h3k27ac": [99.96, 99.97],
                    "h3k27me3": [99.27, 99.6],
                    "h3k36me3": [99.99, 99.97],
                },
                "span": {
                    "h3k4me1": [96.86, 84.35],
                    "h3k4me3": [89.57, 79.16],
                    "h3k27ac": [99.32, 94.9],
                    "h3k27me3": [93.04, 69.56],
                    "h3k36me3": [96.57, 80.69],
                },
            },
            "span": {
                "macs2": {
                    "h3k4me1": [100, 100],
                    "h3k4me3": [100, 100],
                    "h3k27ac": [100, 100],
                    "h3k27me3": [100, 100],
                    "h3k36me3": [100, 100],
                },
                "sicer": {
                    "h3k4me1": [97.85, 99.62],
                    "h3k4me3": [99.7, 99.99],
                    "h3k27ac": [78.08, 89.15],
                    "h3k27me3": [70.25, 95.27],
                    "h3k36me3": [89.06, 98.48],
                },
            },
        },
    }

    def get_pc_histone_stability(self, peak_caller, pc_params, histone):
        """
        Returns percentage of true peaks obtained by running
        algorithm peak_caller with parameters pc_params on file histone
        with level of noise from 0% to 90%
        """
        return self.pc_stability_data[pc_params][peak_caller][histone]

    def get_pc_stability(self, peak_caller, pc_params, histones):
        """
        Returns percentage of true peaks obtained by running
        algorithm peak_caller with parameters pc_params on files,
        listed in histones, with level of noise from 0% to 90%
        """
        res = []
        for h in histones:
            res.append(self.get_pc_histone_stability(peak_caller, pc_params, h))

        return res

    def get_pc_histone_similarity(self, peak_callers, pc_params, histone):
        """
        Returns percentage of peaks from peak_callers[1]
        that are embedded into peaks from peak_callers[0], with
        both algorithms having parameters pc_params and running on
        file histone
        """
        return self\
            .pc_similarity_data[pc_params][peak_callers[0]][peak_callers[1]][histone]

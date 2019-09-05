from scripts.peaks_dynamics import *


def test_simple_coverage(load_data):
    p1 = load_data[0]
    p2 = load_data[1]
    assert cover(p1, p2) == np.asarray([1])
    assert cover(p2, p1) == np.asarray([1])

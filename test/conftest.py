import pytest
from scripts.peaks_dynamics import read_peaks


@pytest.fixture(autouse=True)
def load_data():
    noise0 = read_peaks('data/test/noise0.bed')
    noise1 = read_peaks('data/test/noise1.bed')
    return noise0, noise1

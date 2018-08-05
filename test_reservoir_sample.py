import unittest
from collections import Counter

from reservoir_sample import ReservoirSample


class TestMain(unittest.TestCase):

    def test_reservoir_sample(self):
        samples = []
        for i in range(10000):
            sample = []
            rs = ReservoirSample(3)
            for item in range(1, 11):
                sample = rs.feed(item)
            samples.extend(sample)
        r = Counter(samples)
        print(r)

if __name__ == '__main__':
    unittest.main()

import unittest
from nepali_g2p.nepali_g2p import NepaliG2P

class TestNepaliG2P(unittest.TestCase):
    def setUp(self):
        self.g2p = NepaliG2P()

    def test_nepali_to_phonemes(self):
        self.assertEqual(self.g2p.to_phonemes("नमस्ते"), "namastē")
        self.assertEqual(self.g2p.to_phonemes("हामी नेपाली हौं"), "hāmī nēpālī hauṁ")
        self.assertEqual(self.g2p.to_phonemes("सानो घरमा स-साना लड्डू छन्"), "sānō gharamā sa-sānā laḍḍū chan")
        self.assertEqual(self.g2p.to_phonemes("भगवानको इच्छा"), "bhagavānakō icchā")

    def test_nepali_to_phonemes_simple(self):
        self.assertEqual(self.g2p.to_phonemes_simple("नमस्ते"), "nmstē")
        self.assertEqual(self.g2p.to_phonemes_simple("हामी नेपाली हौं"), "hāmī nēpālī hauṁ")
        self.assertEqual(self.g2p.to_phonemes_simple("सानो घरमा स-साना लड्डू छन्"), "sānō ghrmā s-sānā lḍḍū chn")
        self.assertEqual(self.g2p.to_phonemes_simple("भगवानको इच्छा"), "bhgvānkō icchā")

if __name__ == '__main__':
    unittest.main()

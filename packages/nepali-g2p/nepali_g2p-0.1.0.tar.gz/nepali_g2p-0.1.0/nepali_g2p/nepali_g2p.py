from aksharamukha import transliterate

class NepaliG2P:
    def __init__(self):
        self.nepali_g2p = {
            "क": "k",
            "ख": "kh",
            "ग": "g",
            "घ": "gh",
            "ङ": "ŋ",
            "च": "c",
            "छ": "ch",
            "ज": "j",
            "झ": "jh",
            "ञ": "ñ",
            "ट": "ṭ",
            "ठ": "ṭh",
            "ड": "ḍ",
            "ढ": "ḍh",
            "ण": "ṇ",
            "त": "t",
            "थ": "th",
            "द": "d",
            "ध": "dh",
            "न": "n",
            "प": "p",
            "फ": "ph",
            "ब": "b",
            "भ": "bh",
            "म": "m",
            "य": "y",
            "र": "r",
            "ल": "l",
            "व": "v",
            "श": "ś",
            "ष": "ṣ",
            "स": "s",
            "ह": "h",
            "क्ष": "ksh",
            "त्र": "tra",
            "ज्ञ": "gya",
            "ा": "ā",
            "ि": "i",
            "ी": "ī",
            "ु": "u",
            "ू": "ū",
            "े": "ē",
            "ै": "ai",
            "ो": "ō",
            "ौ": "au",
            "ं": "ṁ",
            "ँ": "̃",
            "ः": "ḥ",
            "ृ": "ṛ",
            "ॄ": "ṝ",
            "ॢ": "ḷ",
            "ॣ": "ḹ",
            "अ": "a",
            "आ": "ā",
            "इ": "i",
            "ई": "ī",
            "उ": "u",
            "ऊ": "ū",
            "ए": "e",
            "ऐ": "ai",
            "ओ": "ō",
            "औ": "au",
            "ॲ": "ô",
            "अं": "am",
            "अः": "aha",
            "्": "",  # Removing the Virama character to avoid unexpected output
        }

        # if the character is followed by another haracter except of vowels
        self.nepali_g2p_vowels = {
            "क": "ka",
            "ख": "kha",
            "ग": "ga",
            "घ": "gha",
            "ङ": "ŋ",
            "च": "ca",
            "छ": "cha",
            "ज": "ja",
            "झ": "jha",
            "ञ": "ñ",
            "ट": "ṭa",
            "ठ": "ṭha",
            "ड": "ḍa",
            "ढ": "ḍha",
            "ण": "ṇa",
            "त": "ta",
            "थ": "tha",
            "द": "da",
            "ध": "dha",
            "न": "na",
            "प": "pa",
            "फ": "pha",
            "ब": "ba",
            "भ": "bha",
            "म": "ma",
            "य": "ya",
            "र": "ra",
            "ल": "la",
            "व": "va",
            "श": "śa",
            "ष": "ṣa",
            "स": "sa",
            "ह": "ha",
            "क्ष": "ksha",
            "त्र": "tra",
            "ज्ञ": "gya",
        }
        # 

    def to_phonemes(self, text: str) -> str:
        return transliterate.process('Devanagari', 'ISO', text)

    def to_phonemes_simple(self, text: str) -> str:
        syllables = self.split_syllables(text)
        phonemes = [self.syllable_to_phoneme(syllable) for syllable in syllables]
        return "".join(phonemes)

    def split_syllables(self, text: str) -> list:
        syllables = []
        current_syllable = ""
        for char in text:
            if char in self.nepali_g2p or char == "्":
                if current_syllable:
                    syllables.append(current_syllable)
                    current_syllable = ""
            current_syllable += char
        if current_syllable:
            syllables.append(current_syllable)
        return syllables

    def syllable_to_phoneme(self, syllable: str) -> str:
        phonemes = []
        previous_char = ""
        virama = False
        for char in syllable:
            if char == "्":
                virama = True
                continue

            if virama:
                if previous_char + char in self.nepali_g2p:
                    phonemes.pop()
                    phonemes.append(self.nepali_g2p[previous_char + char])
                else:
                    phonemes.append(self.nepali_g2p[char])
                virama = False

            elif char in self.nepali_g2p:
                if (
                    previous_char
                    and previous_char in self.nepali_g2p
                    and not self.is_vowel(previous_char)
                    and self.is_vowel(char)
                ):
                    phonemes.pop()
                    phonemes.append(self.nepali_g2p[previous_char + char])
                else:
                    phonemes.append(self.nepali_g2p[char])
            else:
                phonemes.append(char)  # Unrecognized characters

            previous_char = char
        return "".join(phonemes)

    def is_vowel(self, char: str) -> bool:
        return char in ["ा", "ि", "ी", "ु", "ू", "े", "ै", "ो", "ौ", "ृ", "ॄ", "ॢ", "ॣ"]


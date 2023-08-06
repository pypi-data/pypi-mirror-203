# Nepali G2P Conversion Library
This is a simple Nepali grapheme-to-phoneme (G2P) conversion library that converts Nepali text to its phonetic representation using a predefined mapping of Nepali characters to their corresponding phonemes.

# Usage
You can use the NepaliG2P class in nepali_g2p.py to convert Nepali text to phonemes. Here's an example:

```
from nepali_g2p import NepaliG2P

nepali_g2p = NepaliG2P()
nepali_text = "नमस्ते"
phonemes = nepali_g2p.convert(nepali_text)
print(phonemes)
```

This will output:

```
nəməste
```

Note that this library is not perfect and may not accurately represent the pronunciation of all Nepali words.

Dependencies
This library has no external dependencies.

License
This library is licensed under the MIT License.

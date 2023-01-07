diacritics = {
    "ā": "a",
    "ī": "i",
    "ū": "u",
    "ṛ": "ri",
    "ṝ": "ri",
    "ḷ": "li",
    "ḹ": "li",
    "ē": "e",
    "ō": "o",
    "ṃ": "m",
    "ḥ": "h",
    "ṅ": "n",
    "ñ": "n",
    "ṭ": "t",
    "ḍ": "d",
    "ṇ": "n",
    "ś": "sh",
    "ṣ": "sh",
    "ḻ": "l",
    "Ā": "a",
    "Ī": "i",
    "Ū": "u",
    "Ṛ": "ri",
    "Ṝ": "ri",
    "Ḷ": "li",
    "Ḹ": "li",
    "Ē": "e",
    "Ō": "o",
    "Ṃ": "m",
    "Ḥ": "h",
    "Ṅ": "n",
    "Ñ": "n",
    "Ṭ": "t",
    "Ḍ": "d",
    "Ṇ": "n",
    "Ś": "sh",
    "Ṣ": "sh",
    "Ḻ": "l",
}


def replace_diacritic(char: str) -> str:
    return diacritics.get(char, char)


def simplify_diacritics(text: str) -> str:
    return "".join([replace_diacritic(char) for char in text])

# -*- coding: utf-8 -*-
# Copyright (C) 2016-2023 PyThaiNLP Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import List, Tuple

# defined strings for special characters
CHAR_TO_ESCAPE = {" ": "_"}
ESCAPE_TO_CHAR = dict((v, k) for k, v in CHAR_TO_ESCAPE.items())


# map from Blackboard treebank POS tag to Universal POS tag
# from Wannaphong Phatthiyaphaibun & Korakot Chaovavanich
TO_UD = {
    "": "",
    "AJ": "ADJ",
    "AV": "ADV",
    "AX": "AUX",
    "CC": "CCONJ",
    "CL": "NOUN",
    "FX": "NOUN",
    "IJ": "INTJ",
    "NG": "PART",
    "NN": "NOUN",
    "NU": "NUM",
    "PA": "PART",
    "PR": "PROPN",
    "PS": "ADP",
    "PU": "PUNCT",
    "VV": "VERB",
    "XX": "X",
}


def pre_process(words: List[str]) -> List[str]:
    """
    Convert signs and symbols with their defined strings.
    This function is to be used as a preprocessing step,
    before the actual POS tagging.
    """
    keys = CHAR_TO_ESCAPE.keys()
    words = [CHAR_TO_ESCAPE[word] if word in keys else word for word in words]
    return words


def post_process(
    word_tags: List[Tuple[str, str]], to_ud: bool = False
) -> List[Tuple[str, str]]:
    """
    Convert defined strings back to corresponding signs and symbols.
    This function is to be used as a post-processing step,
    after the POS tagging.
    """
    keys = ESCAPE_TO_CHAR.keys()

    if not to_ud:
        word_tags = [
            (ESCAPE_TO_CHAR[word], tag) if word in keys else (word, tag)
            for word, tag in word_tags
        ]
    else:
        word_tags = [
            (ESCAPE_TO_CHAR[word], TO_UD[tag])
            if word in keys
            else (word, TO_UD[tag])
            for word, tag in word_tags
        ]
    return word_tags

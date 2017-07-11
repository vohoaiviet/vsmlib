"""Tests for vocabulary module."""

import unittest
from vsmlib.vocabulary import create_from_dir

path_text = "./test/data/corpora/small"


class Tests(unittest.TestCase):

    def test_create_from_dir(self):
        vocab = create_from_dir(path_text)
        print("the:", vocab.get_id("the"))
        # vocab.save_to_dir("/tmp/vocab")

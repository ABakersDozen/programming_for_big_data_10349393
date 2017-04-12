# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:16:46 2017

@author: macan
"""

# ************ first iteration *************
#import unittest
#
#from spellcheck import SpellChecker
#
#class TestSpellChecker(unittest.TestCase):
#
#    def setUp(self):
#        self.spellChecker = SpellChecker()
#        self.spellChecker.load_words('spell.words')
#
#    def test_spell_checker(self):
#        self.assertTrue(self.spellChecker.check_word('zygotic'))
#        self.assertFalse(self.spellChecker.check_words('zygotic mistasdas elementary'))
#        self.assertTrue(self.spellChecker.check_words('our first correct sentence'))
#
#if __name__ == '__main__':
#    unittest.main()


# ************ second iteration *************
#import unittest
#from spellcheck import SpellChecker
#class TestSpellChecker(unittest.TestCase):
#    def setUp(self):
#        self.spellChecker = SpellChecker()
#        self.spellChecker.load_words('spell.words')
#
#    def test_spell_checker(self):
#        self.assertTrue(self.spellChecker.check_word('zygotic'))
#        self.assertFalse(self.spellChecker.check_words('zygotic mistasdas elementary'))
#        self.assertTrue(self.spellChecker.check_words('our first correct sentence'))
#        # handle case sensitivity
#        self.assertTrue(self.spellChecker.check_words('Our first correct sentence'))
#        # handle full stop
#        self.assertTrue(self.spellChecker.check_words('Our first correct sentence.'))
#        # we notice that it stops when it finds the first spelling mistake, now we start improving the code. this sentence added first.
#        self.assertFalse(self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary'))
#
#
#if __name__ == '__main__':
#    unittest.main()

## ************ third iteration *************
#import unittest
#from spellcheck import SpellChecker
#class TestSpellChecker(unittest.TestCase):
#    def setUp(self):
#        self.spellChecker = SpellChecker()
#        self.spellChecker.load_words('spell.words')
#
#    def test_spell_checker(self):
#        self.assertTrue(self.spellChecker.check_word('zygotic'))
#        failed_words = self.spellChecker.check_words('zygotic mistasdas elementary',1)
#        self.assertEquals(1, len(failed_words))
#        self.assertEquals('mistasdas', failed_words[0])
#        self.assertEquals(0, len(self.spellChecker.check_words('our first correct sentence',1)))
#        # handle case sensitivity
#        self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence',1)))
#        # handle full stop
#        self.assertEquals(0, len(self.spellChecker.check_words('Our first correct sentence.',1)))
#        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary',1)
#        self.assertEquals(2, len(failed_words))
#        self.assertEquals('mistasdas', failed_words[0])
#        self.assertEquals('spelllleeeing', failed_words[1])
#        # more bugs because the spell checker doesn’t spell check itself correctly – 21 entries not correct – dictionary words need to be lower
#        self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))
#
#
#if __name__ == '__main__':
#    unittest.main()

# ************ fourth iteration *************
import unittest
from spellcheck import SpellChecker
class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        failed_words = self.spellChecker.check_words('zygotic mistasdas elementary')
        self.assertEquals(1, len(failed_words))
        self.assertEquals('mistasdas', failed_words[0]['word'])
        self.assertEquals(1, failed_words[0]['line'])
        self.assertEquals(9, failed_words[0]['pos'])
        self.assertEquals(0, len(self.spellChecker.check_words('our first correct sentence')))
        # handle case sensitivity
        self.assertEquals(0, len(self.spellChecker.check_words('Our capital sentence')))
        # handle full stop
        self.assertEquals(0, len(self.spellChecker.check_words('Our full stop sentence.')))
        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        self.assertEquals(2, len(failed_words))
        self.assertEquals('mistasdas', failed_words[0]['word'])
        self.assertEquals(1, failed_words[0]['line'])
        self.assertEquals(9, failed_words[0]['pos'])
        self.assertEquals('spelllleeeing', failed_words[1]['word'])
        self.assertEquals(1, failed_words[1]['line'])
        self.assertEquals(19, failed_words[1]['pos'])
        self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))


if __name__ == '__main__':
    unittest.main()
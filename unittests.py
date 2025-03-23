import unittest
import filter.ask_yell_sentence
import filter.contains_words
import filter.first_20_sentences
import filter.kwartyl
import search.longest_sentence
import search.longest_non_same
import reduce.count_own_name
import reduce.count_white_char
import reduce.count_paragr
import filter.sentence_with_words_count
import filter.lexical_order
import search.podrzedne_zdania


class TestFilterFunctions(unittest.TestCase):

    def test_ask_yell_sentence(self):
        sentences = 'sadadad asd das! adasdasdsaasdass\n\n asdadadsda?'
        result = filter.ask_yell_sentence.getAskYellSentence(sentences)
        self.assertEqual(result, 'sadadad asd das! asdadadsda?')

    def test_FirstSentence(self):
        sentences = 'sentence1.sentence2!sentence3?sentence4\n\nsentence5.invalid.invalid'
        result = filter.first_20_sentences.getFirstSentences(sentences, 5)
        self.assertEqual(result, 'sentence1.sentence2!sentence3?sentence4\n\nsentence5.')

    def test_ContainsWords(self):
        sentences = "To jest zdanie i oraz ale. To jest zdanie. To jest zdanie lub że."
        result = filter.contains_words.getContainsWords(sentences, 2)
        self.assertEqual(result, 'To jest zdanie i oraz ale. To jest zdanie lub że.')

    def test_Kwartyl(self):
        sentences = '123456789112.123\n\n12345!1.'
        result = filter.kwartyl.getKwartyl(sentences)
        self.assertEqual(result, '123\n\n1.')

    def test_Sorted(self):
        sentences = 'a b c 12. aa ab ac. b a c! ab a.'
        result = filter.lexical_order.getIfSorted(sentences)
        self.assertEqual(result, 'a b c 12. aa ab ac.')

    def test_SentenceWithWordsCount(self):
        sentences = 'a b c d e? abd bcd ccd gd. a.a b c d e asdsadasd asdsa.'
        result = filter.sentence_with_words_count.getSentenceWithWordsCount(sentences, 4)
        self.assertEqual(result, ' abd bcd ccd gd. a.')


class TestReduceFunctions(unittest.TestCase):

    def test_PragraphCounter(self):
        sentences = '1\n\n2.asdadasd.asdada\n\n3\n\n4\n\n'
        result = reduce.count_paragr.paragraphCounter(sentences)
        self.assertEqual(result, 3)

    def test_NonWhiteCharCounter(self):
        sentences = 'abc de. ,,,,,][];fg h.'
        result = reduce.count_white_char.whiteCharCounter(sentences)
        self.assertEqual(int(result), 19)

    def test_NazwaWlasna(self):
        sentences = 'Jest Nazwa wlasna! Nie ma nazwy wlasnej? Tu tez nie. Tu Tak!'
        result = reduce.count_own_name.countOwnNamePercent(sentences)
        self.assertEqual(result, 50.0)


class TestSearchFunctions(unittest.TestCase):

    def test_LongestSentence(self):
        sentences = "123\n\n12345?2.asdv."
        result = search.longest_sentence.longestSentence(sentences)
        self.assertEqual(result, '12345?')

    def test_LongestSentenceNonSameChar(self):
        sentences = "To jest test. To jest test test. To jest test bez powtórzeń.abba a asbduisadabddasbadbasbduydbaybsudbasdbsadbaysudasdyasbdyasbdyasbd."
        result = search.longest_non_same.longestSentence_non_sam_char(sentences)
        self.assertEqual(result, " To jest test bez powtórzeń.")

    def test_ZdaniaPodrzedne(self):
        sentences = "To jest zdanie. To jest zdanie, które ma przecinek. Kolejne zdanie, zdanie, które, ma 3, przecinki.  Kolejne zdanie, zdanie, które, ma 3, przecinki dwa."
        result = search.podrzedne_zdania.getZdaniaPodrzedne(sentences, 3)
        self.assertEqual(result, ' Kolejne zdanie, zdanie, które, ma 3, przecinki.')
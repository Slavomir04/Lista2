import unittest
from Filter import getAskYellSentence, getContainsWords, getKwartyl, getIfSorted,getSentenceWithWordsCount,getFirstSentences
from Reduce import paragraphCounter, whiteCharCounter, oneNameCounterInLine, procentNazwaWlasnych
from Search import getZdaniaPodrzedne,longestSentence, longestSentence_non_same_char

class TestFilterFunctions(unittest.TestCase):

    def test_getSentenceWithWordsCount(self):
        sentences = ['1 2 3 4','asdadasd asdadasd,. asdad','asdada,  ']
        result = getSentenceWithWordsCount(sentences,2)
        self.assertEqual(result,['1 2 3 4','asdadasd asdadasd,. asdad'])
    def test_getFirstSentences(self):
        sentences = ['1','2','3','4']
        result = getFirstSentences(sentences,3)
        self.assertEqual(result,['1','2','3'])
    def test_getAskYellSentence(self):
        sentences = ["Czy to jest pytanie?", "To jest zdanie!", "Kolejne zdanie."]
        result = getAskYellSentence(sentences)
        self.assertEqual(result, ["Czy to jest pytanie?", "To jest zdanie!"])

    def test_getContainsWords(self):
        sentences = ["To jest zdanie i oraz ale.", "To jest zdanie.", "To jest zdanie lub że."]
        result = getContainsWords(sentences, words=['i', 'oraz', 'ale', 'że', 'lub'], mincontains=2)
        self.assertEqual(result, ["To jest zdanie i oraz ale.", "To jest zdanie lub że."])

    def test_getKwartyl(self):
        sentences = ['zdanie ma 12',"123", "12"]
        result = getKwartyl(sentences)
        self.assertEqual(result, ['123','12'])

    def test_getIfSorted(self):
        sentences = ["a b c", "c b a", "a a a"]
        result = getIfSorted(sentences)
        self.assertEqual(result, ["a b c", "a a a"])




class TestReduceFunctions(unittest.TestCase):

    def test_paragraphCounter(self):
        paragraphs = ["Cos1", "Cos2", "Cos3"]
        result = paragraphCounter(paragraphs)
        self.assertEqual(result, 3)

    def test_whiteCharCunter(self):
        text = ['123,456    78-9']
        result = whiteCharCounter(text)
        self.assertEqual(int(result), 9)

    def test_oneNameCounterInLine(self):
        line = "adasdasd Test asDadsaTsadas Itasd"
        result = oneNameCounterInLine(line)
        self.assertEqual(result, 2)

    def test_procentNazwaWlasnych(self):
        sentences = ["asdasda asdsadsa", "asdaasd Aasdasd asdAdsa"]
        result = procentNazwaWlasnych(sentences)
        self.assertEqual(result, 50.0)



class TestSearchFunctions(unittest.TestCase):

    def test_longestSentence(self):
        sentences = ["Krótkie zdanie.", "To jest dłuższe zdanie.", "To jest najdłuższe zdanie."]
        result = longestSentence(sentences)
        self.assertEqual(result, "To jest najdłuższe zdanie.")

    def longestSentence_non_same_char(self):
        sentences = ["To jest test.", "To jest test test.", "To jest test bez powtórzeń."]
        result = longestSentence_non_same_char(sentences)
        self.assertEqual(result, "To jest test bez powtórzeń.")


    def test_getZdaniaPodrzedne(self):
        sentences = ["To jest zdanie.", "To jest zdanie, które ma przecinek.", "Kolejne zdanie.","zdanie, które, ma 3, przecinki"]
        result = getZdaniaPodrzedne(sentences, mincount=1)
        self.assertEqual(result, ["To jest zdanie, które ma przecinek.","zdanie, które, ma 3, przecinki"])




import unittest
import sys
from contextlib import contextmanager
from io import StringIO

from ExternalMethods import *
from CircularPositionalList import CircularPositionalList
from ScoreBoard import ScoreBoard


class ScoreBoardTest(unittest.TestCase):
    _maxDimension = 10

    _scoreArrayA = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]

    _scoreArrayB = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250]

    _nameArray = ["Topolino", "Paperino", "Minnie", "Pluto", "Gambadilegno", "Clarabella", "Bassotti",
                  "Archimede", "Orazio", "Macchia nera", "Ciccio", "Basettoni"]

    _arrayDate = ["21 Gennaio 2018", "22 Gennaio 2018", "23 Gennaio 2018",
                  "24 Gennaio 2018", "25 Gennaio 2018", "26 Gennaio 2018", "27 Gennaio 2018", "28 Gennaio 2018",
                  "29 Gennaio 2018", "30 Gennaio 2018", "31 Gennaio 2018", "20 Gennaio 2018", "19 Gennaio 2018"]

    def setUp(self):
        """Call before every test case."""
        self.Scoreboard = ScoreBoard(self._maxDimension)

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def test_ScoreboardHaveCorrectMaxDimension(self):
        self.assertEqual(self._maxDimension, len(self.Scoreboard))

    def test_ScoreboardHaveAlwaysCorrectDimension(self):
        for i in range(0, self._maxDimension):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
            self.assertEqual(i + 1, self.Scoreboard.size())
        self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[11], self._scoreArrayA[11], self._arrayDate[11]))
        self.assertEqual(self._maxDimension, self.Scoreboard.size())

    def test_isEmpty_worksAsExpected(self):
        # initially empty
        self.assertTrue(self.Scoreboard.is_empty())
        # Adding some score
        self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[0], self._scoreArrayA[0], self._arrayDate[0]))
        self.assertFalse(self.Scoreboard.is_empty())

    def test_insert_worksAsExpected(self):
        # filling an empty scoreboard add always elements
        for i in range(0, self._maxDimension):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
            self.assertEqual(i + 1, self.Scoreboard.size())

        # new record has to be inserted in the Scoreboard
        top_score = ScoreBoard.Score(self._nameArray[11], self._scoreArrayA[11], self._arrayDate[11])
        self.Scoreboard.insert(top_score)
        assert self.Scoreboard._sb.find(top_score) is not None
        self.assertEqual(self._maxDimension, self.Scoreboard.size())

        # score lower must not be added in a full Scoreboard
        low_score = ScoreBoard.Score(self._nameArray[0], self._scoreArrayA[0], self._arrayDate[0])
        self.Scoreboard.insert(low_score)
        assert self.Scoreboard._sb.find(low_score) is None
        self.assertEqual(self._maxDimension, self.Scoreboard.size())

    def test_top_worksAsExpectedNotConsideringException(self):
        # filling an empty scoreboard
        for i in range(0, self._maxDimension):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
        first = ScoreBoard.Score(self._nameArray[9], self._scoreArrayA[9], self._arrayDate[9])
        second = ScoreBoard.Score(self._nameArray[8], self._scoreArrayA[8], self._arrayDate[8])
        third = ScoreBoard.Score(self._nameArray[7], self._scoreArrayA[7], self._arrayDate[7])

        # top without parameter print the best score
        with self.captured_output() as (out, err):
            self.Scoreboard.top()
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        self.assertEqual(first.__str__().strip(), output)

        # top with 3 parameter print 3 best scores
        with self.captured_output() as (out, err):
            self.Scoreboard.top(3)
        output = out.getvalue().strip()
        self.assertEqual((first.__str__() + "\n" + second.__str__() + "\n" + third.__str__()).strip(), output)

    def test_top_worksConsideringException(self):
        for i in range(0, 3):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
        self.assertRaises(IndexError, self.Scoreboard.top, 5)

    def test_last_worksAsExpectedNotConsideringException(self):
        # filling an empty scoreboard
        for i in range(0, self._maxDimension):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
        last = ScoreBoard.Score(self._nameArray[0], self._scoreArrayA[0], self._arrayDate[0])
        second_last = ScoreBoard.Score(self._nameArray[1], self._scoreArrayA[1], self._arrayDate[1])
        third_last = ScoreBoard.Score(self._nameArray[2], self._scoreArrayA[2], self._arrayDate[2])

        # top without parameter print the best score
        with self.captured_output() as (out, err):
            self.Scoreboard.last()
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        self.assertEqual(last.__str__().strip(), output)

        # top with 3 parameter print 3 best scores
        with self.captured_output() as (out, err):
            self.Scoreboard.last(3)
        output = out.getvalue().strip()
        self.assertEqual((last.__str__() + "\n" + second_last.__str__() + "\n" + third_last.__str__()).strip(), output)

    def test_last_worksConsideringException(self):
        for i in range(0, 3):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
        self.assertRaises(IndexError, self.Scoreboard.last, 5)

    def test_merge(self):
        # fill Scoreboard under test
        for i in range(0, self._maxDimension):
            self.Scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayA[i], self._arrayDate[i]))
        # fill second Scoreboard
        second_scoreboard = ScoreBoard()
        for i in range(0, self._maxDimension):
            second_scoreboard.insert(ScoreBoard.Score(self._nameArray[i], self._scoreArrayB[i], self._arrayDate[i]))

        # merging the score board
        self.Scoreboard.merge(second_scoreboard)

        # validating merge conditions

        # size is still max size
        self.assertEqual(self._maxDimension, self.Scoreboard.size())
        # array merged is ordered
        self.assertTrue(self.Scoreboard._sb.is_sorted())
        # merging does not add duplicate
        for elem in self.Scoreboard._sb:
            self.assertEqual(1, self.Scoreboard._sb.count(elem))
        # given we know the value validate that the merge array is correct
        expected_correct_merge = ScoreBoard(self._maxDimension)
        for i in range(0, 5):
            score = ScoreBoard.Score(self._nameArray[9 - i], self._scoreArrayB[9 - i], self._arrayDate[9 - i])
            score2 = ScoreBoard.Score(self._nameArray[9 - i], self._scoreArrayA[9 - i], self._arrayDate[9 - i])
            expected_correct_merge.insert(score)
            expected_correct_merge.insert(score2)
        for expectedElem in expected_correct_merge._sb:
            assert self.Scoreboard._sb.find(expectedElem) is not None



class CircularPositionalListTest(unittest.TestCase):

    def setUp(self):
        """Tale metodo verrÃ  eseguito prima di ogni test"""
        self._circularList = CircularPositionalList()

    def test_first(self):
        self.assertIsNone(self._circularList.first())
        p = self._circularList.add_last(3)
        self.assertEqual(self._circularList.first(), p)
        p1 = self._circularList.add_last(4)
        self.assertEqual(self._circularList.first(), p)

    def test_last(self):
        self.assertIsNone(self._circularList.first())
        p = self._circularList.add_last(3)
        self.assertEqual(self._circularList.last(), p)
        p1 = self._circularList.add_last(4)
        self.assertEqual(self._circularList.last(), p1)

    def test_add_first(self):
        self.assertEqual(self._circularList.add_first(4), self._circularList.first())

    def test_add_last(self):
        self.assertEqual(self._circularList.add_last(4), self._circularList.last())

    def test_is_empty(self):
        self.assertTrue(self._circularList.is_empty())
        self._circularList.add_last(3)
        self.assertFalse(self._circularList.is_empty())

    def test_add_before(self):
        p = self._circularList.add_last(3)
        p = self._circularList.add_before(p, 2)
        self.assertEqual(p.element(), 2)

    def test_add_after(self):
        p = self._circularList.add_last(3)
        p = self._circularList.add_after(p, 2)
        self.assertEqual(p.element(), 2)

    def test_replace(self):
        p = self._circularList.add_last(3)
        p1 = self._circularList.add_last(4)
        self._circularList.replace(p, 5)
        self.assertEqual(p.element(), 5)

    def test_before(self):
        # Primo inserimento p1
        p1 = self._circularList.add_last(3)
        self.assertIsNone(self._circularList.before(p1))

        # Secondo inserimento con due elementi uguali p1 <=> p2
        p2 = self._circularList.add_last(3)
        self.assertEqual(self._circularList.before(p2), p1.element())

        # Terzo Inseimento  p3 <=> p1 <=> p2
        p3 = self._circularList.add_first(2)
        self.assertEqual(self._circularList.before(p3), p2.element())

        # p3 <=> p1 <=> p2

        self.assertEqual(self._circularList.before(p1), p3.element())

    def test_after(self):
        # Primo inserimento p1
        p1 = self._circularList.add_last(3)
        self.assertIsNone(self._circularList.after(p1))

        # Secondo inserimento con due elementi uguali p1 <=> p2
        p2 = self._circularList.add_last(3)
        self.assertEqual(self._circularList.after(p1), p2.element())

        # Terzo Inseimento  p3 <=> p1 <=> p2
        p3 = self._circularList.add_first(2)
        self.assertEqual(self._circularList.after(p2), p3.element())

        # p3 <=> p1 <=> p2

        self.assertEqual(self._circularList.after(p1), p2.element())

    def test_find(self):
        for i in range(10):
            p = self._circularList.add_last(i)

        self.assertEqual(self._circularList.find(9), p)
        self.assertIsNone(self._circularList.find(10))

        # Deve trovare la prima occorrenza
        p1 = self._circularList.add_last(9)
        self.assertNotEqual(self._circularList.find(9), p1)

    def test_is_sorted(self):
        for i in range(10):
            self._circularList.add_last(i)

        self.assertTrue(self._circularList.is_sorted())
        self._circularList.add_last(0)
        self.assertFalse(self._circularList.is_sorted())

    def test_clear(self):
        self._circularList.add_last(1)
        self._circularList.clear()
        self.assertTrue(self._circularList.is_empty(), True)
        for i in range(10):
            self._circularList.add_last(i)

        self._circularList.clear()
        self.assertTrue(self._circularList.is_empty(), True)

    def test_count(self):
        for i in range(10):
            self._circularList.add_last(i)

        self.assertEqual(self._circularList.count(1), 1)
        self._circularList.add_last(1)
        self.assertEqual(self._circularList.count(1), 2)
        self.assertEqual(self._circularList.count(10), 0)

    def test_reverse(self):

        for i in range(10):
            self._circularList.add_last(i)

        self._circularList.reverse()
        i = 9

        while i >= 0:
            self.assertEqual(self._circularList.delete(self._circularList.first()), i)

            i -= 1

    def test_copy(self):

        for i in range(10):
            self._circularList.add_last(i)

        circular_test = self._circularList.copy()

        p1 = []

        for p in circular_test:
            p1.append(p)

        # Testo se tutti gli elementi sono uguali
        i = 0
        for p in self._circularList:
            self.assertEqual(p, p1[i])
            i += 1

        # Testo se eliminando il primo elemento l'elemento first Ã¨ uguale per tutte e due le liste
        self._circularList.delete(self._circularList.first())
        circular_test.delete(circular_test.first())
        self.assertEqual(self._circularList.first().element(), circular_test.first().element())

        # Testo se eliminando l'ultimo elemento l'elemento last Ã¨ uguale per tutte e due le liste
        self._circularList.delete(self._circularList.last())
        circular_test.delete(circular_test.last())
        self.assertEqual(self._circularList.last().element(), circular_test.last().element())

        # Testo se aggiungendo un elemento in coda l'elemento last Ã¨ uguale per tutte e due le liste
        self._circularList.add_last(100)
        circular_test.add_last(100)
        self.assertEqual(self._circularList.last().element(), circular_test.last().element())

        # Testo se aggiungendo un elemento in coda l'elemento first Ã¨ uguale per tutte e due le liste
        self._circularList.add_first(100)
        circular_test.add_first(100)
        self.assertEqual(self._circularList.first().element(), circular_test.first().element())

        # Testo se facendo il reverse le due liste hanno ancora gli elementi uguali
        self._circularList.reverse()
        circular_test.reverse()

        p1 = []

        for p in circular_test:
            p1.append(p)

        i = 0
        for p in self._circularList:
            self.assertEqual(p, p1[i])
            i += 1

        self._circularList.clear()
        circular_test.clear()

        p1 = []

        for p in circular_test:
            p1.append(p)

        i = 0
        for p in self._circularList:
            self.assertEqual(p, p1[i])
            i += 1

    def test_contains(self):
        p = self._circularList.add_last(2)
        self.assertTrue(p in self._circularList)
        p = self._circularList.add_last(2)
        self._circularList.delete(self._circularList.last())
        self.assertFalse(p in self._circularList)

    def test_len(self):
        self.assertTrue(len(self._circularList) == 0)
        self._circularList.add_last(2)
        self.assertTrue(len(self._circularList) == 1)

    def test_get(self):
        p = self._circularList.add_last(2)
        self.assertEqual(self._circularList[p], p.element())

    def test_set(self):
        p = self._circularList.add_last(2)
        self._circularList[p] = 3
        self.assertNotEqual(self._circularList[p], 2)

    def test_delete(self):
        p = self._circularList.add_last(2)
        del self._circularList[p]
        self.assertFalse(p in self._circularList)


class ExternalMethodTest(unittest.TestCase):

    def setUp(self):
        """Tale metodo verrÃ  eseguito prima di ogni test"""
        self._circularList1 = CircularPositionalList()
        self._circularList2 = CircularPositionalList()

    def test_bubblesorted(self):
        for i in range(-10, 0):
            self._circularList1.add_last(-i)
        j = 1
        for elem in bubblesorted(self._circularList1):
            self.assertEqual(elem, j)
            j += 1
        # Verifichiamo che il generatore non ha modificato gli elementi della lista
        self.assertEqual(self._circularList1.first().element(), 10)

    def test_merge(self):
        for i in range(10):
            self._circularList1.add_last(i)
            self._circularList2.add_last(i + 10)

        l = merge(self._circularList1, self._circularList2)

        for i in range(20):
            self.assertEqual(l.delete(l.first()), i)


if __name__ == '__main__':
    unittest.main(verbosity=True, buffer=True)

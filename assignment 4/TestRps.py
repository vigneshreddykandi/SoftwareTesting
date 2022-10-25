#vignesh reddy kandi
import unittest
import rps

class test_rps(unittest.TestCase):
    def test_Defeat1(self):
        You = "Rock"
        Com = "Rock"
        receive=rps.Defeat1(You,Com)
        self.assertEqual("Better luck next time :3",receive)

    def test_Defeat2(self):
        You = "Rock"
        Com = "Rock"
        receive=rps.Defeat2(You,Com)
        self.assertEqual("Better luck next time :3",receive)

    def test_Defeat3(self):
        You = "Rock"
        Com = "Rock"
        receive=rps.Defeat3(You,Com)
        self.assertEqual("Better luck next time :3",receive)


    def test_Victory1(self):
        You = "Scissors"
        Com = "Paper"
        receive=rps.Victory1(You,Com)
        self.assertEqual("Will get you next time",receive)

    def test_Victory2(self):
        
        You = "Paper"
        Com = "Rock"
        receive=rps.Victory2(You,Com)
        self.assertEqual("Will get you next time",receive)

    def test_Victory3(self):
        You = "Rock"
        Com = "Scissors"
        receive=rps.Victory3(You,Com)
        self.assertEqual("Will get you next time",receive)

    def test_Tie1(self):
        
        You = "Paper"
        Com = "Paper"
        receive=rps.Tie(You,Com)
        self.assertEqual("Try again",receive)

    def test_Tie2(self):
        You = "Rock"
        Com = "Rock"
        receive=rps.Tie(You,Com)
        self.assertEqual("Try again",receive)

    def test_Tie3(self):
        You = "Scissors"
        Com = "Scissors"
        receive=rps.Tie(You,Com)
        self.assertEqual("Try again",receive)


    def test_false(self):
        You= 8
        Com = "Scissors"
        receive=rps.false(You,Com)
        self.assertEqual(False,receive)
      

if __name__ == "__main__":
    unittest.main()
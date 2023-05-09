import unittest

import HtmlTestRunner

from Cursul9 import Test
from Teme.Tema10 import Login

class TestSuite(unittest.TestCase):
    #aici implementam o suita de teste
    def test_suite(self): #cuvant cheie
        smoketest = unittest.TestSuite()
        #aici adugam testele noastre in suita
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)
        ])


        #aici implemetam raportul HTML
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = "Primul meu raport",
            report_name = "Acesta este un raport de testare automata"
        )

        runner.run(smoketest)
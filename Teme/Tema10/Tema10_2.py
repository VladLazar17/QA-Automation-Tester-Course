'''
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
'''

import unittest
import HtmlTestRunner

from Teme.Tema9 import Login
from Tema10_1 import WebForm

class TestSuite(unittest.TestCase):
    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(WebForm)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Raport de teste',
            report_name='Raport de testare automata'
        )

        runner.run(smoketest)
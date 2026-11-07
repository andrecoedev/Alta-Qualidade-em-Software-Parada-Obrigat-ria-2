from pathlib import Path
import subprocess
import sys
import unittest


CALCULADORA = Path(__file__).with_name("Calculadora.py")


class TestCalculadora(unittest.TestCase):
    def executar(self, *entradas):
        processo = subprocess.run(
            [sys.executable, "-X", "utf8", str(CALCULADORA)],
            input="\n".join(entradas) + "\n",
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
        )
        self.assertEqual(processo.returncode, 0, processo.stderr)
        return processo.stdout

    def test_adicao_de_dois_positivos(self):
        saida = self.executar("1", "2", "3", "n")
        self.assertIn("Resultado: 5.0\n", saida)


if __name__ == "__main__":
    unittest.main()

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

    def test_adicao_de_negativos(self):
        self.assertIn("Resultado: -5.0\n", self.executar("1", "-2", "-3", "n"))

    def test_adicao_com_zero(self):
        for x, y in [("0", "3"), ("3", "0")]:
            with self.subTest(x=x, y=y):
                self.assertIn("Resultado: 3.0\n", self.executar("1", x, y, "n"))

    def test_adicao_com_decimais(self):
        self.assertIn("Resultado: 0.75\n", self.executar("1", "0.5", "0.25", "n"))

    def test_subtracao(self):
        self.assertIn("Resultado: 5.0\n", self.executar("2", "8", "3", "n"))

    def test_multiplicacao(self):
        self.assertIn("Resultado: 42.0\n", self.executar("3", "6", "7", "n"))

    def test_divisao(self):
        self.assertIn("Resultado: 4.0\n", self.executar("4", "8", "2", "n"))

    def test_potencia(self):
        self.assertIn("Resultado: 8.0\n", self.executar("5", "2", "3", "n"))

    def test_raiz_quadrada(self):
        self.assertIn("Resultado: 3.0\n", self.executar("6", "9", "n"))

    def test_raiz_negativa(self):
        self.assertIn("Erro: Raiz quadrada de número negativo", self.executar("6", "-9", "n"))

    def test_logaritmos_negativos(self):
        for operacao in ["8", "9"]:
            with self.subTest(operacao=operacao):
                self.assertIn("Erro: Logaritmo de número não positivo", self.executar(operacao, "-1", "n"))

    def test_sair(self):
        self.assertIn("Calculadora encerrada.", self.executar("0"))

    def test_opcao_invalida(self):
        self.assertIn("Operação inválida.", self.executar("99", "n"))

    def test_realizar_outra_operacao(self):
        saida = self.executar("1", "2", "3", "s", "3", "2", "3", "n")
        self.assertIn("Resultado: 5.0\n", saida)
        self.assertIn("Resultado: 6.0\n", saida)


if __name__ == "__main__":
    unittest.main()

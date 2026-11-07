# Bug Hunter & TDD Calculator

André Lucas Coelho de Jesus — Alta Qualidade em Software — Parada Obrigatória 2.

Analisei a calculadora fornecida, registrei 11 bugs no arquivo [Bugs.md](Bugs.md) e corrigi o erro da adição usando TDD.

## Executar

No terminal, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe Calculadora.py
```

Ambiente usado: Windows, Python 3.14.3, NumPy 2.5.4 e pytest 9.2.0.

## Testar

```powershell
.\.venv\Scripts\python.exe -m unittest -v test_calculadora
.\.venv\Scripts\python.exe -m pytest -q
```

O enunciado cita unittest e pytest. Escrevi os testes com unittest e executei a mesma suíte pelos dois frameworks. Os testes usam o menu real da calculadora, enviando entradas pelo terminal e conferindo a saída.

Resultado final: **14 testes passando** nos dois frameworks. No pytest, também passaram os 4 subtestes dos casos com zero e logaritmos negativos.

## Correção com TDD

Escolhi a soma porque era um erro em uma operação básica. Para `2 + 3`, o código original retornava `7`.

1. **Red:** escrevi um teste esperando `5.0`. Executei antes de alterar o código e ele falhou. [Log](evidencias/01-red.txt).
2. **Green:** removi o `x +` que somava o primeiro número novamente. O teste passou. [Log](evidencias/02-green.txt).
3. **Refactor:** simplifiquei a função para `return x + y`. Rodei os testes de regressão e todos passaram. [unittest](evidencias/03-refactor-unittest.txt) e [pytest](evidencias/04-pytest.txt).

Também testei negativos, decimais, zero, outras operações básicas, mensagens de erro já existentes, saída e repetição do menu. A correção ficou restrita à adição. Os outros 10 bugs continuam pendentes no relatório.

## Git e GitHub

Usei o Git para guardar as etapas em commits separados. O GitHub hospeda o repositório e permite consultar os arquivos e o histórico pela internet.

| Commit | Etapa |
| --- | --- |
| `bd56b93` | Código original e ambiente |
| `1a9524b` | Teste falhando e evidências dos bugs |
| `52c5621` | Correção mínima da soma |
| `c8ca58a` | Refatoração e testes de regressão |

Os arquivos da entrega estão na branch `trabalho-faculdade`. [Abrir a entrega](https://github.com/andrecoedev/Alta-Qualidade-em-Software-Parada-Obrigat-ria-2/tree/trabalho-faculdade).

## Reflexão sobre Scrum

Os bugs encontrados podem formar um backlog. Numa sprint, eu priorizaria os erros que encerram o programa e os cálculos que retornam valores errados. A meta desta atividade foi corrigir a soma com teste e deixar as outras pendências registradas.

Como o trabalho foi individual, adaptei a organização para uma lista de problemas e uma entrega pequena. O critério de conclusão da correção foi o teste passar e os fluxos de regressão continuarem funcionando. Na retrospectiva, o principal aprendizado foi que o teste precisa falhar antes da correção: assim dá pra confirmar que ele realmente identifica o defeito.

## Referências consultadas

- [GitHub: sobre o Git](https://docs.github.com/pt/get-started/using-git/about-git).
- [Python: unittest](https://docs.python.org/3/library/unittest.html).
- [pytest: documentação indicada no enunciado](https://docs.pytest.org/en/7.1.x/contents.html).
- [pytest: execução de testes unittest](https://docs.pytest.org/en/stable/how-to/unittest.html).
- [Martin Fowler: Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html).

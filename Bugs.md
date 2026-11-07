# Relatório de bugs

**Aluno:** André Lucas Coelho de Jesus

**Disciplina:** Alta Qualidade em Software

**Data da identificação:** 07/11/2026

Testei no Windows, com Python 3.14.3 e NumPy 2.5.4. Todos os bugs abaixo aconteceram de forma consistente. As evidências foram coletadas no código original, antes da correção.

Para reproduzir cada caso, executar `python Calculadora.py` e digitar as entradas na ordem indicada, pressionando Enter depois de cada uma. Quando a operação terminar normalmente, responder `n` para sair.

Os logs estão em [evidencias/00-bugs-original.txt](evidencias/00-bugs-original.txt). Os códigos BUG-01 a BUG-11 identificam cada caso no arquivo. As capturas estão em [evidencias/bugs.png](evidencias/bugs.png) e [evidencias/tdd.png](evidencias/tdd.png).

## BUG-01 — Adição soma o primeiro número duas vezes

- **Local:** `Calculadora.py`, função `adicao`.
- **Descrição:** a expressão `x + np.add(x, y)` calcula `2x + y`.
- **Passos:** escolher `1`, digitar `2` e `3`.
- **Esperado:** `5.0`.
- **Obtido:** `7.0`, registrado no log BUG-01.
- **Severidade:** alta. A operação básica de soma entrega um valor errado.
- **Correção:** remover a soma duplicada. Depois, simplificar para `return x + y`.
- **Status:** resolvido com TDD. Evidências: `01-red.txt`, `02-green.txt` e `03-refactor-unittest.txt`.

## BUG-02 — Divisão por zero encerra a calculadora

- **Local:** `Calculadora.py`, função `divisao`.
- **Descrição:** o divisor não é validado antes de calcular.
- **Passos:** escolher `4`, digitar `8` e `0`.
- **Esperado:** informar que não é possível dividir por zero e manter o programa funcionando.
- **Obtido:** `ZeroDivisionError: division by zero`, registrado no log BUG-02.
- **Severidade:** alta. A entrada encerra o programa com exceção.
- **Sugestão:** validar se o divisor é zero e mostrar uma mensagem.
- **Status:** não resolvido.

## BUG-03 — Fatorial retorna zero para inteiros não negativos

- **Local:** `Calculadora.py`, função `fatorial`, laço `for`.
- **Descrição:** o laço começa em zero. A primeira multiplicação zera o acumulador.
- **Passos:** escolher `7` e digitar `5`. Repetir com `0`.
- **Esperado:** `120` para `5!` e `1` para `0!`.
- **Obtido:** `0` nos dois casos, registrado nos logs BUG-03a e BUG-03b.
- **Severidade:** alta. O cálculo de fatorial fica incorreto para todo inteiro não negativo.
- **Sugestão:** começar o laço em `1`, mantendo o acumulador inicial em `1`.
- **Status:** não resolvido.

## BUG-04 — Fatorial aceita número negativo

- **Local:** `Calculadora.py`, função `fatorial`.
- **Descrição:** falta validar o domínio da operação. Com entrada negativa, o laço não executa e a função retorna `1`.
- **Passos:** escolher `7` e digitar `-3`.
- **Esperado:** informar que o fatorial precisa de um inteiro não negativo.
- **Obtido:** `1`, registrado no log BUG-04.
- **Severidade:** média. O programa apresenta um resultado para uma entrada inválida.
- **Sugestão:** rejeitar valores menores que zero antes do laço.
- **Status:** não resolvido.

## BUG-05 — Logaritmo natural chama uma função inexistente

- **Local:** `Calculadora.py`, função `logaritmo_natural`.
- **Descrição:** a função usa `np.ln`, que não existe no NumPy.
- **Passos:** escolher `8` e digitar `1`.
- **Esperado:** `0.0`, pois `ln(1) = 0`.
- **Obtido:** `AttributeError: module 'numpy' has no attribute 'ln'`, registrado no log BUG-05.
- **Severidade:** alta. Entradas positivas encerram o programa nessa operação.
- **Sugestão:** usar `np.log(x)`.
- **Status:** não resolvido.

## BUG-06 — Logaritmo de base 10 usa a base errada

- **Local:** `Calculadora.py`, função `logaritmo_base10`.
- **Descrição:** `np.log` calcula o logaritmo natural, apesar do nome da função e da opção do menu.
- **Passos:** escolher `9` e digitar `100`.
- **Esperado:** `2.0`.
- **Obtido:** `4.605170185988092`, registrado no log BUG-06.
- **Severidade:** alta. O resultado numérico não corresponde à operação escolhida.
- **Sugestão:** usar `np.log10(x)`.
- **Status:** não resolvido.

## BUG-07 — Logaritmo de base 10 não rejeita zero

- **Local:** `Calculadora.py`, função `logaritmo_base10`, condição `x < 0`.
- **Descrição:** a validação deixa o zero passar, mesmo sendo uma entrada fora do domínio real do logaritmo.
- **Passos:** escolher `9` e digitar `0`.
- **Esperado:** `Erro: Logaritmo de número não positivo`.
- **Obtido:** `-inf` e `RuntimeWarning: divide by zero encountered in log`, registrados no log BUG-07.
- **Severidade:** média. A calculadora apresenta infinito no lugar de explicar a entrada inválida.
- **Sugestão:** trocar a validação para `x <= 0`.
- **Status:** não resolvido.

## BUG-08 — Opção de seno não foi implementada

- **Local:** `Calculadora.py`, função `calculadora_cientifica`, seleção das operações.
- **Descrição:** o menu mostra a opção `10`, mas não existe um ramo para tratar essa escolha nem uma função de seno.
- **Passos:** escolher `10`.
- **Esperado:** pedir o ângulo e calcular o seno.
- **Obtido:** `Operação inválida. Tente novamente.`, registrado no log BUG-08.
- **Severidade:** média. Uma operação anunciada no menu fica indisponível.
- **Sugestão:** implementar a operação e definir a unidade do ângulo na entrada.
- **Status:** não resolvido.

## BUG-09 — Cosseno chama uma função não definida

- **Local:** `Calculadora.py`, função `calculadora_cientifica`, opção `11`.
- **Descrição:** o programa chama `cosseno(x)`, mas essa função não foi definida.
- **Passos:** escolher `11` e digitar `60` graus.
- **Esperado:** resultado próximo de `0.5`.
- **Obtido:** `NameError: name 'cosseno' is not defined`, registrado no log BUG-09.
- **Severidade:** alta. A operação encerra o programa.
- **Sugestão:** implementar a função, convertendo graus para radianos antes do cálculo.
- **Status:** não resolvido.

## BUG-10 — Tangente chama uma função não definida

- **Local:** `Calculadora.py`, função `calculadora_cientifica`, opção `12`.
- **Descrição:** o programa chama `tangente(x, radianos=False)`, mas essa função não foi definida.
- **Passos:** escolher `12` e digitar `45` graus.
- **Esperado:** resultado próximo de `1.0`.
- **Obtido:** `NameError: name 'tangente' is not defined`, registrado no log BUG-10.
- **Severidade:** alta. A operação encerra o programa.
- **Sugestão:** implementar a função e tratar ângulos em que a tangente não está definida.
- **Status:** não resolvido.

## BUG-11 — Entrada não numérica encerra o programa

- **Local:** `Calculadora.py`, função `calculadora_cientifica`, conversões com `float` e `int`.
- **Descrição:** as entradas são convertidas sem tratar erro de formato.
- **Passos:** escolher `1` e digitar `abc` como primeiro número.
- **Esperado:** avisar que a entrada é inválida e permitir uma nova tentativa.
- **Obtido:** `ValueError: could not convert string to float: 'abc'`, registrado no log BUG-11.
- **Severidade:** média. Um erro de digitação encerra a calculadora.
- **Sugestão:** tratar `ValueError` nas leituras numéricas.
- **Status:** não resolvido.

## Acompanhamento

Identifiquei 11 bugs e escolhi o BUG-01 para a correção com TDD. Os outros 10 continuam registrados como pendências. Os testes de regressão verificam a soma e alguns fluxos que já funcionavam; eles não significam que toda a calculadora está correta.

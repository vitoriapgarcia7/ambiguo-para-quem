# Dicionário de dados: `respostas_humanas.csv`

Respostas dos revisores humanos ao formulário do estudo, **anonimizadas**. Cada linha é um requisito e cada coluna de revisor traz o veredito dessa pessoa.

## Colunas

| Coluna | Descrição | Valores |
|---|---|---|
| `requisito` | Código do requisito, como na Tabela 1 do artigo | `REQ-01` a `REQ-08` |
| `R1` a `R9` | Veredito de cada revisor para o requisito: ele é ambíguo segundo o critério operacional do estudo? | `Sim` ou `Não` |

## Observações

- **9 revisores** (5 estudantes, 3 integrantes do grupo de autoras e 1 docente de Engenharia de Software) responderam a todos os requisitos. Uma décima resposta, de uma das autoras, foi excluída da análise para preservar a independência da avaliação humana e **não consta** neste arquivo.
- As colunas `R1` a `R9` estão em **ordem embaralhada** e sem identificação. Este arquivo **não contém** e-mails, nomes nem carimbo de data e hora. A única indicação de perfil é a de que `R1`, `R5` e `R8` são os três integrantes do grupo de autoras, informação necessária para reproduzir a análise de sensibilidade da Tabela 6 do artigo (que compara os nove revisores com os seis externos ao grupo).
- **Regra de agregação:** o requisito é considerado ambíguo na condição humana quando **5 ou mais dos 9** revisores responderam `Sim` (sem empate, pois 9 é ímpar). A regra foi definida antes da análise das respostas.
- Este arquivo traz apenas o veredito Sim/Não. O script [`scripts/calcular_concordancia.py`](../scripts/calcular_concordancia.py) recalcula a concordância, o kappa de Fleiss e a análise de sensibilidade a partir dele. A [planilha de análise](../analise/planilha_de_analise.xlsx) calcula o resultado humano, o kappa e a análise por requisito a partir dele.
- Período de coleta: 09/11/2026 a 14/11/2026.

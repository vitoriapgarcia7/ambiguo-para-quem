# Análise

Planilha de análise do estudo e cópias em CSV das suas abas, para ler direto no navegador.

| Arquivo | O que é |
|---|---|
| [planilha_de_analise.xlsx](planilha_de_analise.xlsx) | Planilha completa, com as fórmulas (baixe para abrir no Excel ou no Google Planilhas). O GitHub não mostra arquivos `.xlsx` na tela. |
| [concordancia.csv](concordancia.csv) | Tabela de contagem, concordância observada e esperada, kappa de Cohen |
| [analise_por_requisito.csv](analise_por_requisito.csv) | Trechos e questões de cada condição, correspondência e grupo, por requisito |
| [execucoes_llm.csv](execucoes_llm.csv) | Registro das 3 execuções da LLM, veredito e tipo por requisito, e estabilidade |
| [../respostas_humanas/respostas_humanas.csv](../respostas_humanas/respostas_humanas.csv) | Sim ou Não de cada revisor por requisito |

## Regras

- **Condição humana:** o requisito é ambíguo quando **5 ou mais dos 9** revisores marcaram Sim.
- **Condição LLM:** o requisito é ambíguo quando **2 ou mais das 3** execuções marcaram Sim.
- Não houve gabarito: as duas condições foram tratadas como leituras independentes.

As fórmulas da planilha recalculam a partir das respostas. Os trechos, as questões e a correspondência foram classificados manualmente pelas autoras.

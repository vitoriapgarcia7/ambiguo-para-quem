# Seleção dos requisitos

Como os 8 requisitos analisados foram escolhidos do corpus **PURE** ([Ferrari et al., 2017](https://doi.org/10.1109/RE.2017.29)), composto por 79 documentos de requisitos em linguagem natural, públicos e reunidos para pesquisa em Engenharia de Requisitos e Processamento de Linguagem Natural.

> [!IMPORTANT]
> Os documentos originais do PURE **não são redistribuídos aqui**. Os 8 requisitos usados aparecem no [prompt](../prompt/prompt_llm.txt), porque fazem parte do material enviado à LLM.

## Critérios

1. **Dois documentos**, escolhidos por uma das autoras por apresentarem sistemas familiares a estudantes e docentes de Engenharia de Software e pela disponibilidade no corpus:
   - **DigitalHome SRS v1.3** (2010), sistema de automação residencial;
   - **WARC Tools Phase III** (2009), ferramentas para armazenar, organizar, converter e preservar conteúdo da web.
2. **Cinco requisitos por documento**, todos formulados com o termo **"shall"** (indicação de obrigatoriedade), distribuídos ao longo do documento:
   - *WARC Tools:* aproximadamente a cada cinco requisitos com "shall", a partir do primeiro.
   - *DigitalHome:* distribuídos entre as seções 3.4, 4.1, 4.3, 4.5 e 5.1, sem intervalo fixo.
3. A seleção **não considerou a presença ou a ausência de ambiguidades** nos requisitos. Uma ferramenta de inteligência artificial ajudou a sugerir o esquema de espaçamento e os requisitos candidatos.
4. **De 10 para 8:** pela estimativa de tempo de revisão (15 a 20 minutos por revisor), foram mantidos os **quatro primeiros** de cada documento e excluídos os últimos da seleção, **independentemente do conteúdo**.

## Requisitos

| Código | Documento | Requisito no documento | Situação |
|---|---|---|---|
| REQ-01 | DigitalHome SRS v1.3 | 3.4.3.2 | Analisado |
| REQ-02 | DigitalHome SRS v1.3 | 4.1.3 | Analisado |
| REQ-03 | DigitalHome SRS v1.3 | 4.3.1 | Analisado |
| REQ-04 | DigitalHome SRS v1.3 | 4.5.3 | Analisado |
| — | DigitalHome SRS v1.3 | 5.1.3 | Excluído (tempo de revisão) |
| REQ-05 | WARC Tools Phase III | NFR 1 | Analisado |
| REQ-06 | WARC Tools Phase III | NFR 6 | Analisado |
| REQ-07 | WARC Tools Phase III | FR 1 | Analisado |
| REQ-08 | WARC Tools Phase III | FR 13 | Analisado |
| — | WARC Tools Phase III | FR 19 | Excluído (tempo de revisão) |

## Lista completa dos requisitos com "shall"

A lista de todos os requisitos com "shall" de cada documento, em ordem, com os selecionados marcados:

- [selecao_requisitos.csv](selecao_requisitos.csv): abre direto no navegador.
- [selecao_requisitos.xlsx](selecao_requisitos.xlsx): planilha, uma aba por documento (o GitHub não mostra `.xlsx`; baixe para abrir).

Total contado: **61** requisitos com "shall" no DigitalHome e **27** no WARC Tools. A contagem foi automática, sobre o texto dos PDFs, e deve ser conferida por amostragem.

### Como a lista foi montada

1. Cada requisito é um item com número próprio (DigitalHome: 3.4.3.2, 4.1.3...; WARC: NFR 1, FR 13...).
2. Entra na lista se o texto do item (até 8 linhas) contém a palavra "shall".
3. Subitens numerados (por exemplo 4.3.1.1) contam como itens próprios.
4. A posição é a ordem de aparição no documento.

Atenção: outra forma de contar (por exemplo, ignorar subitens ou itens em tabelas) muda as posições. Para conferir, abra os PDFs e procure por "shall" (Ctrl+F).

Leitura honesta: a seleção ficou espaçada ao longo dos documentos, mas não segue uma regra de passo fixo exata no DigitalHome.

## Limitações

A seleção foi feita por uma autora, por familiaridade e **sem sorteio**, e o conjunto é pequeno (8 requisitos de 2 documentos). Por isso os resultados do estudo não devem ser generalizados.

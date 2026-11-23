# 🔎 Ambíguo para quem? Veredito igual, justificativas diferentes na leitura crítica de requisitos

*Material de replicação de um estudo piloto que compara a revisão humana e uma LLM na identificação de ambiguidades em requisitos de software.*

![licença](https://img.shields.io/badge/licen%C3%A7a-CC%20BY%204.0-blue)
![tipo](https://img.shields.io/badge/estudo-piloto-orange)
![squad](https://img.shields.io/badge/Squad-05-purple)
![curso](https://img.shields.io/badge/Engenharia%20de%20Software-Unipampa-green)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24427857.svg)](https://doi.org/10.5281/zenodo.24427857)

> [!NOTE]
> **Artigo:** PDF final disponível na versão de dezembro de 2026 · **DOI:** [10.5281/zenodo.24427857](https://doi.org/10.5281/zenodo.24427857)

---

## 🧭 Navegação rápida

| Quero... | Vá para |
|---|---|
| Entender o estudo em 1 minuto | [📝 Resumo](#resumo) |
| Ver o prompt enviado à LLM | [🤖 prompt/prompt_llm.txt](prompt/prompt_llm.txt) |
| Ver o formulário dos revisores | [📋 instrumentos/formulario.md](instrumentos/formulario.md) |
| Ver as respostas da LLM | [💬 saidas_llm/](saidas_llm/) |
| Ver as respostas dos revisores | [👥 respostas_humanas/](respostas_humanas/) |
| Conferir a seleção dos requisitos | [🧾 selecao_requisitos/](selecao_requisitos/) |
| Refazer a análise e o kappa | [📊 analise/](analise/) |
| Recalcular as tabelas do artigo | [🔁 Como reproduzir](#reproduzir) |
| Saber qual arquivo gera qual tabela | [🗺️ Mapa para o artigo](#mapa) |
| Saber como citar | [📌 Como citar](#como-citar) |

---

<a id="identificacao"></a>
## 🎓 Identificação

| | |
|---|---|
| 🏛️ **Universidade** | Universidade Federal do Pampa (Unipampa) |
| 📍 **Campus** | Alegrete |
| 💻 **Curso** | Bacharelado em Engenharia de Software |
| 📚 **Disciplina** | Verificação e Validação |
| 🔢 **Código** | AL0342 |
| 👩‍🏫 **Professora** | Anielle Severo Lisboa de Andrade |
| 👥 **Squad** | 05 · Bloco temático: Leitura Crítica de Requisitos por IA |

<a id="autoras"></a>
## ✍️ Autoras

| Nome | E-mail institucional |
|---|---|
| Hanna Mendonça | [hannamendonca.aluno@unipampa.edu.br](mailto:hannamendonca.aluno@unipampa.edu.br) |
| Mirieli de Oliveira | [mirielioliveira.aluno@unipampa.edu.br](mailto:mirielioliveira.aluno@unipampa.edu.br) |
| Natalia Perri | [nataliaperri.aluno@unipampa.edu.br](mailto:nataliaperri.aluno@unipampa.edu.br) |
| Vitória Garcia | [vitoriapg.aluno@unipampa.edu.br](mailto:vitoriapg.aluno@unipampa.edu.br) |

---

<a id="resumo"></a>
## 📝 Resumo

A ambiguidade em requisitos de software escritos em linguagem natural pode levar a interpretações divergentes, e sua identificação costuma depender de revisão humana. Este estudo piloto investiga em que medida a revisão humana e uma LLM concordam e divergem na identificação de ambiguidades em requisitos de software já existentes. Oito requisitos do corpus PURE foram avaliados de forma independente por nove revisores humanos e por três execuções do ChatGPT (versão web gratuita), sem tratar nenhuma das condições como gabarito. A concordância no veredito (ambíguo ou não) foi medida pelo kappa de Cohen por requisito, e os apontamentos foram comparados qualitativamente. Os veredictos agregados coincidiram nos oito requisitos (κ de Cohen = 1,00), mas os nove revisores concordaram pouco entre si (κ de Fleiss ≈ 0,06) e, sem os três integrantes do grupo, o κ de Cohen cai para 0,09. Os apontamentos coincidiram integralmente em apenas dois requisitos, com correspondência parcial em cinco. Como a LLM classificou sete dos oito requisitos como ambíguos e o número de requisitos é reduzido, os resultados não devem ser generalizados.

<details>
<summary>🇬🇧 <strong>Abstract</strong> (clique para abrir)</summary>

Ambiguity in natural language software requirements can lead to divergent interpretations, and identifying it usually relies on human review. This pilot study investigates the extent to which human review and an LLM agree and diverge in identifying ambiguities in existing software requirements. Eight requirements from the PURE corpus were evaluated independently by nine human reviewers and by three executions of ChatGPT (free web version), without treating either condition as ground truth. Agreement on the verdict (ambiguous or not) was measured per requirement with Cohen's kappa, and the findings were compared qualitatively. The aggregated verdicts agreed on all eight requirements (Cohen's κ = 1.00), but the nine reviewers agreed little among themselves (Fleiss' κ ≈ 0.06), and without the three group members Cohen's κ drops to 0.09. The findings matched fully in only two requirements and partially in five. Since the LLM classified seven of the eight requirements as ambiguous and the number of requirements is small, the results should not be generalized.

</details>

<!-- Este resumo deve ficar igual ao resumo do artigo. Se um mudar, atualize o outro. -->

---

<a id="arquivos"></a>
## 📂 O que tem em cada pasta

| Pasta | Conteúdo | Abrir |
|---|---|---|
| 📄 `artigo/` | PDF do artigo | [artigo/](artigo/) |
| 🤖 `prompt/` | Prompt integral das 3 execuções (zero-shot, com os 8 requisitos em inglês e tradução de apoio) | [prompt_llm.txt](prompt/prompt_llm.txt) |
| 📋 `instrumentos/` | Texto do formulário aplicado aos revisores | [formulario.md](instrumentos/formulario.md) |
| 💬 `saidas_llm/` | As 3 saídas brutas do ChatGPT, sem edição | [execucao_1.txt](saidas_llm/execucao_1.txt) · [execucao_2.txt](saidas_llm/execucao_2.txt) · [execucao_3.txt](saidas_llm/execucao_3.txt) |
| 👥 `respostas_humanas/` | Respostas dos revisores, anonimizadas, e dicionário de dados | [respostas_humanas.csv](respostas_humanas/respostas_humanas.csv) · [dicionario_de_dados.md](respostas_humanas/dicionario_de_dados.md) |
| 🧾 `selecao_requisitos/` | Requisitos com "shall" de cada documento, em ordem, com os selecionados destacados | [selecao_requisitos.csv](selecao_requisitos/selecao_requisitos.csv) · [selecao_requisitos.xlsx](selecao_requisitos/selecao_requisitos.xlsx) · [leiame](selecao_requisitos/LEIAME.md) |
| 📊 `analise/` | Planilha de análise e cópias em CSV (regras de agregação, kappa, estabilidade, análise por requisito) | [README](analise/README.md) · [planilha_de_analise.xlsx](analise/planilha_de_analise.xlsx) |
| 🐍 `scripts/` | Script que recalcula as tabelas de concordância do artigo | [calcular_concordancia.py](scripts/calcular_concordancia.py) |

---

<a id="metodo"></a>
## ⚙️ Em poucas linhas: o método

- 📚 **Corpus:** PURE (Ferrari et al., 2017). Dois documentos: *DigitalHome SRS v1.3* e *WARC Tools Phase III*. Oito requisitos, em inglês, com tradução de apoio em português.
- 👥 **Condição humana:** 9 revisores (5 estudantes, 3 integrantes do grupo e 1 docente de Engenharia de Software), por formulário, entre 09/11/2026 e 14/11/2026.
- 🤖 **Condição LLM:** ChatGPT (versão web gratuita), 3 execuções em 09/11/2026, em chats temporários, com o mesmo prompt.

**Regras de agregação**

| Condição | Regra |
|---|---|
| 👥 Humana | Requisito ambíguo quando **5 ou mais dos 9** revisores responderam "Sim" (sem empate) |
| 🤖 LLM | Requisito ambíguo quando **2 ou mais das 3** execuções responderam "Sim" |
| 🤝 Concordância | Kappa de Cohen por requisito, sobre o veredito binário |
| 🔁 Estabilidade da LLM | Veredito e tipo idênticos nas 3 execuções |
| 👥 Entre revisores | Kappa de Fleiss entre os 9 revisores e concordância individual de cada um com a LLM |
| 🔎 Sensibilidade | Repete a comparação sem os 3 integrantes do grupo (ambíguo se 4 ou mais de 6). **Exploratória**: definida depois de ver os dados |

<a id="reproduzir"></a>
## 🔁 Como reproduzir a análise

Os números das tabelas de contagem, de concordância e de sensibilidade do artigo saem de um script que usa **só a biblioteca padrão do Python** (3.8 ou mais novo, sem instalar nada). Leva menos de 1 segundo.

```bash
git clone https://github.com/vitoriapgarcia7/ambiguo-para-quem.git
cd ambiguo-para-quem
python scripts/calcular_concordancia.py
```

Se preferir a planilha, abra a [planilha de análise](analise/planilha_de_analise.xlsx): as abas calculam, nesta ordem, o resultado humano (maioria), o resultado da LLM (2 de 3), a tabela de contagem, o kappa de Cohen e a estabilidade.

Para refazer o estudo do zero, use o [prompt integral](prompt/prompt_llm.txt) em chats temporários novos, 3 vezes, e aplique as regras de agregação acima.

<a id="mapa"></a>
## 🗺️ Mapa para o artigo

Qual arquivo gera qual tabela:

| No artigo | Arquivo | Como |
|---|---|---|
| Tabela 2 (Sim por requisito e condição) | [`respostas_humanas.csv`](respostas_humanas/respostas_humanas.csv) e [`execucoes_llm.csv`](analise/execucoes_llm.csv) | `python scripts/calcular_concordancia.py` |
| Tabela 3 (tipos de ambiguidade) | [`analise_por_requisito.csv`](analise/analise_por_requisito.csv) | classificação manual das autoras |
| Tabela 4 (concordância e kappa de Cohen) | [`concordancia.csv`](analise/concordancia.csv) | o mesmo script confere o resultado |
| Tabela 5 (estabilidade das 3 execuções) | [`execucoes_llm.csv`](analise/execucoes_llm.csv) | leitura direta |
| Tabela de sensibilidade (Fleiss e sem os integrantes) | [`respostas_humanas.csv`](respostas_humanas/respostas_humanas.csv) | `python scripts/calcular_concordancia.py` |
| Tabela dos três grupos | [`analise_por_requisito.csv`](analise/analise_por_requisito.csv) | classificação manual das autoras |

> [!NOTE]
> Confira os números das tabelas no PDF final: eles podem mudar de posição na versão de dezembro.

## 🗃️ De onde vêm os dados

- **Requisitos:** 8 requisitos do corpus [PURE](https://doi.org/10.1109/RE.2017.29), listados em [`selecao_requisitos/`](selecao_requisitos/).
- **Respostas humanas:** formulário eletrônico, coletadas de 09/11/2026 a 14/11/2026. **Anonimizadas**: sem nomes, e-mails ou carimbo de data e hora, e com as colunas em ordem embaralhada.
- **Execuções da LLM:** 3 execuções em 09/11/2026 (17h02, 17h24 e 17h27), registradas em [`saidas_llm/`](saidas_llm/).

## 🤖 O modelo usado

ChatGPT, versão web, plano gratuito, 3 execuções em chats temporários em 09/11/2026. **A interface não informou o modelo nem a versão**, e os parâmetros de geração (temperatura, top-p) não são configuráveis nessa interface. O prompt exato está em [`prompt/`](prompt/).

---

> [!WARNING]
> **Limitações de replicação.** O ChatGPT foi usado pela interface web gratuita: **o modelo e a versão não foram informados**, e os parâmetros de geração não eram configuráveis. A replicação exata não é garantida. O PURE é um corpus público e é possível que o modelo tenha tido contato com ele no treinamento, o que não foi verificado.

> [!IMPORTANT]
> **Corpus.** Os documentos originais do PURE **não são redistribuídos aqui**. Use o corpus original (Ferrari et al., 2017). Os oito requisitos usados aparecem no [prompt](prompt/prompt_llm.txt) porque fazem parte do material submetido à LLM.

> [!CAUTION]
> **Dados pessoais.** As respostas dos revisores estão **anonimizadas**: sem e-mails, sem nomes e sem carimbo de data e hora. A única indicação de perfil é a de que `R1`, `R5` e `R8` são integrantes do grupo, necessária para a análise de sensibilidade. Veja o [dicionário de dados](respostas_humanas/dicionario_de_dados.md).

---

<a id="licenca"></a>
## ⚖️ Licença

Texto, dados e documentação: **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br)**. Código (`scripts/`): **[MIT](scripts/LICENSE)**.

<a id="como-citar"></a>
## 📌 Como citar

O GitHub mostra o botão **"Cite this repository"** (arquivo [CITATION.cff](CITATION.cff)). Em BibTeX:

```bibtex
@dataset{ambiguo_para_quem_2026,
  author    = {Mendonça, Hanna and de Oliveira, Mirieli and Perri, Natalia and Garcia, Vitória},
  title     = {Ambíguo para quem? Material de replicação},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24427857},
  url       = {https://doi.org/10.5281/zenodo.24427857}
}
```

<sub>Squad 05 · Verificação e Validação (AL0342) · Unipampa, campus Alegrete · Bacharelado em Engenharia de Software</sub>
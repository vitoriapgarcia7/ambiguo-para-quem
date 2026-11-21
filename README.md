# 🔎 Ambíguo para quem? Veredito igual, justificativas diferentes na leitura crítica de requisitos

*Material de replicação de um estudo piloto que compara a revisão humana e uma LLM na identificação de ambiguidades em requisitos de software.*

![licença](https://img.shields.io/badge/licen%C3%A7a-CC%20BY%204.0-blue)
![tipo](https://img.shields.io/badge/estudo-piloto-orange)
![squad](https://img.shields.io/badge/Squad-05-purple)
![curso](https://img.shields.io/badge/Engenharia%20de%20Software-Unipampa-green)
<!-- Depois da release no Zenodo, descomente e troque XXXXXXX pelo número do DOI:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
-->

> [!NOTE]
> **Artigo:** PDF final disponível na versão de dezembro de 2026 · **DOI:** [colar aqui o DOI do Zenodo]

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

A ambiguidade em requisitos de software escritos em linguagem natural pode levar a interpretações divergentes, e sua identificação costuma depender de revisão humana. Este estudo piloto investiga em que medida a revisão humana e uma LLM concordam e divergem na identificação de ambiguidades em requisitos de software já existentes. Oito requisitos do corpus PURE foram avaliados de forma independente por nove revisores humanos e por três execuções do ChatGPT (versão web gratuita), sem tratar nenhuma das condições como gabarito. A concordância no veredito (ambíguo ou não) foi medida pelo kappa de Cohen por requisito, e os apontamentos foram comparados qualitativamente. As duas condições concordaram nos oito requisitos (κ = 1,00), mas os apontamentos coincidiram integralmente em apenas dois, com correspondência parcial em cinco. A LLM classificou sete dos oito requisitos como ambíguos e os nove revisores concordaram pouco entre si, o que, somado ao número reduzido de requisitos, limita a generalização dos resultados.

<details>
<summary>🇬🇧 <strong>Abstract</strong> (clique para abrir)</summary>

Ambiguity in natural language software requirements can lead to divergent interpretations, and identifying it usually relies on human review. This pilot study investigates the extent to which human review and an LLM agree and diverge in identifying ambiguities in existing software requirements. Eight requirements from the PURE corpus were evaluated independently by nine human reviewers and by three executions of ChatGPT (free web version), without treating either condition as ground truth. Agreement on the verdict (ambiguous or not) was measured per requirement with Cohen's kappa, and the findings were compared qualitatively. The two conditions agreed on all eight requirements (κ = 1.00), but the findings matched fully in only two and partially in five. The LLM classified seven of the eight requirements as ambiguous and the nine reviewers agreed little among themselves, which, together with the small number of requirements, limits the generalizability of the results.

</details>

> [!TIP]
> Este resumo deve ficar **igual** ao resumo do artigo. Se um mudar, atualize o outro.

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
| 🧾 `selecao_requisitos/` | Requisitos com "shall" de cada documento, em ordem, com os selecionados destacados | [selecao_requisitos.xlsx](selecao_requisitos/selecao_requisitos.xlsx) · [leiame](selecao_requisitos/LEIAME.md) |
| 📊 `analise/` | Planilha de análise (regras de agregação, kappa, estabilidade, análise por requisito) | [planilha_de_analise.xlsx](analise/planilha_de_analise.xlsx) |

---

<a id="metodo"></a>
## ⚙️ Em poucas linhas: o método

- 📚 **Corpus:** PURE (Ferrari et al., 2017). Dois documentos: *DigitalHome SRS v1.3* e *WARC Tools Phase III*. Oito requisitos, em inglês, com tradução de apoio em português.
- 👥 **Condição humana:** 9 revisores (8 estudantes e 1 docente de Engenharia de Software), por formulário, entre 09/11/2026 e 14/11/2026.
- 🤖 **Condição LLM:** ChatGPT (versão web gratuita), 3 execuções em 09/11/2026, em chats temporários, com o mesmo prompt.

**Regras de agregação**

| Condição | Regra |
|---|---|
| 👥 Humana | Requisito ambíguo quando **5 ou mais dos 9** revisores responderam "Sim" (sem empate) |
| 🤖 LLM | Requisito ambíguo quando **2 ou mais das 3** execuções responderam "Sim" |
| 🤝 Concordância | Kappa de Cohen por requisito, sobre o veredito binário |
| 🔁 Estabilidade da LLM | Veredito e tipo idênticos nas 3 execuções |

<a id="reproduzir"></a>
## 🔁 Como reproduzir a análise

1. Abra a [planilha de análise](analise/planilha_de_analise.xlsx).
2. Confira que as [respostas dos revisores](respostas_humanas/respostas_humanas.csv) correspondem às colunas dos revisores.
3. As abas calculam, nesta ordem: resultado humano (maioria), resultado da LLM (2 de 3), tabela de contagem, kappa de Cohen e estabilidade.

---

> [!WARNING]
> **Limitações de replicação.** O ChatGPT foi usado pela interface web gratuita: **o modelo e a versão não foram informados**, e os parâmetros de geração não eram configuráveis. A replicação exata não é garantida. O PURE é um corpus público e é possível que o modelo tenha tido contato com ele no treinamento, o que não foi verificado.

> [!IMPORTANT]
> **Corpus.** Os documentos originais do PURE **não são redistribuídos aqui**. Use o corpus original (Ferrari et al., 2017). Os oito requisitos usados aparecem no [prompt](prompt/prompt_llm.txt) porque fazem parte do material submetido à LLM.

> [!CAUTION]
> **Dados pessoais.** As respostas dos revisores estão **anonimizadas**: sem e-mails, sem nomes e sem carimbo de data e hora. Veja o [dicionário de dados](respostas_humanas/dicionario_de_dados.md).

---

<a id="licenca"></a>
## ⚖️ Licença

Texto, dados e documentação: **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br)**.

<a id="como-citar"></a>
## 📌 Como citar

O GitHub mostra o botão **"Cite this repository"** (arquivo [CITATION.cff](CITATION.cff)). Em BibTeX:

```bibtex
@dataset{ambiguo_para_quem_2026,
  author    = {Mendonça, Hanna and de Oliveira, Mirieli and Perri, Natalia and Garcia, Vitória},
  title     = {Ambíguo para quem? Material de replicação},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.XXXXXXX},
  url       = {https://doi.org/10.5281/zenodo.XXXXXXX}
}
```

<sub>Squad 05 · Verificação e Validação (AL0342) · Unipampa, campus Alegrete · Bacharelado em Engenharia de Software</sub>

# Formulário aplicado aos revisores

Formulário eletrônico (Google Forms) respondido individualmente pelos revisores entre 09/11/2026 e 14/11/2026. Cada revisor analisou os **8 requisitos** (REQ-01 a REQ-08), apresentados no idioma original (inglês) e acompanhados da tradução de apoio em português, na mesma ordem usada com a LLM.

O endereço de e-mail foi coletado apenas para controle das respostas e não é divulgado.

## Texto de abertura do formulário

> Obrigada por participar! Você vai ler 8 requisitos de software e dizer, para cada um, se ele é ambíguo ou não. Leva cerca de 15 a 20 minutos. Não existe resposta certa ou errada: queremos saber como você lê cada requisito.
>
> Um requisito é AMBÍGUO quando, com o mesmo contexto fornecido, permite pelo menos duas interpretações plausíveis que levam a consequências diferentes para o comportamento esperado do sistema ou para os critérios de aceitação (o que seria testado). Sugestões de estilo e informação apenas faltando, sem duas leituras plausíveis, não contam.
>
> Os 4 tipos de ambiguidade:
> - Lexical: uma palavra tem mais de um sentido.
> - Sintática: a estrutura da frase permite mais de uma leitura.
> - Referencial: um pronome ou expressão pode se referir a mais de uma coisa.
> - Pragmática: o sentido depende de contexto ou convenção que o texto não deixa claros.
>
> Os requisitos vêm de documentos reais em inglês (PURE). Cada um aparece com o texto original e uma tradução de apoio em português. Avalie o requisito considerando os dois textos juntos. Pode usar dicionário para palavras soltas, mas não use IA nem tradutores automáticos para traduzir a frase inteira.
>
> Você não precisa conhecer o assunto do documento. Avalie apenas o que o texto permite entender. Se algo parecer ambíguo só no original ou só na tradução, marque a sua resposta normalmente e escreva isso no campo de comentário do final.
>
> Regras: leia sozinha, sem conversar com outras pessoas até concluir. Não use IA nem pesquise sobre os requisitos. Use só o texto fornecido. Responda todos os requisitos, inclusive os que achar claros (marque "Não"). Suas respostas serão usadas apenas neste trabalho acadêmico.

## Confirmação

Antes de começar, o revisor marcava:

- ☐ Li as regras, farei a revisão sozinha, sem usar IA, e responderei uma única vez.

## Perguntas para cada requisito (REQ-01 a REQ-08)

1. **Este requisito é ambíguo?**
   - Sim
   - Não

Quem respondia **Sim** descrevia também:

2. **Trecho ambíguo** (copie o pedaço do requisito)
   - Resposta curta.
3. **Tipo de ambiguidade**
   - Lexical
   - Sintática
   - Referencial
   - Pragmática
4. **Descreva as duas interpretações possíveis e o que muda no comportamento do sistema entre elas**
   - Resposta longa.

## Final

- **Comentários (opcional):** por exemplo, se algo pareceu ambíguo só no original ou só na tradução.

Os tipos de ambiguidade e o critério são os mesmos do [prompt](../prompt/prompt_llm.txt) enviado à LLM.

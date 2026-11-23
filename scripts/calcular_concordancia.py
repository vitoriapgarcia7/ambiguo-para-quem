#!/usr/bin/env python3
"""Recalcula os números de concordância do artigo "Ambíguo para quem?".

Usa apenas a biblioteca padrão do Python 3.8 ou mais novo. Leva menos de 1 segundo.

Uso (na raiz do repositório):
    python scripts/calcular_concordancia.py
    python scripts/calcular_concordancia.py --integrantes R1,R5,R8

Entradas:
    respostas_humanas/respostas_humanas.csv   Sim/Não de cada revisor (R1 a R9)
    analise/execucoes_llm.csv                 Sim/Não das 3 execuções da LLM

Saídas (impressas na tela):
    Tabela 2  contagens e veredito por requisito e por condição
    Tabela 4  concordância observada, esperada e kappa de Cohen (humanos x LLM)
    Tabela 6  kappa de Fleiss, concordância individual com a LLM e a análise de
              sensibilidade sem os integrantes do grupo
"""
import argparse
import csv
import itertools
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def ler_humanos(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        linhas = list(csv.reader(f))
    revisores = linhas[0][1:]
    reqs = [l[0] for l in linhas[1:]]
    m = [[1 if c.strip() == "Sim" else 0 for c in l[1:]] for l in linhas[1:]]
    return reqs, revisores, m


def ler_llm(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        linhas = list(csv.reader(f))
    i = next(k for k, l in enumerate(linhas) if l and l[0] == "Requisito")
    saida = {}
    for l in linhas[i + 1:]:
        if l and l[0].startswith("REQ-"):
            saida[l[0]] = [1 if c.strip() == "Sim" else 0 for c in l[1:4]]
    return saida


def cohen(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    k = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    return po, pe, k


def fleiss(m):
    n_req, n_rev = len(m), len(m[0])
    pi = [(s * (s - 1) + (n_rev - s) * (n_rev - s - 1)) / (n_rev * (n_rev - 1))
          for s in (sum(l) for l in m)]
    p_obs = sum(pi) / n_req
    p_sim = sum(sum(l) for l in m) / (n_req * n_rev)
    p_esp = p_sim ** 2 + (1 - p_sim) ** 2
    return p_obs, p_esp, (p_obs - p_esp) / (1 - p_esp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--integrantes", default="R1,R5,R8",
                    help="IDs (anonimizados) dos revisores que são integrantes do grupo")
    a = ap.parse_args()

    reqs, revs, m = ler_humanos(RAIZ / "respostas_humanas" / "respostas_humanas.csv")
    llm = ler_llm(RAIZ / "analise" / "execucoes_llm.csv")
    grupo = [r.strip() for r in a.integrantes.split(",")]
    idx_g = [revs.index(r) for r in grupo]
    idx_e = [j for j in range(len(revs)) if j not in idx_g]

    veredito_llm = [1 if sum(llm[r]) >= 2 else 0 for r in reqs]
    nome = {1: "Sim", 0: "Não"}

    print("TABELA 2: veredito por requisito e condição")
    print("REQ     Sim humanos(de 9)  Humano  Sim LLM(de 3)  LLM")
    veredito_h = []
    for r, linha in zip(reqs, m):
        s = sum(linha)
        v = 1 if s >= 5 else 0
        veredito_h.append(v)
        print(f"{r}  {s:>10}          {nome[v]:<6}  {sum(llm[r]):>8}       {nome[veredito_llm[reqs.index(r)]]}")

    po, pe, k = cohen(veredito_h, veredito_llm)
    print("\nTABELA 4: humanos (>=5 de 9) x LLM (>=2 de 3)")
    print(f"  concordância observada = {po:.2f}   esperada = {pe:.2f}   kappa de Cohen = {k:.2f}")

    po_f, pe_f, k_f = fleiss(m)
    ind = [sum(m[i][j] == veredito_llm[i] for i in range(len(reqs))) for j in range(len(revs))]
    print("\nTABELA 6: nove revisores")
    print(f"  kappa de Fleiss = {k_f:.2f}  (Po = {po_f:.2f}, Pe = {pe_f:.2f})")
    print(f"  veredito individual igual ao da LLM: {sum(ind)}/{len(reqs) * len(revs)}"
          f" ({100 * sum(ind) / (len(reqs) * len(revs)):.1f}%)")
    print("  por revisor:", ", ".join(f"{r}={x}/8" for r, x in zip(revs, ind)))

    ext = [[l[j] for j in idx_e] for l in m]
    k_ext = fleiss(ext)[2]
    corte = len(idx_e) // 2 + 1  # mais da metade
    v_ext = [1 if sum(l) >= corte else 0 for l in ext]
    ind_e = sum(ind[j] for j in idx_e)
    print(f"\nTABELA 6: seis externos (sem {', '.join(grupo)}); ambíguo se >= {corte} de {len(idx_e)}")
    print(f"  kappa de Fleiss = {k_ext:.2f}")
    print(f"  veredito individual igual ao da LLM: {ind_e}/{len(reqs) * len(idx_e)}"
          f" ({100 * ind_e / (len(reqs) * len(idx_e)):.1f}%)")
    print(f"  requisitos ambíguos pela maioria: {sum(v_ext)} de {len(reqs)}")
    print("  votos por requisito:", [sum(l) for l in ext])
    print(f"  kappa de Cohen (externos x LLM) = {cohen(v_ext, veredito_llm)[2]:.2f}")
    print("\nNota: empates (3 de 6) contam como não ambíguo. A análise de sensibilidade foi"
          " definida depois de ver os dados e é exploratória.")


if __name__ == "__main__":
    main()

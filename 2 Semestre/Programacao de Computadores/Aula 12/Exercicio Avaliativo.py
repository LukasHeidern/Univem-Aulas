### Lucas Ferrari lopes - 617571

import re

dna_rna = { 'ATA': 'UAU',
            'ACA': 'UGU',
            'AAC': 'UUG',
            'AGC': 'UCG',
            'CAC': 'GUG',
            'CGA': 'GCU',
            'GTA': 'CAU'}

rna_aa = {'UAU': 'Ile',
          'UGU': 'Thr',
          'UUG': 'Asn',
          'UCG': 'Ser',
          'GUG': 'His',
          'GCU': 'Arg',
          'CAU': 'Val'}

def check_dna(dna):
    if re.fullmatch(r"(([GCTA]){3})+", dna):
        codons = [dna[i:i + 3] for i in range(0, len(dna), 3)]
        if codons[-1] in ["ATC", "ATT", "ACT"] and all(codon in dna_rna.keys() for codon in codons[:-1]):
            return True
        else: return False
    else: return False

def gen_rna(dna):
    rna = ''
    for i in [dna[i:i + 3] for i in range(0, len(dna), 3)][:-1]: rna += dna_rna[i]
    return rna

def gen_polypeptide(rna):
    polypeptide = []
    for i in [rna[i:i + 3] for i in range(0, len(rna), 3)]:
        polypeptide.append(rna_aa[i])
    return '-'.join(polypeptide)

def main():
    while True:
        dna = input("Digite o DNA: ").upper()
        if check_dna(dna):
            rna = gen_rna(dna)
            polypeptide = gen_polypeptide(rna)
            print(f"\nDNA - {dna}\nRNA - {rna}\nPolipeptideos - {polypeptide}\n")
        else: print("DNA invalido!")
        if input("Deseja continuar? [Sn]: ")[0] not in "Ss":
            break

main()

### [T,G,C,A]
### [A,C,G,U]
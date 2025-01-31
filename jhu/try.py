from Bio.Blast import NCBIWWW, NCBIXML
fasta_string = open("myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

blast_record = NCBIXML.read(result_handle)
print(len(blast_record.alignments))

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("***ALIGNMENT***")
            print(f'sequence: {alignment.title}')
            print(f'length: {alignment.length}')
            print(f'e value: {hsp.expect}')
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)

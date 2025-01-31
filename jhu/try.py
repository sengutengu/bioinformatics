from Bio.Blast import NCBIWWW, NCBIXML
fasta_string = open("myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

blast_record = NCBIXML.read(result_handle)
print(len(blast_record.alignments))


min_e = 100
min_title = ""
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < min_e:
            min_e = hsp.expect
            min_title = alignment.title

    
print(min_title)
print(min_e)
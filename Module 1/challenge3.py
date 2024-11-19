from bioinformatics_module import reverse_complement

pattern = "AGATTAGATCTTTCTTAGAAGAGGCTAGGTACCAGTATTCGCTTTATGTGTCCTATACAATACACTTTACCCGTTTGCGTGCTAAGTCTACATTTCGTATCAAAGAACTCCGGAATGGGATATAAAACCGTGGGCATCGACCGGCCCACCGCGAATGCTAGGAGGGAACAAGAAGATGGTAATCTTTGGATCTCACCGGGGAGGTAAACGATCGGCTAAGTCTCATAAGTTACGGCTGTACCTAACGGGACACAACTAAGGACGATTCTAGCTAGGTTAAAGCCAAGGCTTGCGAGAGGATGTACACGATTCGATGAAAACCTCTCGCTGTGTCCGATGCTGTGGGCGCCACGTTGAGTATTTGATCATACTTGTAATCGACCAAGCTGGTAGCCAAGTTAGCGAGATCCATAGCGGTTGGCTTTCCCCATCGTTGGTTTGCCTACGTGAGCCGGGTCCCAACGTAGGTAGAGTATTACTTGTGCGGTCTATACGAACTAAGCCATTGGTGGGCCAAGTTCAATTCTGTGATATTAGTATACCGACTGCTTTTGTAACGCCCTTGGCCCCATCCCTTGGTTAATGCACCATGCCGAAAGAGTTAACTACCACGCAAACTAATATCACTAAATCTAGATTTATTGCACGATATAGAACATATGCTATTTCATGCGTGGTTTTAAGGTCTCTCGGGTTATAGACCTTTAACCAAGACTTCCCATGAGTCGTATGACGTACACTCCAGGTCACGCGTCGCTTAAGGGACAGTACTTGACGGTTTGGGTATGTTACGGAGGACGGAGGCCCAGCATCGGTGTTCATTAGCCTCTCGACCGCCTCATCTTCCTTCAAGATTTCCACAGACGACCCTGTATGAGTAACAGGCCAACTATATAATAACAGCGAGCCCGAGCGTATTGTATGACGTCGGATTTGAACCCAATTAGACAGGGGGTTAACGCCTCCTAATTAAGCCGAAGTTACGTTGGTATTAACATGGCCCGCGCGTTGCACACTGGACGGCCTTTTTCGCCCGCCGTCGTTTTCACCTCGTTCTCCCCTTTAAACTGTCACACTTACACTGACTGCATCTAGAACACGGTGTAAAGCCATTTAGCCCAAGCGTCGCACCGTGTTGGCGCACTTCCAGTTAATACGAGCGATAGGGTAACGATGTGTACACAGAAGAAAACCAACGTATATTTAAGCGTGAGTTACTGAGTTGGTAACTATGATCCCGGGGACCTTCCGTGAAGTCTCCCCGGCGCGCTCCGTAATGACTCAAAGAGGCAGCTTAGCGACAACATTGAAGCCCGCCCTTCGACCCATGAGAGCGCGATATCTCGCTCTTCCCCTAGACGAAGCGACGGAATAATAGGTGTGTGGGATGGGGAATTGCGGCTACGAGACGCGGCAACAGTCGCGATTTACACTCGAAGTGCGACAGCACGTTAAGTTCGCAGTACTAAAGACGAAACATAGGCGGTGCTTACCATAGTAAACGGCTTGCACCGGCTACAAAAGTCTGCAAATCCGTTTCCGATTCTAAGTTGTGAGGGATGTTATGGGGCGAGATCTTCCGATTCCCAATCCCTGAATGCGGACTCTATTGTCAAACCTATTGGCATTTAGAATCAGCACTCTACAAGTTGCGATTTAACTAGCACTTGGGTTTATCTGGTTCGGTTGTGCGGCGGGCAGTTCCCGCGTCCCTCGGCGGGTTCCAGGTTCCTCTGAGGTGCCTTACAGAAGCACGGACCAGCACCTCCCCATGTTGTCGGACACCACCAGACAGGAGGAGAACGACCGATGACATAGTGTCAGCGTTCAGTTACCACATTACTCGAAAACGATCCAGATCCCAGGAAACGAGATTTAGTCCTACCTTCCCTTTACAGCATCTGGATCTAGCATCGTCATATTTACTTAGGACAGAGGGGTTAAGCTTGTCTTTGAAGAGGGACATTTCATAGCACTAATAGAATGGCCCAAGATTACATTGGTCTCCAAGCACGTAGCTTTCACGGCTTGCATTCGAGTGTTAAAAAACTACTTAATGGCCTTGCAAGTCTTTGCTCCGACGGTCCTTGCAAGGGTTACGCAATCAGGCCGAACAAGTCGCTAAGAGTATCAATGGTGATTTTGCCCTCGAATTACCGAATGGAGCTAAACCATACATGCGCAGGTAGGCTTGTAACTAATACGCCAGTGTGTTGTACGGATAGTAAAAAGAATGGTTACGCCATGTACGGATTCCTACAATTAAAGCAACGTACAGGCGAGAGTAACCTTGTTGCCGTGTGCTGAAAAAACGTGCATCCAGCATGATAAGATCCACAAATAAGTAGCCCACCCCTCGTGGCTACAACCTATCGACCTCTGTCGTGCGCTGGCCCTGGTGTCTGTGCTAAGAGTCATTTCGCTACTCGTAGACTCTCAGGAAAGGGTTCATACATGAACGCTCTGGCTCATCCAGCATTGGTGTAGCATTAGAAGAGCTATCGAACAATTCATAATGTCCATCTATATGGTAAAATTGGATCAATGCCCTATCTATAACGACAATGATTGAGTCCGCCAGCTACCCCAGCCTTTCCGCCTAGACGAGCTCGCATGACCCAGAGCCGGAATATGCCGCACGCTGTGGCATCGTTATTGAGCTACATTGTCTGTGTTTCAGGCACAGTATGCCATGGCGACTAGTTGCAGTTGCGGCCGGGTCAATTGACATCACGCAGACTGCATTGGAGCTCTACTCATATATGCAATCCGATCCTCGGAGAGCCCGACTCTTAGCGCGCACTCAACTCTACCAGCAGTTCGCATCCGGCAGTAGTCACACTCTTCGAGAGAACTTGGATCGTCTCTCAAGCCAGAAGATACTTACACCACACGATCAGCGCCTACACGTACAAGGCAGGTTCTCCTACGCGTCGGAGTATGCCCGTCGAGGGCCGCAGGCTTAACGGCTGGGCACCGATTCTGCAACGGCGTATACCACATTGAAGGGATAATCATGTGACAGAACAAAGAGCGAGGTGTGCTCAAAATTCGTTAGTAAACAAAGTTTGCCTTCGCTCATGTCAGAGCCCGCAGACGTAAAAAAAAACACGGGCATATGCATGTAGGAGACTTAGGGATGAGGGCGCTGCCTATGGCTTCGTAAGCCTACCGGGCACATTTAGCGACACCACTCACTCGTCTTGCAACTGAAAAGTGGATAAGGGGTAAATACCAAACGTGGCGTGGAATAACATCACGATTCCTTCTTGCGAACGACTAATAGAGCAGTGAGAAATCCGTATCTCCATCACCTGACCGCTGCGGAAGCAGAACGGAGCTATTTAAGCCTCAACTTGACCGCGCCATTTCCCGCCGCGACCATTCAAGCTATCCGCCCCGGGTGGTTTTGTTGAATTCCAGGGGTCGAAGTAGGCGTAGGCATAAGAGAACGGACGGTAGGGCATCATACGTACTGATAGTAGTAGCTCTCCCCTTTGTGTAGCGCACCTATCGTCTTTGGCAATTATAGGAAACGCAACCACTCTTATCCGTAAGATGCTATATAGCAATCGTATAAACAGGGGACGAATGGACTCGCACGCCGCGGCTGCAGGGTATGCCACCCCCGGCAATTAGCCCCAGTAATACCCCACAAGCGAAGTGGGTTTGTATCGGGCGGCATATGCTTCTTTAAGATACAGCGGCGTCTGGCATACTCGCAGGTTGCATCGAGTAACGTGCGTCGGTCACTCTGTACGTACGCTATGTTTTCGCAAATTACATGAGAATACTTATCGGCGTGTGCGTCACGTTGTGCCGCAGGGATGTGATCATGGCTTTCCTCCCATCCAGTCGTCGCCGTACCCGCCTGGCCTATTACGTGATGCTGCCTGGATCAAGAACCAAGGTAGTGCCTTCTTTGGCGCAGCGATGTTACGGCACGAGGTGATGCGGATGGGGATGGAATGGTCCCAATCAGAGGACGTCCTCGAGATGAATATGACTCTTCAATTTGCTCAACCTGACCAAGACCCACCGTAGTTGCCATGGCATAGCTGTACGTGGCATAGTTTCGAGAGATAATCAGCGCATCACTCTCGCTAGGTCTAGATTACCTGCCCCAAGGGCTTACGCTTTCTATCATCAGAGGCACTAGATTCTCGCGGGTGCCTACCTAAATCTAGTGAGGTAAGTTACATATGTATTGCCGAGCGTCTCGGGTTGTGCCAAGCGTTCAATCTGCACATAAAAGCGAGCCAAACATTAGGACTGGTGCAAGCCATATGCTAGGTCTATCCCGTTACACGCTAGGCCATGCGAGCGGGGGTGTCTCGGCTGAAATACGGTAATCTAGAAGCTCATCGGGTTTCCGAGGTATCTTCTTCGTGCTCCTGACCACAAGGGGGGTGGGCGGTGATTGCACGTCCTCGATAGCAAGCTGGACCAATCTGAGCTCTAACCGTCTACTTAGACGGCACGGAGGCTTGGCATCTGTAGCCGGTCCCTCTGTATGAATCCGTAAGTGACAATGAACCGACTTCCTACGAGAGTCCGTGCACGTTCATGACCACGTACCTGGTGGCTGTTTGCAGATCCTCACAGCACGAGGAGAACGCGTGTGCGATCTCCGATTACAGCCAAGCCGCTCGCTGAAATGGAGGGCGTGCCGTTTTGTACCACGAACGGCGTTCTGCTTGACCCACCGCCACCGTTCCGAAACATTCCAGAAACCAGACGAACTATCTCGAAGCCTTTTGAGTATACCGGTTTTGACGAAATATCAGGCGGACCGATAATACTTGGATGTTTTTCCTTGTGATCAGCTTGATATAAAGGGGCGCAACGACGCGCAAGGGTTAAAGTGTTAAAACGTACCCACGTGGACTATAACACCCCCAGCCAACACTTACCTTGCTGCCGTGAAGATTTTGTCAGGGCTAGTGTTAGGTTGAGTTATGAGTTACGGCGCAAAAGATGGGCAGTAACCTTCCCCCCACACTCTTGCAGACAACCATGACTGTGCGTGTGACACGAGCTAATGAAACTGGCATTAGGCAGGCCCCGATTCTTTTTGGCTCTGGGTTGTGGCGGATAGCATAGTGGGCATACTGTCTTCCAAGCATGCATGCGAGACTAACTTAGTGGATACAGCTAAGTCATCGACAAGTGAGAACATGCCTTTCGGTGTCAAACTAGCGAGCCGTTGTGGACTGGCGCTCACTTGTGGCCATTCGCACAAGACATGTAGACGGGTCAGGTTGTGGACCTTCAAACCAGGGTATAGGAGTCTAGTGTCCAAGGCCCGGAGAAAGTCGACGACTCACACCGCTGTCCAGGCCACAGGCCTTGTAAAGTCAGATATTGCCGCCATTCGATCTAATTGAGTAAGGCATGGCCGAGCTCTAGCAGCGTCACATCCTCGACGAGACGCCCCCTAGGCACTGTTACATTTACGTGGGCGAAGCTTGCCACTTGTCCCCGGGGCTTGGGCCCAGTACCCAGGTTCTCATCGCGGATTGCGAGCCTCGCCGACTTTACCCGCCAATCCGTTTCTTGGAGAACACTTCTACAATTCTGAACTATGGGATAGCACATATAACATGGTGGCTGAAAGAGATCGATGACTGGCAGCATCGGCACTATGTTCGTTTTGATTGCGTAAAAATGGTCTCTCAATGTTTCGAATAACTACTTCGGCACTTTAGGGAATGATCGGAAATATGCTCTGAGAGTAGTATACTACGATCATTTTATGTCGGTATGCGTGAGATTCGCACAATCGCACGCTAAATACTACTTAGAGCCGGGCCAAACCGACGGCGCAAGGAGTGACCTGTGACAGAAGACCTATAAGGCAGAGAAAGACAATGAAGGGTCCGCTAGTTTTCGACCAAAATGGACTAAACATTACTTTGACAATAACGAATGATACCAGCACCAACAATTTAGATACGGTGATATATGATCGAGCCTTGGAAAGAAATGGCTAATACAGTTTACAGTTTGGAGGAAGAAGATAAAGAACCTCACGCCGGCAGAATGATGGGTTGGTGTGATAACAGTATACGGTAGCGCAATGCTTTTGTAGACCACGGGGTAGGTATCACCGTTTAGCGGATAACATGCAAGTCTTAAGGGTGAATTTGAGCGGATTAACAAGACCTGTAAAGTGTTGTCGGCAATTAAGCGTAAATTTATTAGAGATGCGGTGCGGAGGCCTCCACAAAGGGGGTGGTGCTTTTGATCGATGTGACTGTGTGCCTCTAGCAGATAGTTGTTCCGGGTCGATTAGTCCCTCGAGACTCACGCGCCGTCAAAACGCCGACATATCCAAGGGTTGGCTGCTGCCATCGTTTGACGGACAACGGACCAAATGCTTCTATCGTATTTTACCGGATCTCCTGATGATATAATATAGTTAGAAATCCTCTTAGCTATTTGACCGCCAACACTGCGGACATAAGCCAGATACAACTGTGGTGCGTGTTTCAGTATGGTCGATTTCGGGGGGCTAACGATAATGGTAGTAAGATAACTTACGAAGGCCGATGACTGTAGCCGCGCTTTGCGATGAGTAGCACAGAACACATACTAACGCGAGATACTCTACACCATACAGATAGGTAAGTTATCTATGATTGGTGAGTCCCCTCGTCCCGTGTGAGACCTGACTATCTAATCGCGTTCGTAACGTGTAGCCATGCGTTGCATACGTGTACCCTACAAGGAAAGGGTGTCTACCCCTGGATAAACTGCTACCTACATTTGGTCATCCGACCTAGGTGGATTTATGTGCGCGGCTGGTTTGATTGACACGTTTAAGATGGACGTGGGTGGCGTGTAAAGGTGATAGAATTTGTCTACAACGAGACACTTCAAGGGCGCGGTCTATAATAATCTTTTTGCTAGCAACTAATAGTGCCTGACAGGAGTAGCGCAGTGCGTCACAGCGGTCATCTGGCAAGTTGGCTATGCGCTCCAGCCCCCCATGGGGTTAGGACATGGCTCCCCCCTGCCATATACAGCTTTTTTCGTTAAAACGGTAACCATTGGACCAACTCGAAGTAGTCTCCGTTGCTCTGTTGACCTCTGTCGCCAGACCGCTACCCCGGACCGATCCAAATTGACCCAAGCGTACTTTCTGCACCTATCACGGCATCTCACTCCGTAACCGGATTGGAGCCATGGGTTAACACTAGTCAGGCACCCTCGAGTTCGTAGATTGGACCTATGAGTTTCTTCCCGTCTTAGAGGCAGCGTCGACTCCTGACTGAATCAAAATCTACGTTTTCAAGTTTGTCATTTCAATTATATTTTCGAGTGCCCGTGTTAAGGGGCGGGAAAGTGGCTATCTGAGGTAATAGCCGAGGCCAACCTCGAAGTCAGTTAAGCGGCAAGGCCTTATGCTTGCATCACGGGAAATCGTCCGGTCGTGCATCCAGCCGCTTCCGATATCTCGATTGCTCGAAGACGTGTAAGCCAAAAGCTAAGGGGAGATGGTTATAAGAATACCGTCAGTTTATGTGGGCTTGCCTAATACACCCATGTCATGAATACACTCTGGAGTGACCTCAAACAAGATCCCGCAATTAGGTCATATCCTCCCAGGGGACGAAACCACTGGAGGTTTCATATACCCCTGGTAGGGTCATCCATTGTCGACAAGCCGACGGCGTAGAACGGGGGGGGCGCCGACTCGCCTTCCGATACTCTAGTAGAAGAGACGACGGACGTTCATTCGCGGCACACTTGGCCCCGTGCCATGACAGACCCCGAGCATCCTTTAATGCACAGAAGTTTTCACACCCTATAAGAATACTATTGTGTATCTATTCGTCCGGGCAGCAGTAAACCCCGGCCGGCGCGCGCTGATTAAGGTTCGATCTATAGTATTGTTATGGCTACTCCTGCCCCTGCTGGGCCATCTTTCTGGCATCAGCCGCTCAGCACCCCTTTAGGTGGTCTCCGCTGTTTGTGAGCGAGGCAAATGTTATAAGGCCGCCGTGAAGGCTACGATCCCTTAGTGGTGCTGCCCGCCCGACTCCCACGATCGGCAATCAAAGCTACTCCCCGGATTGACTGCTTGTTGTTGTATCCACCTTTACACAATAGGTCATAGTTTGTTGTTTCGTCTGTCCCTAACTATTCTCCTCACGCCCTGTAGTGCCGATTGTTAGACCAAACCCGCCGTAGTCAACTGAATATCGGCTGCCTAAGTCGAAGTTACCTCGTTGAGCAGCATAGGCCAGCAAAGATATAGGCTGGGCGCGTGTGTAATTGCGGTTGACGTAATCGTACCCCAATGACGCGTCGATTTTAAGATTATCGTGCGAGAACGATGCACCCGAACCAGCGAGTTACCTGGTGTTGATACCATCGGTAAAGAGCG"

print(reverse_complement(pattern))
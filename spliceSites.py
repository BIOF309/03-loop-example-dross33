"""Identifies Splice Donors and Acceptors - input file contains chromosome number, start of exon, end of exon across genome. Output file outputs bps of splice donors and acceptors""" 

exonFile = open('exon.bed', 'r')
exons = exonFile.readlines()
exonFile.close()
with open('spliceAcceptorDonor.bed', 'w') as outputFile:
    outputFile.write('Chr\tStart\tStop\tCategory\n')
    for line in exons:
        cols = line.strip().split()
        spliceAcceptorStart = int(cols[1]) - 2
        spliceDonorStop = int(cols[2]) + 2
        outputFile.write(cols[0] + '\t' + str(spliceAcceptorStart) + '\t' + cols[1] + '\t' + 'Splice Acceptor' + '\n' + cols[0] + '\t' + cols[2] + '\t' + str(spliceDonorStop) + '\t' + 'Splice Donor' + '\n')

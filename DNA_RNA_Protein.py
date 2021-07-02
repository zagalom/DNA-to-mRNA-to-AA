#DNA->RNA->Protein

print ('Are you using a DNA ou RNA string?')
RNAS= 'RNA'
Resp=input().upper()
if "DNA" in Resp:
    print('Is the strand sense or antisense? Meaning, from 5 to 3 or from 3 to 5?')
    Resp2= input().upper()
    if "ANTISENSE" in Resp2:
        print ('Please input the string')
        DNAs=input().upper()
        RNAs = DNAs.replace('A', 'u').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
        print ('The complementar RNA strand is:')
        print (RNAs)
    else:
        print ('Please input the string')
        DNAs=input().upper()
        RNAs = DNAs.replace('A', 'u').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
        print ('The complementar RNA strand is:')
        print (RNAs)
if "RNA" in Resp:
    print ('Please input the string')
    RNAs=input().upper()

#
def readable(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]

def method(seq, start=['AUG'], stop=['UAA','UAG','UGA']):
    response = ''
    started = False
    for x in readable(seq, 3):
        if x in start:
            started = True
        if x in stop:
             started=False
        if started:
            response += x
                
    yield response

for result in method(RNAs):
    b=result
print (' ')
print ('The readable part of the RNA is:')
print(result)

def translate(seq):
      
    table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                 
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UGG':'W', 'UGU':'C',
        'UGC':'C'}
    protein =""
    if len(b)%3 == 0:
  
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein+= table[codon]
    return protein
p = translate(b)
print (' ')
print ('The aa sequence is:')
print (p)
print('')
print('')
print ('Ready to close programm? Yes or no')

Close=input().lower
if "yes" in Close:
    print('Bye')

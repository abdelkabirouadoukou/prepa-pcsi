note1 = float(input("Entre la note 1"))
note1Coff1 = float(input("Entre le corfficient de note 1: "))

note2 = float(input("Entre la note 2"))
note1Coff2 = float(input("Entre le corfficient de note 2: "))

note3 = float(input("Entre la note 3"))
note1Coff3 = float(input("Entre le corfficient de note 3: "))

moyenne = (note1*note1Coff1 + note2*note1Coff2 + note3*note1Coff3)/(note1Coff1+note1Coff2+note1Coff3)

print(moyenne)
import datetime, random

class Osoba:
    #konstruktor
    def __init__(self, meno, priezvisko, rok):
        self.priezvisko = priezvisko
        self.meno = meno
        self.rok = rok
        self.vek = datetime.date.today().year - rok
        #atributy (vlastnosti)

    #metoda pozdrav
    def pozdrav(self):
        print("Ahoj, ja som", self.meno, self.priezvisko, "a narodil som sa v roku", self.rok, "cize mam", self.vek, "rokov")


    #stringova repezentacia objektu (pri print())
    def __str__(self):
        return f"{self.meno} {self.priezvisko} : Osoba"
    
class Ucitel(Osoba): #dedicnost, zdedi vsetko z triedy Osoba
    def __init__(self, meno, priezvisko, rok, titul, predmet, trieda=None):
        super().__init__(meno, priezvisko, rok) #pouzije konstruktor rodicovskej triedy
        self.titul = titul
        self.predmet = predmet
        self.trieda = trieda
    def pozdrav(self):
        print("Dobry den, ja som",self.titul, self.meno, self.priezvisko, "a ucim predmet", self.predmet, "a som stary", self.vek, "rokov")
    def vypis(self):
        return f"{self.titul} {self.meno} {self.priezvisko}, {self.predmet}, {self.vek}"


        
    def __str__(self):
        return f"{self.titul} {self.meno} {self.priezvisko} : Ucitel : {self.predmet}-{self.trieda}"

class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        print("Ahoj, volam sa", self.meno, self.priezvisko, "chodim do triedy", self.trieda, "a mam", self.vek, "rokov")
    def vypis(self):
        return f"{self.meno} {self.priezvisko}, {self.trieda}, {self.vek}"


    def __str__(self):
        return f"{self.meno} {self.priezvisko} : Student : {self.trieda}"


#vytvorenie objektu
jano = Osoba("Jantoslav", "Hrobokop", 1911)
jano.pozdrav()
print(jano)

fero = Student("Franto", "Teply", 2006, "II.CI")
fero.pozdrav()

ucitel1 = Ucitel("Michal", "Sutek", 1978, "Mgr.", "ZCY", "III.AT")
ucitel1.pozdrav()
print(ucitel1)

ucitelia = []
ziaci = []

tituly = ["Mgr.", "Ing.", "PaeDr."]
rimske = ["IV", "III", "II", "I"]
predmety = ["SJL", "ANJ", "MAT"]

with open("mena.txt", "r", encoding="utf-8") as f_mena:
    mena = [meno.strip() for meno in f_mena]

with open("priezviska.txt", "r", encoding="utf-8") as f_priez:
    priez = [priez.strip() for priez in f_priez]

for i in range(20):
    ucitelia.append(Ucitel(random.choice(mena), random.choice(priez), random.randrange(1970, 2000), random.choice(tituly), random.choice(predmety)))
    rok =random.randrange(2006, 2009)
    ziaci.append(Student(random.choice(mena), random.choice(priez), rok, f"{rimske[rok-2006]}.{chr(random.randrange(65,68))}"))

print()
print(*[student.vypis() for student in ziaci], sep="\n")
print()
print(*[ucitel.vypis() for ucitel in ucitelia], sep="\n")

#f"{rimske[random.randrange(3)]}.{chr(random.randrange(65, 68))}"
k=65
for i in range(4):
    for j in range(4):
        do{
            uc = random.randint(len(ucitelia))}
        while(not ucitelia[uc].trieda)
            ucitelia[uc].trieda = f"{rimske[j+1]}.{chr(k)}"
            k += 1
    k = 65



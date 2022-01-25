class Firma():
    def __init__(self,imie) :
        self.imie = imie
        self.praca = True
    
    def program(self):
        wybor = self.menuWybor()

        if wybor == 1:
            self.dodajPracownik()
        if wybor == 2:
            self.usunPracownik()
        if wybor == 3:
            wybor_miesięcny_roczne = input("Chcesz zobaczyć roczną kwotę?(tak/nie)")
            if wybor_miesięcny_roczne == "tak":
                self.pokazPensje(konta = "r")
            else:
                self.pokazPensje()
            
        if wybor == 4:
            self.zaplacPensje()

    def menuWybor(self):
        wybor = int(input("*** WITAMY *** \n\n1-Dodaj Pracownik\n2-Usun Pracownik\n3-Pokaz Pensje\n4-Zaplac Pensje\n\nWybierz Opcji :".format(self.imie)))  
        while wybor < 1 or wybor > 6:
            wybor = int(input("Porsze dokonać wyboru między 1 - 6 :"))
        return wybor 



    def dodajPracownik(self):
        id = 1
        imie = input("Wpisz nazywa pracownika:")
        nazwisko = input("Wpisz nazwisko pracownika:")
        wiek = input("Wpisz wiek pracownika:")
        gender = input("Wpisz gender pracownika:")
        pensje = input("Wpisz pensje pracownika:")

        with open ("pracowników.txt","r") as plik:
            listPracowników = plik.readlines()

        if len (listPracowników) == 0:
            id = 1
        else:
            with open("pracowników.txt","r") as plik:
               id =int(plik.readlines()[-1].split(")")[0]) + 1 

        with open ("pracowników.txt","a+") as plik:
            plik.write("{})-{}-{}-{}-{}-{}\n" .format(id,imie,nazwisko,wiek,gender,pensje))

     
   
   
    def usunPracownik(self):
        with open("pracowników.txt","r") as plik:
           pracowników = plik.readlines()

        pokazPracowników = []

        for osob in pracowników:
           pokazPracowników.append(" ".join(osob[:-1].split("-")))

        for osob in pokazPracowników:
            print(osob)

        wybor = int(input("Proszę wpisać numer pracownika, który chce pan usunąć(1-{}:)" .format(len(pokazPracowników))))
        while wybor < 1 or wybor > len(pokazPracowników):
            wybor = int(input("Proszę dokonać wyboru między (1-{}):" .format(len(pokazPracowników))))

        pracowników.pop(wybor - 1)

        numer = 1

        zmienPracowników = []

        for osob in pracowników:
            zmienPracowników.append(str(numer) + osob.split(")")[1])
            numer += 1 

        with open ("pracowników.txt","w") as plik:
            plik.writelines(zmienPracowników)


   
    def pokazPensje(self,konta = "m"):
        ### konto: jeśli napiś m = miesięczny, jeśli napiś t= tydzień ###
        with open ("pracowników.txt","r") as plik:
            pracowników = plik.readlines()  

            pensje = []
            
            for osob in pracowników:
                pensje.append(int(osob.split("-")[-1]))
            if konta == "r":
                print("Pensje, które musisz podać w tym roku : {} ".format(sum(pensje)*12))  
            else:
                print("Pensje, które musisz podać w tym miesiącu : {} ".format(sum(pensje)))

    def zaplacPensje(self):
        with open ("pracowników.txt","r") as plik:
            pracowników = plik.readlines()  

            pensje = []
            
            for osob in pracowników:
                pensje.append(int(osob.split("-")[-1]))
            
            całPensje = sum(pensje)

            ###Pobieranie pensji z budżet###

            with open ("budżet.txt","r") as plik:
                całBudżet = int(plik.readlines()[0])

            całBudżet = całBudżet - całPensje

            with open ("budżet.txt","w") as plik:
                plik.write(str(całBudżet))
            
           
                
firma = Firma("Managment IT")

while firma.praca:
    firma.program()
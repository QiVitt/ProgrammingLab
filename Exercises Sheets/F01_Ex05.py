

class Automobile:

    def __init__(self, casa_auto, modello, numero_posti, numero_portiere, kw, targa, categoria):
        self.casa_auto = casa_auto
        self.modello = modello
        self.numero_posti = numero_posti
        self.numero_portiere = numero_portiere
        self.kw = kw
        self.targa = targa
        self.categoria = categoria

    def __str__(self):
        print('Automobile: {} {} {} {} {} {} {}'.format(self.casa_auto, self.modello, self.numero_posti, self.numero_portiere, self.kw, self.targa, self.categoria))

    def parla(self):
        print('Broom Broom')

    def confronta(self, Automobile_due):
        x = isinstance(Automobile_due, Automobile)
        if(x != True):
            print('Impossibile eseguire il metodo')
            print('Il secondo oggetto non risulta essere istanza di Automobile')
            return None
        
        flag = 0
        if(self.casa_auto != Automobile_due.casa_auto):
            flag = 1
        if(self.modello != Automobile_due.modello):
            flag = 1
        if(self.numero_posti != Automobile_due.numero_posti):
            flag = 1
        if(self.numero_portiere != Automobile_due.numero_portiere):
            flag = 1
        if(self.kw != Automobile_due.kw):
            flag = 1
        if(self.categoria != Automobile_due.categoria):
            flag = 1

        if(flag == 0):
            print('Le due Automobili hanno le stesse caratteristiche')
        else:
            print('Le due Automobili hanno caratteristiche diverse')

    def bollo(self):
        computed_bollo = 0
        if(self.categoria == 'Euro0'):
            if(self.kw <= 100):
                computed_bollo = 3 * self.kw
            else:
                computed_bollo = 4.5 * self.kw
        elif(self.categoria == 'Euro1'):
            if(self.kw <= 100):
                computed_bollo = 2.5 * self.kw 
            else:
                computed_bollo = 4.35 * self.kw
        elif(self.categoria == 'Euro2'):
            computed_bollo = 3 * self.kw
        else:
            print('Valore bollo/kw inserito non valido')

        return computed_bollo

class Transformer(Automobile):
    def __init__(self, casa_auto, modello, numero_posti, numero_portiere, kw, targa, categoria, instance_name, generazione, grado, fazione, reparto):
        super().__init__(casa_auto, modello, numero_posti, numero_portiere, kw, targa, categoria)
        self.name = instance_name
        self.generazione = generazione
        self.grado = grado
        self.fazione = fazione
        self.reparto = reparto

    def parla(self):
        if(self.fazione == 'Autobots'):
            print('Noi siamo Autobots, proteggeremo ogni essere vivente')
        elif(self.fazione == 'Decepticons'):
            print("Noi siamo Decepticons e l'AllSpark sarà nostro!")
        else:
            print('Il valore inserito non corrisponde ad alcuna fazione esistente')

    def scheda_militare(self):
        print('Generazione - Grado - Fazione - Reparto')
        print('{} {} {} {}'.format(self.generazione, self.grado, self.fazione, self.reparto))

fobj = Automobile('AlfaRomeo', 'Mito', 5, 4, 250, 'AA000AA', 'Euro2')
sobj = Automobile('Lamborghini', 'Aventador', 4, 2, 450, 'AV010AV','Euro2')
tobj = Automobile('Lamborghini', 'Aventador', 4, 2, 450, 'AV010AV','Euro2')

fobj.__str__()
sobj.__str__()
tobj.__str__()

fobj.parla()
sobj.parla()
tobj.parla()

fobj.confronta(sobj)
sobj.confronta(tobj)

returned_bollo = fobj.bollo()
print(returned_bollo)
returned_bollo = sobj.bollo()
print(returned_bollo)
returned_bollo = tobj.bollo()
print(returned_bollo)

print(25 * '-')

xobj = Transformer('Porsche', 'Carrera', 4, 2, 350, 'AB012AB', 'Euro2', 'Bumblebee', 1, 'Capitano', 'Autobots', 'Supporto')

xobj.parla()
xobj.scheda_militare()


--------------------------------------------------

1. " L'oggetto auto_0 è di tipo Automobile "
2. " Automobile Superclasse - Transformer Sottoclasse "
3. " L'oggetto t_0 è di tipo Transformer "
4. " Sì, gli oggetti t_0 e t_1 sono dello stesso tipo "
5. " Sì, gli oggetti auto_0 e t_1 possono essere dello stesso tipo "
6. " Sì, t_1 potrebbe essere di tipo Automobile "
7. " No, auto_0 non potebbe essere di tipo Transformer "

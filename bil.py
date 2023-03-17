#Det här är en klass man kan skapa objekt av
class Bil:

    #constructor körs först när man skapar objekt av klasser
    def __init__(self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager
        
        
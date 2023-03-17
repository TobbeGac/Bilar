#Det här är en klass man kan skapa objekt av
class Bil:

    #constructor körs först när man skapar objekt av klasser
    def __init__(self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager

    def set_lager(self, lager):
        self.lager = lager
    
    def get_lager(self):
        return self.lager
    
    def get_fabrikat(self, fabrikat):
        self.fabrikat = fabrikat
    
    def get_color(self, color):
        self.color = color
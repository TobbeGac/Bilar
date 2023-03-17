import bil

looping = True #för att avsluta programmet
volvo_svart = bil.Bil("Volvo", "Svarta", 5)
volvo_vit = bil.Bil("Volvo", "Vit", 2)
ferrari_röd = bil.Bil("Ferrari", "röd", 4)

billista = [volvo_svart, volvo_vit, ferrari_röd]

while looping:
    print("-----------------------------------------")
    print("\n-:BilAutomat:-\n")

    i = 0
    #Skriver ut lista med bilar
    for bil in billista:
        print(str(i+1) + " : " + bil.fabrikat + " : " +bil.color+ ", anta i lager: " + str(bil.lager) + " st")

    #Avsluta programmet
    go = input("\n Vill du avsluta programmet? j/n ")

    if (go == "j"):
        break
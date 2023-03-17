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
        i += 1

    bil_nr = input("\nMata in siffran för vald bil: ")
    bil_nr_int = int(bil_nr)

    #print("bil nr= " + bil_nr)

    lager_int = billista[bil_nr_int-1].get_lager()


    if lager_int > 0:
        print("\n Här kommer en " + billista[bil_nr_int-1].color + " " + billista[bil_nr_int-1].fabrikat)

        #minskar lagret
        nytt_lagersaldo_int = lager_int - 1
        nytt_lagersaldo_string = str(nytt_lagersaldo_int)
        #Minskar bilobjektet lager
        billista[bil_nr_int-1].set_lager(nytt_lagersaldo_int)

        

    else:
        print ("\nSynd, du blir utan bil!\n")
    print("Lager saldo: " +str( billista[bil_nr_int-1].get_lager()))
    #Avsluta programmet
    go = input("\n Vill du avsluta programmet? j/n ")

    if (go == "j"):
        break
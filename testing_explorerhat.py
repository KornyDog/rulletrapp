import mysql.connector #Importerer modul for å koble til sql database som er skrevet i python
import time #Importerer time modulen som vi blant annet trenger for sleep()
from time import sleep
import explorerhat #Importerer modulen til hat-en vi bruker


while True: #Starter en løkke som kjører for alltid
    sensor = explorerhat.analog.one.read() #definerer at "sensor" skal bety at vi tar en read av analog input 1 på hat-en

    if sensor > 3.2: #Dersom sensoren gir en verdi HØYERE en 3.2 så kjøres følgende
        print("Object Detected") #Printer til konsol at vi har registrert bevegelse
        print("...")
        print(".....")
        explorerhat.motor.backward(70) #Setter på motoren til rulletrappen


        #|||SQL Integration|||
        mydb = mysql.connector.connect( #Definerer "mydb" som står for koblingen til databasen.
            host="192.168.2.2", #Africa
            user="root",
            password="Passord01",
            database="rulletrappdb"
        )

        mycursor = mydb.cursor() #en "cursor" gir oss muligheten til å kommunisere med en mysql database, og gir oss tilgang til funks
        sql = "INSERT INTO rulletrappdb.rulletrappbruk (hvilkenRulletrapp) VALUES (1)" #Sender in hvilken rulle trapp som aktiveres, som for øyeblikket bare er 1 av 1
        mycursor.execute(sql) #Vi bruker execute() som cursor gir oss tilgang til for å akseptere SQL query-en over og executer den

        mydb.commit() #commit er nødvendig for å konfirmere endringene vi prøver å gjøre i databasen

        print("record inserted.") #printer til konsol for å sjekke at koden fungerer så langt


        #vi setter i til 10 og minker den med 1 for hver gang vi printer i, som skjer hvert sekund
        for i in range(3, -1, -1):
            sleep(1)
            print(i)


        explorerhat.motor.forwards(0) #stopper motoren etter count down er ferdig
        sensor = 0
        sleep(2) #denne sleepen er for å gi litt pusterom for å kunne stoppe koden mens motoren er i en state "av"



    else: #Dersom sensoren gir en verdi MINDRE enn 3.2 så kjøres følgende

        print("Object Not Detected") #Printer til konsoll at ingenting plukkes opp
        explorerhat.motor.forwards(0) #Stopper motoren
        print("...")
        time.sleep(1)
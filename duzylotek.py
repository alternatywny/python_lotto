#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time

nowagra = "t"
while nowagra == "t":
    #powtarzaj dopuki uzytkownik wprowadzi poprawne dane
    while True:
        try:
            ileliczb = int(input("Ile liczb chcesz wytypowac?  "))
            maksymalna = int(input("Z ilu liczb chcesz typowac?  "))
            while ileliczb > maksymalna:
                print("Nie mozesz typowac wiecej liczb niz liczy zbior!")
                ileliczb = int(input("Ile liczb chcesz wytypowac?  "))
                maksymalna = int(input("Z ilu liczb chcesz typowac?  "))
            break
        except ValueError:
            print("bledne dane!")
    print("\n")
    print("Prosze wytypuj %s ze zbioru %s liczb. Masz 3 szanse!" % (ileliczb, maksymalna))

    wynik = []

    i = 0
    while i < ileliczb:
        liczba = random.randint(1, maksymalna)

        #sprawdza czy liczba znajduje się już w zbiorze
        if wynik.count(liczba) == 0:
            #print("//LOSOWANIE// Liczba nr %s to: %s" % (i+1, liczba))
            wynik.append(liczba)
            i = i+1

    #print("Wyniki losowania: %s" % (wynik))
    l = 0

    for y in range(3):
        print("\n Runda #%s " % (y+1))
        i = 0
        typy = set()
        while i < ileliczb:
            try:
                print("\n")
                typ = int(input("Podaj liczbe %s :  " %(i+1)) )
            except ValueError:
                print("Musisz podac liczbe!")
                continue
            if typ > maksymalna:
                print("Musisz podac cyfre z zakresu 1 - %s" % (maksymalna))
            elif typ not in typy:
                typy.add(typ)
                print("Twoja liczba nr %s to: %s " % (i+1, typ))
                i = i +1
            elif typ in typy:
                print("Nie mozesz podac dwoch takich samych liczb!")

        time.sleep(0.5)
        print("\nTwoje liczby to: %s" % (typy))

        while l < 1:
            time.sleep(0.5)
            print("\n \n ***** komora maszyny losującej jest pusta *****")
            time.sleep(0.5)
            print("\n ***** następuje zwolnienie blokady *****")
            time.sleep(1)
            print("\n ***** LOSOWANIE ***** \n")
            for i in range(ileliczb):
                print(" --- liczba nr %s ---" % (i+1))
                time.sleep(1)
            l = l + 1

        print("\n-----------------------------------------------------")
        trafienia = set(wynik) & typy
        #drukuje
        if len(trafienia) == ileliczb:
            time.sleep(0.5)
            print("Ilosc trafien: %s" % (len(trafienia)))
            time.sleep(0.5)
            print("Trafione liczby: %s\n" % (trafienia))
            print("BRAWO!!!! Udalo Ci sie zgadnac za %s razem!!!\n" % (y+1))
            print("Kim jestes? Jestes ZWYCIĘZCĄ!!\n")
            print("-----------------------------------------------------")
            break
        elif 2-y == 0:
            time.sleep(0.5)
            print("Ilosc trafien: %s" % (len(trafienia)))
            time.sleep(0.5)
            print("Trafione liczby: %s" % (trafienia))
            print("To byla Twoja ostatnia szansa. Moze uda Ci sie nastepnym razem.")
            print("-----------------------------------------------------")
        else:
            time.sleep(0.5)
            print("Ilosc trafien: %s" % (len(trafienia)))
            time.sleep(0.5)
            print("Trafione liczby: %s" % (trafienia))
            print("Probuj dalej! Masz jeszcze %s szanse :) " %(2-y))
            print("-----------------------------------------------------")
        time.sleep(1)
    nowagra = ""
    while nowagra not in("t", "n"):
        nowagra = (input("\n\nCzy chcesz zagrac od nowa? (t/n)\n\n")).lower()
        if nowagra not in("t", "n"):
            print("Proszę podac prawidłową odpowiedz! (t/n)")

print("Koniec gry. Nacisnij enter klawisz aby wyłaczyc.")
input()
# ----------------------------------------------------------------------
# C1. Python — rīks, kas atlasa un saglabā
# ----------------------------------------------------------------------

# Uzraksti skriptu, kuram līmeni padod kā argumentu komandrindā. Skripts izvada, cik tāda līmeņa rindu žurnālā ir, un saglabā visas šīs rindas failā, kura nosaukums sākas ar līmeņa nosaukumu. Ja arguments nav padots, skripts izvada pamācību un neavarē.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Mainīgo, kurā glabā līmeni, nosauc ar vārdu meklejamais.

import csv
meklejamais=input("Ievadi kļūdas līmeni: ")
skaits = {}
def func():
    with open("sistema.log", encoding="utf-8") as f:
                for rinda in f:
                    dalas = rinda.split()
                    if dalas[2] == meklejamais:
                        serviss = dalas[3].rstrip(":")
                        if serviss in skaits:
                            skaits[serviss] = skaits[serviss] + 1
                        else:
                            skaits[serviss] = 1
    with open(f"{meklejamais}.csv", 'w', encoding='UTF-8-sig', newline="") as f:
        csvwriter = csv.writer(f,delimiter=";")
        csvwriter.writerow(["Serviss","Kļūdas"])
        for Serviss, Kļūdas in skaits.items():
            csvwriter.writerow([Serviss, Kļūdas])

if meklejamais == "INFO":
    func()
elif meklejamais == "WARNING":
    func()
elif meklejamais == "ERROR":
    func()
elif meklejamais == "CRITICAL":
    func()
else:
    print("Ievadi pareizu kļūdas līmeni!")
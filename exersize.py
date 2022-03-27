r = 0
f = 0
while True:
 import csv
 with open('glossor2.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  print("välkommen till glosförhöret, programerat av Sami Jarrar i RWS skolan.")
  print("---------------------------------")
  dina_ord1 = []
  for row in data:


    print("Det svenska order är: ",row["svenska"])
    dina_ord1 = input("Skriv ordet på engelska: ")
    x = dina_ord1.lower()


    if row['engelska'].lower() == x: 
        print ("Rätt svar")
        print("")
        r = r + 1
        print("Rätt: ",r,"Fel: ",f)
    else:
        f = f + 1
        print("Rätt: ",r,"Fel: ",f)
        print ("Fel svar")
        print("Rätta svaret är: ", row["engelska"])
        print("")
    print("")
 check = input("Skriv GO för att köra igen, tryck på någon knapp om du vill avsluta programet: ")
 if check.upper() == "GO":   
    f = 0 
    r = 0
    continue
 print("Bye...") 
 break
 

 


    

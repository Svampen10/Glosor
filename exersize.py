while True:
 import csv
 with open('glossor2.csv', newline='') as csvfile:
  data = csv.DictReader(csvfile)
  print("Svenskaordet till Engelskaordet")
  print("---------------------------------")
  dina_ord1=[]
  for row in data:

 

 

    print("Det svenska order är: ")
    print(row['svenska'])    
    dina_ord1 = input("skriv nu ordet på engelska ")


    if row['engelska'] == dina_ord1: 
        print ("rätt")
        print("")
    else:
        print ("fel")
        print("rätta svaret är", row["engelska"])
        print("")
    print("")
 check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
 if check.upper() == "Y": 
    continue
 print("Bye...")
 break 

    

#zadadas znamky a da ti to priemer ked das 0 koncis

znamky=[]

while True:
    
    znamka = int(input("Zadaj znamku: "))
    if -1< znamka <6:
        if znamka == 0:
            break
        znamky.append(znamka)

print(f"{len(znamky)} s priemerom sum{(znamky)/len(znamky)}")



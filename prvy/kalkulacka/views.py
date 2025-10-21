from django.shortcuts import render

def index(request):
    if request.method == "GET":
        vysledok = 0
    if request.method == "POST":
        try :
            a = float(request.POST["a"])
            b = float(request.POST["b"])
            operator = request.POST["operator"]
        except ValueError:
            return render(request, 'kalkulacka/index.html', dict(vysledok="nespravny input"))

        
        if operator == "+":
            vysledok = a+b
        elif operator == "-":
            vysledok = a-b
        elif operator == "*":
            vysledok = a*b
        else:
            if(b==0):
                vysledok="nulou sa nedeli"
            else:
                vysledok = a/b
        


    return render(request, 'kalkulacka/index.html', dict(vysledok=vysledok))

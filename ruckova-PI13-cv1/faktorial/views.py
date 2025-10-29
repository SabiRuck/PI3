from django.shortcuts import render, HttpResponse

def index(request):
    if request.method == "GET":
        output=""
    if request.method == "POST":
        try:
 
            num = int(request.POST["num"])
            if(num<0):
                raise ValueError
        except ValueError:
            return render(request, "faktrial/index.html", {"output":"Wrong Input"})

        output = 1
        for i in range(1, num+1):
            output = output * i
        output = f"Faktorial cisla {num} je {output}, {len(request.POST)}"
    return render(request, "faktorial/index.html", {"output":output})
from django.shortcuts import render

def index(request):
    if request.method == "GET":
        output=""
    if request.method == "POST":
        try:
            num = int(request.POST["num"])
            if(num<0):
                raise ValueError
        except ValueError:
            return render(request, "prvocislo/index.html", {"output":"Wrong Input"})
        a = 0

        output="je"

        is_prime = True
        for i in range(2, num):
            if int(num) % i == 0 :
                output="nie je"

        output = f"Cislo {num} {output} prvocislo"

        

    return render(request, "prvocislo/index.html", {"output":output})

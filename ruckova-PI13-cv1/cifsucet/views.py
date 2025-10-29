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
            return render(request, "cifsucet/index.html", {"output":"Wrong Input"})
        idk = str(num)
        output=0
        for i in idk:
            output = output + int(i)
        output = f"Ciferny sucet cisla {num} je {output}"

        
    return render(request, "cifsucet/index.html", {"output":output})
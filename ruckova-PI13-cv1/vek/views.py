from django.shortcuts import render

def index(request):
    if request.method == "GET":
        output=""
        name = ""
    if request.method == "POST":
        try:
            name = str(request.POST["name"])
            date = str(request.POST["date"])
            date1 = int(date)

        except ValueError:
            return render(request, "vek/index.html", {"output":"Wrong Input"})


        months = ["januar", "februar", "marec", "april", "maj", "jun", "jul", "august", "september", "oktober", "november", "december"]

        day = int(date[:2])
        month = int(date[2:4])
        year = int(date[4:])

        output = f"Tvoj datum narodenia je {day}.{months[month-1]}.{year}"
        name = f"Ahoj {name}."
        
        
    return render(request, "vek/index.html", {"output":output, "name":name})


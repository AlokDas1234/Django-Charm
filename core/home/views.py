from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        text_input = request.POST.get("text_input")
        dropdown = request.POST.get("dropdown")

        # Debug: log the inputs
        print("Uploaded File:", uploaded_file)
        print("Text Input:", text_input)
        print("Dropdown Selection:", dropdown)

        return HttpResponse("Form submitted successfully!")

    return render(request, "home/index.html")

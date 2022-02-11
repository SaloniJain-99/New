from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request,"home.html")

def welcome(request):
    t = request.GET['text']
    n=int(t)
    sum=0
    while n>0:
        d=n%10
        sum=sum+d
        n=n//10
    return render(request,"welcome.html",{'sod':sum})
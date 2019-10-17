from django.shortcuts import render
from Evaluated import forms

# Create your views here.

class mainPage:
    def index(request):
        index_dict = {
            'head1':'Welcome to the calculator page using Django!',
            'eval_cal':'Proceed to evaluated calculator using the following link',
            'normal_cal':'Proceed to graphical calculator using the following link',
        }
        return render(request,'Calculator/index.html',context=index_dict)

class EvaluatedCalculator:
    def index(request):
        res = None
        form = forms.CalForm()
        cal_dict = {
            "about":"This calculator evaluates an expression and returns the result!",
            "instruction":"Just enter an expression in the input box to evaluate the result",
            "example":"For example enter 1+2",
            "form":form,
            "result":res,
        }
        if request.method == "POST":
            form = forms.CalForm(request.POST)
            if form.is_valid():
                res = eval(form.cleaned_data['expr'])
                cal_dict["result"] = res
        return render(request,"Evaluated/index.html",context=cal_dict)
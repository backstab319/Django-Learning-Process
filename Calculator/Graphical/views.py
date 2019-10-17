from django.shortcuts import render
from Graphical import forms
from Graphical.models import calGraphicData

# Create your views here.
class calGraphic:
    def index(request):
        if request.method == "POST":
            form = forms.calGraphic(request.POST)
            if form.is_valid():
                uval = form.cleaned_data['btn']
                obj = calGraphic()
                if uval == "=": obj.evaluate()
                if uval not in ["c","="]: res_data = obj.update(uval)
                elif uval == "=":
                    res_data = obj.evaluate()
                else:
                    res_data = ""
                    obj.clear()
                index_dict = {
                    "result": res_data,
                }
        else:
            index_dict = {
                "result":"Please enter some data",
            }
        index_dict.update({
            "head1":"Calculator made using Django",
        })
        return render( request, "Graphical/index.html",context=index_dict)

    def update(request,uval):
        fieldData = calGraphicData.objects.get(name="cal_data")
        fieldData.data += uval
        fieldData.save()
        return fieldData

    def evaluate(request):
        fieldData = calGraphicData.objects.get(name="cal_data")
        fieldData.data = result = eval(str(fieldData))
        fieldData.save()
        return result

    def clear(request):
        fieldData = calGraphicData.objects.get(name="cal_data")
        fieldData.data = ""
        fieldData.save()

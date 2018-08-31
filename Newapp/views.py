from django.shortcuts import render
from Newapp.models import Register
from django.http import HttpResponse,HttpResponseRedirect
from Newapp.forms import RegisterForm
from django.urls import reverse
import xlwt
# Create your views here.


def base(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,label_suffix='')
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('Newapp:thanksforregistering'))
    else:
        form = RegisterForm(label_suffix='')

    return render(request,'Newapp/base.html',{'form':form})

def thanks(request):
    return render(request,'Newapp/thanks.html')

def download(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="registered.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['NAME', 'EMAIL', 'ROLL NO','BRANCH']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Register.objects.all().values_list('Name', 'Email', 'Roll','Branch')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def extract(response):
    return render(response,'Newapp/download.html')
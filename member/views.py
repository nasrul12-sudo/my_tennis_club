from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from .forms import ExcelUploadForm

def member(request):
    return render(request, 'index.html')

def user(request):
    return render(request, "all_user.html")

def buku(request):
    return render(request, 'buku-kas.html')

def billing(request):
    return render(request, "e-billing.html")

def jurnal(request):
    return render(request, 'jurnal-umum.html')

def transaksi(request):
    return render(request, "tambah-transaksi.html")

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            fs = FileSystemStorage()
            filename = fs.save(excel_file.name, excel_file)
            file_url = fs.url(filename)
            print(file_url)
#             return render(request, 'upload_success.html', {'file_url': file_url})
#     else:
#         form = ExcelUploadForm()
#     return render(request, 'upload_excel.html', {'form': form})

# def upload_success(request):
#     return render(request, 'upload_success.html')


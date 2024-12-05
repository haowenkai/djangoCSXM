from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def house_management(request):
    return render(request, 'app/house_management.html')

def fee_management(request):
    return render(request, 'app/fee_management.html')

def report_management(request):
    return render(request, 'app/report_management.html')

def repair_management(request):
    return render(request, 'app/repair_management.html')

def announcement(request):
    return render(request, 'app/announcement.html')

def property_management(request):
    return render(request, 'app/property_management.html')

def permission_management(request):
    return render(request, 'app/permission_management.html')

from django.shortcuts import render, get_object_or_404
from .models import FacultyInfo, Department, Program, ExchangeProgram

def index(request):

    faculty_info = FacultyInfo.objects.first()
    return render(request, 'faculty/index.html', {'faculty_info': faculty_info})

def program_list(request):

    programs = Program.objects.select_related('department').all()
    return render(request, 'faculty/program_list.html', {'programs': programs})

def program_detail(request, pk):

    programs = get_object_or_404(Program.objects.select_related('department'), pk=pk)
    return render(request, 'faculty/program_detail.html', {'program': programs})

def department_list(request):

    departments = Department.objects.prefetch_related('programs').all()
    return render(request, 'faculty/department_list.html', {'departments': departments})

def department_detail(request, pk):

    department = get_object_or_404(Department, pk=pk)
    return render(request, 'faculty/department_detail.html', {'department': department})

def exchange_list(request):
    programs = ExchangeProgram.objects.all()
    return render(request, 'faculty/exchange_list.html', {'programs': programs})
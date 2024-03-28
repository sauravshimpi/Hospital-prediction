from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.verify import authentication, form_varification
from app.process import multidisease_detection, list_generate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .form import patient_form
from app.models import Patient_data, doctors_data
from datetime import datetime
import random
# Create your views here.
def index(request):
    # return HttpResponse("This is Home page")    
    return render(request, "index.html", {'action' : 'index'})

def log_in(request):
    if request.method == "POST":
        # return HttpResponse("This is Home page")  
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successful...!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid User...!")
            return redirect("log_in")
    # return HttpResponse("This is Home page")    
    return render(request, "log_in.html", {'action' : 'log_in'})

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        # print(fname, contact_no, ussername)
        verify = authentication(fname, lname, password, password1)
        if verify == "success":
            user = User.objects.create_user(username, password, password1)          #create_user
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Your Account has been Created.")
            return redirect("/")
            
        else:
            messages.error(request, verify)
            return redirect("register")
    # return HttpResponse("This is Home page")    
    return render(request, "register.html", {'action' : 'register'})

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def dashboard(request):
    context = {
        'fname': request.user.first_name,
        }
    
    return render(request, "dashboard.html", context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def non_mri(request): 
    doctor_data = doctors_data.objects.all()
    context = {
        'fname': request.user.first_name, 
        'form' : patient_form(),
        'doctor_data' : doctor_data
        }
    if request.method == "POST":
        form = patient_form(request.POST, request.FILES)
        if form.is_valid():
            patient_first_name = form.cleaned_data['first_name']
            patient_last_name = form.cleaned_data['last_name']
            patient_contact = form.cleaned_data['contact']
            patient_age = form.cleaned_data['age']
            patient_sym1 = form.cleaned_data['sym1']
            patient_sym2 = form.cleaned_data['sym2']
            patient_sym3 = form.cleaned_data['sym3']
            patient_sym4 = form.cleaned_data['sym4']
            patient_sym5 = form.cleaned_data['sym5']
            patient_sym6 = form.cleaned_data['sym6']
            patient_sym7 = form.cleaned_data['sym7']
            patient_sym8 = form.cleaned_data['sym8']
            patient_sym9 = form.cleaned_data['sym9']
            patient_sym10 = form.cleaned_data['sym10']
            verify_from = form_varification(patient_first_name,patient_last_name,patient_contact,patient_age)
            if verify_from == "Success":
                symptoms = [patient_sym1, patient_sym2, patient_sym3, patient_sym4, patient_sym5, patient_sym6, patient_sym7, patient_sym8, patient_sym9, patient_sym10]
                if all(elem == 'default' for elem in symptoms):
                    messages.error(request, "Please Insert atleast 3 Symptoms")
                    return redirect("non_mri")
                else:
                    sym_list = list_generate(symptoms)
                    pred = multidisease_detection(sym_list)
                    for doctor in doctor_data:
                        if doctor.disease == pred[0]:
                            doc = doctor.doctor_name
                            break
                        else:
                            doc = doctor.doctor_name
                    print(doc)
                    patient_data = Patient_data(patient_first_name = patient_first_name, patient_last_name = patient_last_name, patient_contact = patient_contact, patient_age = patient_age, patient_sym1 = patient_sym1, patient_sym2 = patient_sym2, patient_sym3 = patient_sym3, patient_sym4 = patient_sym4, patient_sym5 = patient_sym5, prediction = pred[0], doctor = doc)
                    patient_data.date = datetime.today()
                    patient_data.save()
                    messages.info(request, pred[0])
                    return redirect("result_non_mri")
            else:
                messages.error(request, verify_from)
                return redirect("non_mri")
        else:
            messages.error(request, "Invalid Form")
            return redirect("non_mri")
    return render(request, "non_mri.html", context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def result_non_mri(request):
    doctor_data = doctors_data.objects.all()
    patient_data = Patient_data.objects.last()
    context = {
        'fname': request.user.first_name, 
        'patient_data' : patient_data,
        'doctor_data' : doctor_data,
    }
    return render(request, "result_non_mri.html", context)

# @login_required(login_url="log_in")
# @cache_control(no_cache = True, must_revalidate = True, no_store = True)
# def mri(request):
#     doctor_data = doctors_data.objects.all()
#     context = {
#         'fname': request.user.first_name, 
#         'form' : mri_patient_form(),
#         'doctor_data' : doctor_data,
#         }
#     if request.method == "POST":
#         form = mri_patient_form(request.POST, request.FILES)
#         if form.is_valid():
#             patient_first_name = form.cleaned_data['first_name']
#             patient_last_name = form.cleaned_data['last_name']
#             patient_contact = form.cleaned_data['contact']
#             patient_age = form.cleaned_data['age']
#             patient_mri = form.cleaned_data['mri_image']
            
#             verify_from = form_varification(patient_first_name,patient_last_name,patient_contact,patient_age)
#             if verify_from == "Success":
#                 pred = mri_disease_detection(patient_mri)
#                 for doctor in doctor_data:
#                     if doctor.disease == pred:
#                         doc = doctor.doctor_name
#                         break
#                     else:
#                         doc = doctor.doctor_name
#                 patient_data = mri_patient_data(patient_first_name = patient_first_name, patient_last_name = patient_last_name, patient_contact = patient_contact, patient_age = patient_age, uploaded_mri =  patient_mri, prediction = pred, doctor = doc)
#                 patient_data.date = datetime.today()
#                 patient_data.save()
#                 messages.info(request, pred)
#                 return redirect("result_mri")
#             else:
#                 messages.error(request, verify_from)
#                 return redirect("mri")
#         else:
#             messages.error(request, "Invalid Form")
#             return redirect("mri")
#     return render(request, "mri.html", context)


# @login_required(login_url="log_in")
# @cache_control(no_cache = True, must_revalidate = True, no_store = True)
# def result_mri(request):
#     doctor_data = doctors_data.objects.all()
#     patient_data = mri_patient_data.objects.last()
#     context = {
#         'fname': request.user.first_name, 
#         'patient_data' : patient_data,
#         'doctor_data' : doctor_data,
#     }
#     return render(request, "result_mri.html", context)
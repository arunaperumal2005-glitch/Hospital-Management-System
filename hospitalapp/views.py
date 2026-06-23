from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Patient,Doctor,Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.

@login_required
def home(request):
    context = {
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'appointment_count': Appointment.objects.count(),
    }
    return render(request, 'home.html', context)


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    search = request.GET.get('search')
    if search:
        patients = patients.filter(
            Q(name__icontains=search)
        )
    return render(
        request,
        'patient_list.html',
        {'patients': patients}
    )



@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    search = request.GET.get('search')
    if search:
        doctors = doctors.filter(
            Q(name__icontains=search) |
            Q(specialization__icontains=search)
        )
    return render(
        request,
        'doctor_list.html',
        {'doctors': doctors}
    )



@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    search = request.GET.get('search')
    if search:
        appointments = appointments.filter(
            Q(patient__name__icontains=search) |
            Q(doctor__name__icontains=search)
        )
    return render(
        request,
        'appointment_list.html',
        {'appointments': appointments}
    )



def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'add_appointment.html', {'form': form})



def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'add_patient.html', {'form': form})


def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'delete_patient.html', {'patient': patient})




def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'add_doctor.html', {'form': form})



def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'delete_doctor.html', {'doctor': doctor})



def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'add_appointment.html', {'form': form})


def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'delete_appointment.html', {'appointment': appointment})
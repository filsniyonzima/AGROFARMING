from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stock, Farmer, Agronomist, SeedRequest
from .forms import StockForm, FarmerForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .forms import FarmerForm 
from .utils import is_farmer_authenticated, get_logged_farmer  # Import your utility functions
 

class AddFarmerView(View):
    def get(self, request):
        form = FarmerForm()
        return render(request, 'myapp/add_farmer.html', {'form': form})

    def post(self, request):
        form = FarmerForm(request.POST)
        if form.is_valid():
            new_farmer = form.save(commit=False)
            new_farmer.set_password(form.cleaned_data['password'])  # Hash the password
            new_farmer.save()
            messages.success(request, 'Farmer added successfully.')
            return redirect('admin_dashboard')
        return render(request, 'myapp/add_farmer.html', {'form': form})

class AdminDashboardView(View):
    def get(self, request):
        # Retrieve counts and stock data
        farmer_count = Farmer.objects.count()
        seed_count = Stock.objects.filter(seed__isnull=False).values('seed').distinct().count()
        fertilizer_count = Stock.objects.filter(fertilizer__isnull=False).values('fertilizer').distinct().count()
        stocks = Stock.objects.all()

        # Log the counts for debugging
        print(f"Farmer Count: {farmer_count}, Seed Count: {seed_count}, Fertilizer Count: {fertilizer_count}")

        return render(request, 'myapp/admin_dashboard.html', {
            'farmer_count': farmer_count,
            'seed_count': seed_count,
            'fertilizer_count': fertilizer_count,
            'stocks': stocks,
        })


        return redirect('agronomist_login')  # Redirect if not authenticated
class HelloView(View):
    def get(self, request):
        return render(request, 'myapp/hello.html')

class CodeView(View):
    def get(self, request):
        return render(request, 'myapp/code.html')

class IndexView(View):
    def get(self, request):
        return render(request, 'myapp/index.html')

class StockManagementView(LoginRequiredMixin, View):
    def get(self, request):
        form = StockForm()
        stocks = Stock.objects.all()
        return render(request, 'myapp/stock_management.html', {'form': form, 'stocks': stocks})

    def post(self, request):
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock added successfully.')
            return redirect('stock_management')
        stocks = Stock.objects.all()
        return render(request, 'myapp/stock_management.html', {'form': form, 'stocks': stocks})

class FarmerCreateView(View):
    def get(self, request):
        form = FarmerForm()
        return render(request, 'myapp/farmer_register.html', {'form': form})

    def post(self, request):
        form = FarmerForm(request.POST)
        if form.is_valid():
            new_farmer = form.save(commit=False)
            password = form.cleaned_data.get('password')
            new_farmer.set_password(password)  
            new_farmer.save()
            messages.success(request, 'Farmer registered successfully.')
            return redirect('agronomist_login')
        return render(request, 'myapp/farmer_register.html', {'form': form})

class FarmerLoginView(View):
    def get(self, request):
        return render(request, 'myapp/farmer_login.html')

    def post(self, request):
        contact = request.POST.get('contact_info')
        password = request.POST.get('password')
        farmer = authenticate(request, username=contact, password=password)

        if farmer is not None:
            login(request, farmer)
            return redirect('farmer_dashboard')
        else:
            messages.error(request, 'Invalid contact number or password.')
            return render(request, 'myapp/farmer_login.html')

class AgronomistLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'myapp/agronomist_login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            contact = form.cleaned_data['contact']
            password = form.cleaned_data['password']

            # Check for Farmer
            try:
                farmer = Farmer.objects.get(contact=contact)
                if farmer.check_password(password):
                    request.session['farmer_id'] = farmer.id  # Store farmer ID in session
                    return redirect('admin_dashboard')  # Redirect to farmer's dashboard
            except Farmer.DoesNotExist:
                pass  # Continue to check for Agronomist

            # Check for Agronomist
            user = authenticate(request, username=contact, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')

            messages.error(request, 'Invalid credentials. Please try again.')

        return render(request, 'myapp/agronomist_login.html', {'form': form})

class FarmerDashboardView(View):
    def get(self, request):
        if is_farmer_authenticated(request):
            farmer = get_logged_farmer(request)
            return render(request, 'myapp/farmer_dashboard.html', {'farmer': farmer})
        return redirect('agronomist_login')  # Redirect if not authenticated
def addrequests(request):
    success_message = None
    if request.method == 'POST':
        request_date = request.POST.get('request_date')
        description = request.POST.get('description')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        seed_request = SeedRequest(
            request_date=request_date,
            description=description,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
        )
        seed_request.save()
        success_message = "Seed request added successfully!"

    return render(request, 'myapp/addrequests.html', {'success_message': success_message})

def view_requests(request):
    seed_requests = SeedRequest.objects.all()
    return render(request, 'myapp/view_seed_requests.html', {'seed_requests': seed_requests})

def approve_request(request, id):
    seed_request = get_object_or_404(SeedRequest, id=id)
    seed_request.status = 'Approved'
    seed_request.save()
    return redirect('view_requests')

def reject_request(request, id):
    seed_request = get_object_or_404(SeedRequest, id=id)
    seed_request.status = 'Rejected'
    seed_request.save()
    return redirect('view_requests')

def add_feedback(request, id):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        seed_request = get_object_or_404(SeedRequest, id=id)
        seed_request.feedback = feedback
        seed_request.save()
        return redirect('view_requests')

def view_requestsforadmin(request):
    seed_requests = SeedRequest.objects.all()
    return render(request, 'myapp/view_seed_requests-admin.html', {'seed_requests': seed_requests})

def stock_management(request):
    stocks = Stock.objects.all()
    return render(request, 'myapp/stock_management.html', {'stocks': stocks})

def stock_update(request, id):
    stock = get_object_or_404(Stock, id=id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock updated successfully.')
            return redirect('stock_management')
    else:
        form = StockForm(instance=stock)
    return render(request, 'myapp/edit_stock.html', {'form': form})

def stock_delete(request, id):
    stock = get_object_or_404(Stock, id=id)
    if request.method == 'POST':
        stock.delete()
        messages.success(request, 'Stock deleted successfully.')
        return redirect('stock_management')
    return render(request, 'myapp/confirm_delete.html', {'stock': stock})

class StockListView(ListView):
    model = Stock
    template_name = 'myapp/your_template_name.html'  # Replace with your actual template name
    context_object_name = 'stocks'

class StockUpdateView(UpdateView):
    model = Stock
    template_name = 'myapp/edit_stock.html'  # Replace with your edit template
    fields = ['seed', 'fertilizer', 'seedquantity', 'fertilizerquantity', 'planting_season']
    success_url = reverse_lazy('stock_list')

class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'myapp/confirm_delete.html'  # Replace with your confirmation template
    success_url = reverse_lazy('stock_list') 
    
class FarmersDashboardView(View):
    def get(self, request):
        if is_farmer_authenticated(request):
            farmer = get_logged_farmer(request)
            # You may want to retrieve the same counts as in AdminDashboardView for this farmer
            farmer_count = Farmer.objects.count()
            seed_count = Stock.objects.filter(seed__isnull=False).values('seed').distinct().count()
            fertilizer_count = Stock.objects.filter(fertilizer__isnull=False).values('fertilizer').distinct().count()
            stocks = Stock.objects.all()

            return render(request, 'myapp/admin_dashboard.html', {
                'farmer': farmer,
                'farmer_count': farmer_count,
                'seed_count': seed_count,
                'fertilizer_count': fertilizer_count,
                'stocks': stocks,
            })
        return redirect('agronomist_login')  # Redirect if not authenticated

class FarmerManagementView(View):
    def get(self, request):
        farmers = Farmer.objects.all()
        return render(request, 'myapp/farmer_management.html', {'farmers': farmers})

class EditFarmerView(View):
    def get(self, request, id):
        farmer = get_object_or_404(Farmer, id=id)
        form = FarmerForm(instance=farmer)  # Use your FarmerForm
        return render(request, 'myapp/edit_farmer.html', {'form': form, 'farmer': farmer})

    def post(self, request, id):
        farmer = get_object_or_404(Farmer, id=id)
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmer_management')  # Redirect to the farmers list
        return render(request, 'myapp/edit_farmer.html', {'form': form, 'farmer': farmer})

class DeleteFarmerView(View):
    def post(self, request, id):
        farmer = get_object_or_404(Farmer, id=id)
        farmer.delete()
        return redirect('farmer_management')  # Redirect to the farmers list
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'myapp/aboutus.html')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, CustomPasswordChangeForm  # Import the new forms

@login_required
def settings_view(request):
    if request.method == 'POST':
        if 'profile-form' in request.POST:
            profile_form = ProfileUpdateForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('settings')
        elif 'password-form' in request.POST:
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, 'Password changed successfully.')
                return redirect('settings')

    profile_form = ProfileUpdateForm(instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'myapp/settings.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, AddAccountForm
from django.contrib.auth.views import login


def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return login(request)
    

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
            
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': user_form})
    
@login_required
def add_account(request):
    if request.method == 'POST':
        add_account_form = AddAccountForm(request.POST)
        if add_account_form.is_valid():
            # store the current user as the creator of the account
            new_account = add_account_form.save(commit=False)
            new_account.user = request.user
            new_account.save()
            return HttpResponseRedirect(reverse('dashboard'))
            
    else:
        add_account_form = AddAccountForm()
    return render(request, 'account/add_account.html', {'form': add_account_form})
    
    
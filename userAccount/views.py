from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, AddAccountForm, AddBalanceForm, AddTagForm
from django.contrib.auth.views import login
from .models import Account

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
    
@login_required
def add_balance(request):
    if request.method == 'POST':
        account_field = int(request.POST.get('account_field'))
        balance_to_add = int(request.POST.get('amount'))
        account_object = Account.objects.get(id=account_field)
        account_object.balance = account_object.balance + balance_to_add
        account_object.save()
        return HttpResponseRedirect(reverse('dashboard'))
            
    else:
        add_balance_form = AddBalanceForm(request.user)
    return render(request, 'account/add_balance.html', {'form': add_balance_form})
    
@login_required
def add_tag(request):
    if request.method == 'POST':
        tag_form = AddTagForm(request.POST)
        if tag_form.is_valid():
            # create a new tag and attach the current user to it.
            tag_object = tag_form.save(commit=False)
            tag_object.user = request.user
            tag_object.save()
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        tag_form = AddTagForm()
    return render(request, 'account/add_tag.html', {'form': tag_form, 'section': 'tag'})

        
    
    
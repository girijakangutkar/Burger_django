from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Category, OrderModel


class ThanksPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')
      
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class Menu(View):
  def get(self, request, *args, **kwargs):
    return render(request,'app/menu.html')
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
      success_url = reverse_lazy("order_confirmation")
      return render(request, 'app/order.html')#context)

class OrderConfirmation(View):
    def get(self, request, *args, **kwargs):
        """
        # get every item from each category
        patty = MenuItem.objects.filter(
            category__name__contains='Patty')
        cheese = MenuItem.objects.filter(category__name__contains='Cheese')
        tomatoes = MenuItem.objects.filter(category__name__contains='Tomatoes')
        drinks = MenuItem.objects.filter(category__name__contains='Dirnk')

        # pass into context
        context = {
            'patty': patty,
            'cheese': cheese,
            'tomatoes': tomatoes,
            'drinks': drinks,
        }
        # render the template
        return render(request, 'app/order.html', context)

    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }
      """
        return render(request, 'app/order_confirmation.html')
        
@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse_lazy('index'))

def SignUp(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'app/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse_lazy('thanks'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/login.html', {})
       
        
        

 
import json
from IPython import embed
from .models import Invoice
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.
class LoginPage(TemplateView):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if uname == '' or pwd == '':
            return HttpResponseBadRequest('Username or Password missing')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            elif user.is_staff:
                return redirect('/manager/')
            return redirect('/cashier/')
        return render(request, "login.html", {'status': 'Invalid Username or Password'})


class SignUpPage(TemplateView):

    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        repwd = request.POST.get('repassword')
        if pwd != repwd:
            return render(request, "signup.html", {'status': 'Passwords do not match'})
        if uname == '' or pwd == '':
            return HttpResponseBadRequest('Username or Password missing')
        user = User.objects.create_user(username=uname, password=pwd)
        user.save()
        return redirect('/login/')


class HomePage(TemplateView):

    def get(self, request):
        return render(request, "index.html")


class DashboardPage(TemplateView):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login/')
        if request.user.is_staff:
            return redirect('/dashboard/admin/')
        return redirect('/dashboard/user/')


class LogoutPage(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('/login/')


@method_decorator(csrf_exempt, name='dispatch')
class ManagerPage(TemplateView):

    def get(self, request):
        return render(request, 'manager.html')

    def post(self, request):
        invoices_list = []
        invoices = Invoice.objects.all()
        for inv in invoices:
            invoices_list.append({
                'invoice_no': inv.invoice_no,
                'item_code': inv.item_code,
                'item_name': inv.item_name,
                'quantity': inv.quantity,
                'date': inv.date.strftime('%d-%m-%Y %H:%M'),
                'unit_price': inv.unit_price,
                'cashier_id': inv.cashier_id.id,
                'country': inv.country,
            })
        return HttpResponse(json.dumps(invoices_list))


class CashierPage(TemplateView):

    def get(self, request):
        return render(request, 'user.html')

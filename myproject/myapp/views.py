from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.
from .forms import *

# ===================================================User Log In ===============================



class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('myapp:UserLoginView')
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = ULoginForm
    success_url = reverse_lazy('myapp:DashboardView')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data['password']
        usr = authenticate(username=username, password=password)

        if usr is not None:
            login(self.request, usr)

        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Invalid user login!'})
        return super().form_valid(form)

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('myapp:UserLoginView')


# ================================= end user log in ===========================================

def dashboard(request):
    return render(request, 'dashboard.html')

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

class data_entry(View):
    def get(self, request):
        gp = engineer_group.objects.get(team_member=request.user)
        archor = anchor_site.objects.filter(engineer=gp.team_name)
        context = {'archor':archor}
        return render(request, 'data_entry.html', context)
    
    def post(self, request):
        archorid = int(self.request.POST['archorid'])
        fuellter = float(self.request.POST['fuellter'])
        fuelcm = float(self.request.POST['fuelcm'])
        dgrh = float(self.request.POST['dgrh'])
        dgkwh = float(self.request.POST['dgkwh'])
        dgavgprday = float(self.request.POST['dgavgprday'])
        gridkwh = float(self.request.POST['gridkwh'])
        omlload = float(self.request.POST['omlload'])
        atomload = float(self.request.POST['atomload'])
        mptload = float(self.request.POST['mptload'])
        mytelload = float(self.request.POST['mytelload'])
        cabinetvol = float(self.request.POST['cabinetvol'])
        cmtbox = self.request.POST['cmtbox']
        sid = anchor_site.objects.get(id=archorid)
        
        report_data.objects.create(site=sid, 
                                   engineer=request.user,
                                   fuel_cm=fuelcm,
                                   fuel_liter=fuellter,
                                   dg_rh=dgrh,
                                   dg_kwh=dgkwh,
                                   dg_avg_rh_day=dgavgprday,
                                   grid_kwh=gridkwh,
                                   oml_load=omlload,
                                   atom_load=atomload,
                                   mpt_load=mptload,
                                   mytel_load=mytelload,
                                   cabinet_vol = cabinetvol,
                                   remark = cmtbox
                                   )

        return JsonResponse({'status':'success'})
    

class mer_report(View):
    def get(self, request):
        datas = report_data.objects.all()
        context = {}
        return render(request, 'mer_report.html', context)

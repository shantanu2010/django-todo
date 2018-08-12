from django.views import View
from todolist.models import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.forms import ModelForm
from django.forms.widgets import *
from django.urls.base import *
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


class CreditListView(LoginRequiredMixin,ListView):
    login_url = 'login/'
    model = Card
    context_object_name = "data_set"
    template_name = "cards.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreditListView,self).get_context_data(**kwargs)
        userpermissions = self.request.user.get_all_permissions()
        context.update({'title':'Cards List',"user_permission":userpermissions})
        return context


class AddCard(ModelForm):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=512)
    date = models.DateField()


    class Meta:
        model = Card
        exclude=['id']

        widgets = {
            'title': TextInput(attrs={'class' : 'form-control','placeholder':'Title','label':'Title'}),
            'content': TextInput(attrs={'class' : 'form-control','placeholder':'Content','label':'Content'}),
            'date': TextInput(attrs={'class' : 'form-control','placeholder':'Date','label':'Date'}),
        }


class AddCardView(LoginRequiredMixin,CreateView):
    login_url = 'login/'
    #permission_required = 'credit.add_card'
    #permission_denied_message = "Dont have required permisssions to create a new Card"
    model=Card
    form_class = AddCard
    template_name = "add_card.html"
    success_url = reverse_lazy('cards')


class UpdateCardView(LoginRequiredMixin,UpdateView):
    login_url = 'login/'

    model = Card
    form_class = AddCard
    template_name = "add_card.html"
    success_url = reverse_lazy('cards')


class DeleteCardView(LoginRequiredMixin,DeleteView):
    login_url = 'login/'

    model = Card
    template_name = "delete_card.html"
    success_url = reverse_lazy('cards')


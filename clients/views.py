import json

from django.views import View
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.generic import (ListView, CreateView,
    UpdateView)
from django.core.paginator import (Paginator, EmptyPage,
    PageNotAnInteger)

from .models import Client
from .forms import ClientsForm


class ClientsListView(View):
    """
        This view is used for retriving the data according to the search
        string given by the user and to list the gathered data. When search
        string is empty it will show all the data present in the database.
    """
    model = Client

    def get(self, request):
        page = request.GET.get('page', 1)
        if request.is_ajax():
            search_str = self.request.GET.get('search_val')
            object_list = self.model.objects.all()
            if search_str != '':
                object_list = object_list.filter(Q(name__icontains = search_str) |
                        Q(email__icontains = search_str)| Q(phone_number__icontains = search_str)
                        | Q(suburb__icontains = search_str))

            context = {'clients': object_list, 'search_value': search_str, 'title': False}
            html = render_to_string('clients/show_clients.html', context)
            data = json.dumps({'html': html})
            return HttpResponse(data, content_type='application/json')
        else:
            object_list = self.model.objects.all()
            paginator = Paginator(object_list, 10)
            try:
                clients = paginator.page(page)
            except PageNotAnInteger:
                clients = paginator.page(1)
            except EmptyPage:
                clients = paginator.page(paginator.num_pages)
            context = {'title': True, 'clients': clients}
            return render(request, 'clients/show_clients.html', context)


class NewClientView(CreateView):
    """
        This view create's a record for the client and saves it
        in the database.
    """
    model = Client
    form_class = ClientsForm
    success_url = reverse_lazy('clients')
    template_name = 'clients/add_clients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = 'add'
        return context


class ClientUpdateView(UpdateView):
    """
        This view is used to update/edit the data of particular
        client which is selected by user.
    """
    model = Client
    fields = ['name', 'street_name', 'suburb', 'postcode',
        'state', 'contact_name', 'email', 'phone_number']
    template_name = 'clients/add_clients.html'
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        client = form.save(commit=False)
        client.updated_at = timezone.now()
        client.save()
        return redirect('clients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = 'edit'
        return context

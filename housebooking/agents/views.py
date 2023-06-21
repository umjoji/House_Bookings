from django.shortcuts import render, redirect
# from .forms import AgentRegForm, AgentRegForm2
from.models import Agent
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.

class AgentCreate(LoginRequiredMixin, CreateView):
    model = Agent
    fields = ['identification',
              'id_number',
              'DOB',
              'licensing_organisation',
              'license_number',
              'upload_license',
              'highest_academic_qualification',
              'education_institution',
              'upload_degree',
    ]

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

class AgentUpdate(LoginRequiredMixin, UpdateView):
    model = Agent
    fields = ['identification',
              'id_number',
              'DOB',
              'licensing_organisation',
              'license_number',
              'upload_license',
              'highest_academic_qualification',
              'education_institution',
              'upload_degree',
    ]



def dashboard(request, pk):
    return render(request, "dashboard_agent.html")

# def agent_registration(request):
#     form = AgentRegForm()
#     if request.method == "POST":
#         form = AgentRegForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, "agent_reg.html", context)

# def agent_registration2(request, agent_id):
#     agent = AgentReg.objects.get(agent_id=agent_id)
#     if request.method == "POST":
#         form = AgentRegForm2(request.POST, request.FILES)
#         if form.is_valid():
#            agent_reg2 = form.save(commit=False)
#            agent_reg2.agent = agent
#            agent_reg2.save()
#            return redirect('success_page')
#     else:
#         form = AgentRegForm2()
#     context = {
#         'agent': agent,
#         'form': form
#     }
#     return render(request, "agent_reg2.html", context)

# # def document_list(request):
# #     documents = AgentReg2.objects.all()
# #     return render(request, "agent_doc_list.html", {'documents': documents})

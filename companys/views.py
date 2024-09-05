from django.shortcuts import render
from django.views import View

from companys.models import HR


class RegView(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        fio = request.POST.get('fio')
        org_name = request.POST.get('org-name')
        org_email = request.POST.get('org-email')
        org_type = request.POST.get('org-type')
        excursion = request.POST.get('excursion')
        practices = request.POST.get('practices')
        event = request.POST.get('event')
        if excursion == 'on':
            excursion = True
        else:
            excursion = False
        if practices == 'on':
            practices = True
        else:
            practices = False
        if event == 'on':
            event = True
        else:
            event = False

        HR.objects.create(
            fio=fio,
            org_name=org_name,
            org_email=org_email,
            org_type=org_type,
            excursion=excursion,
            practices=practices,
            event=event
        )
        return render(request, 'thank.html')

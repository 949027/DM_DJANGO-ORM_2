from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datacenter.models


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        duration = datacenter.models.get_duration(visit)
        format_duration = datacenter.models.format_duration(duration)
        non_closed_visit = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration,
            }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

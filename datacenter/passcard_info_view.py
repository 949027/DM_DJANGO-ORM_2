from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datacenter.models


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    for visit in Visit.objects.filter(passcard=passcard):
        duration = datacenter.models.get_duration(visit)
        format_duration = datacenter.models.format_duration(duration)
        suspicious_visit = duration > 3600
        passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': format_duration,
                'is_strange': suspicious_visit,
        }
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)









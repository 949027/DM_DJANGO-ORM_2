from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datacenter.models
import datetime


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)
    for visit in Visit.objects.filter(passcard=passcard):
        suspicious_visit = False
        if visit.leaved_at is None:
            duration = datetime.datetime.now() - visit.entered_at
        else:
            duration = visit.leaved_at - visit.entered_at
        format_duration = datacenter.models.format_duration(duration.total_seconds())
        if duration.total_seconds() > 3600:
            suspicious_visit = True
        passcard_visit = {
                'entered_at': visit.passcard,
                'duration': format_duration,
                'is_strange': suspicious_visit,
        }
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)









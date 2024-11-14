from django.shortcuts import render
from django.conf import settings

def demo_view(request):
    return render(request, 'coldfront_djp_plugin/demo.html', context={"value":
        settings.DJP_PLUGIN_VALUE})

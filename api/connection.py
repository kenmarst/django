#-*-coding:utf-8-*-

import json, requests
from collections import ChainMap
from django.http import HttpResponse, JsonResponse

result_success = {'Result':'Success'}
result_fail = {'Result':'Fail'}
fail_code999 = {'Code':'9999'}
fail_message = {'Message':'xxxxxxxxxxxxxxxx'}

def check(request):
    if request.method == 'POST':
        try:
            client_ip = request.META['REMOTE_ADDR']
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'IP'}
            if all(k in req for k in req_key) and all(req.values()):
                try:
                    from api.models import Devices
                    devices = Devices.objects.get(ip = client_ip)

                    if devices.state == 'Proposed':
                        res = dict({'Result':0})
                    elif devices.state == 'Approved':
                        res = dict({'Result':1})
                    elif devices.state == 'Setting':
                        res = dict({'Result':2})
                    elif devices.state == 'Getting':
                        res = dict({'Result':3})
                    else:
                        res = dict(ChainMap(result_fail, fail_code999, fail_message))
                except:
                    res = dict(ChainMap(result_fail, fail_code999, fail_message))
            else:
                res = dict(ChainMap(result_fail, fail_code999, fail_message))
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def get(request):
    if request.method == 'POST':
        try:
            client_ip = request.META['REMOTE_ADDR']
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'IP'}
            if all(k in req for k in req_key) and all(req.values()):
                try:
                    from api.models import Devices
                    devices = Devices.objects.get(ip = client_ip)

                    res = dict(ChainMap(result_success, {
                        'Welcome' : devices.welcome,
                        'AccessDenied' : devices.accessdenied,
                        'ScreenSaver' : devices.screensaver,
                        'NTP' : devices.ntp,
                        'Timezone' : devices.timezone,
                        'Audio' : devices.audio,
                        'BioScore' : devices.bioscore,
                        'Language' : devices.language
                    }))
                except:
                    res = dict(ChainMap(result_fail, fail_code999, fail_message))
            else:
                res = dict(ChainMap(result_fail, fail_code999, fail_message))
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def set(request):
    if request.method == 'POST':
        try:
            client_ip = request.META['REMOTE_ADDR']
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'Welcome', 'AccessDenied', 'ScreenSaver', 'NTP', 'Timezone', 'Audio', 'BioScore', 'Language'}
            if all(k in req for k in req_key) and all(req.values()):
                try:
                    from api.models import Devices
                    Devices.objects.filter(ip = client_ip).update(welcome = req['Welcome'])
                    Devices.objects.filter(ip = client_ip).update(accessdenied = req['AccessDenied'])
                    Devices.objects.filter(ip = client_ip).update(screensaver = req['ScreenSaver'])
                    Devices.objects.filter(ip = client_ip).update(ntp = req['NTP'])
                    Devices.objects.filter(ip = client_ip).update(timezone = req['Timezone'])
                    Devices.objects.filter(ip = client_ip).update(audio = req['Audio'])
                    Devices.objects.filter(ip = client_ip).update(bioscore = req['BioScore'])
                    Devices.objects.filter(ip = client_ip).update(language = req['Language'])

                    res = dict(result_success)
                except:
                    res = dict(ChainMap(result_fail, fail_code999, fail_message))
            else:
                res = dict(ChainMap(result_fail, fail_code999, fail_message))
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

#-*-coding:utf-8-*-

import json, requests
from collections import ChainMap
from django.http import HttpResponse, JsonResponse

result_success = {'Result':'Success'}
result_pass = {'Result':'Pass'}
result_fail = {'Result':'Fail'}
fail_code999 = {'Code':'9999'}
fail_message = {'Message':'xxxxxxxxxxxxxxxx'}

def face_verify(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'FRUserId'}
            if all(k in req for k in req_key) and all(req.values()):
                """
                enter code
                """
                res = dict(result_pass)
            else:
                res = dict(ChainMap(result_fail, fail_code999, fail_message))
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def face_identify(request):
    if request.method == 'POST':
        try:
            """response note
            enter code

            you can refer to the following method:
            if success, enter values to below variables:
            fruserid
            then use like below code to response:
            res = dict(ChainMap(result_pass, {'FRUserId':fruserid}))

            if error, use like below code to response:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))
            """
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def face_check(request):
    if request.method == 'POST':
        try:
            """
            enter code
            """
            res = dict(result_success)
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def rfid_verify(request):
    if request.method == 'POST':
        try:
            client_ip = request.META['REMOTE_ADDR']
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'RFIDCard'}
            if all(k in req for k in req_key) and all(req.values()):
                try:
                    from .models import Devices
                    ip_device = Devices.objects.get(ip = client_ip)
                    if ip_device.state == 'Proposed':
                        from .models import Frusers
                        fruser = Frusers.objects.get(rfidcard = req['RFIDCard'])
                        for member in fruser.frusergroupmember_set.filter(fruseroid=fruser.oid):
                            for device in member.groupoid.frusergroupdevices_set.filter(groupoid=member.groupoid):
                                if device.deviceoid == ip_device:
                                    return JsonResponse(dict(ChainMap(result_pass, {'FRUserId':fruser.fruserid})))
                        return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
                    else:
                        return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
                except:
                    return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
            else:
                return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
        except:
            return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
    else:
        return HttpResponse('method error')

def rfid_check(request):
    if request.method == 'POST':
        try:
            client_ip = request.META['REMOTE_ADDR']
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'RFIDCard'}
            if all(k in req for k in req_key) and all(req.values()):
                try:
                    from .models import Devices
                    if Devices.objects.get(ip = client_ip).state == 'Proposed':
                        from .models import Frusers
                        Frusers.objects.get(rfidcard = req['RFIDCard'])
                        return JsonResponse(dict(result_success))
                    else:
                        return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
                except:
                    return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
            else:
                return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
        except:
            return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
    else:
        return HttpResponse('method error')

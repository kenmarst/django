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
        from .models import Devices, Frusers, Fruserlogs
        class end_procedure:
            def __init__(self, response, fruseroid = None, deviceoid = None, logcontent = None):
                Fruserlogs.objects.create(fruseroid = fruseroid, deviceoid = deviceoid, logcontent = logcontent)
                self.ret = JsonResponse(response)

        try:
            client_ip = request.META['REMOTE_ADDR']
            ip_device = Devices.objects.get(ip = client_ip)

            if ip_device.state != 'Proposed':
                try:
                    res_upload = json.loads(
                        requests.post(
                            'http://localhost:8800/storage/upload',
                            files = {'image' : (
                                request.FILES['image'].name,
                                request.FILES['image'].file,
                                request.FILES['image'].content_type
                            )}
                        ).text
                    )

                    if res_upload['state'] == 1000:
                        res_face_detect = json.loads(
                            requests.post(
                                'http://localhost:8800/face/detection/detect',
                                data = {'img_id' : res_upload['img_id']}
                            ).text
                        )
                        face_id = res_face_detect['faces'][0]['face_id']

                        for group in json.loads(requests.post('http://localhost:8800/face/query/group_list').text)['groups']:
                            person_id = None
                            similarity = 50
                            res_group_identify = json.loads(
                                requests.post(
                                    'http://localhost:8800/face/group/identify',
                                    data = {'group_id' : group, 'face_id' : face_id}
                                ).text
                            )

                            if res_group_identify['state'] == 1000:
                                for person in res_group_identify['persons']:
                                    if person['similarity'] >= similarity:
                                        similarity = person['similarity']
                                        person_id = person['person_id']

                        if person_id != None:
                            try:
                                fruser = Frusers.objects.get(personid = person_id)

                                for member in fruser.frusergroupmember_set.filter(fruseroid=fruser.oid):
                                    for device in member.groupoid.frusergroupdevices_set.filter(groupoid=member.groupoid):
                                        if device.deviceoid == ip_device:
                                            return end_procedure(
                                                response = dict(ChainMap(result_pass, {'FRUserId':fruser.fruserid})),
                                                fruseroid = fruser,
                                                deviceoid = ip_device,
                                                logcontent = 'Face identify pass'
                                            ).ret
                                return end_procedure(
                                    response = dict(ChainMap(result_fail, fail_code999, fail_message)),
                                    deviceoid = ip_device,
                                    logcontent = 'Face identify pass'
                                ).ret
                            except:
                                return end_procedure(
                                    response = dict(ChainMap(result_fail, fail_code999, fail_message)),
                                    deviceoid = ip_device,
                                    logcontent = 'Face identify fail'
                                ).ret
                        else:
                            return end_procedure(
                                response = dict(ChainMap(result_fail, fail_code999, fail_message)),
                                deviceoid = ip_device,
                                logcontent = 'Face identify fail'
                            ).ret
                    else:
                        return end_procedure(
                            response = dict(ChainMap(result_fail, fail_code999, fail_message)),
                            deviceoid = ip_device,
                            logcontent = 'Face identify fail'
                        ).ret
                except:
                    return end_procedure(
                        response = dict(ChainMap(result_fail, fail_code999, fail_message)),
                        deviceoid = ip_device,
                        logcontent = 'Face identify fail'
                    ).ret
            else:
                return end_procedure(
                    response = dict(ChainMap(result_fail, fail_code999, fail_message)),
                    deviceoid = ip_device,
                    logcontent = 'Face identify fail'
                ).ret
        except:
            return JsonResponse(dict(ChainMap(result_fail, fail_code999, fail_message)))
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
                    if ip_device.state != 'Proposed':
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
                    if Devices.objects.get(ip = client_ip).state != 'Proposed':
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

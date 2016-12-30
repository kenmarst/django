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
            """response note
            enter code

            you can refer to the following method:
            if success, enter values to below variables:
            result
            then user like below code to response:
            res = {'Result' : result}

            if error, use like below code to response:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))
            """
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def get(request):
    if request.method == 'POST':
        try:
            """response note
            enter code

            you can refer to the following method:
            if success, enter values to below variables:
            welcome, accessdenied, screensaver, ntp, timezone, audio, bioscore, language
            then user like below code to response:
            res = dict(ChainMap(result_success, {
                'Welcome' : welcome,
                'AccessDenied' : accessdenied,
                'ScreenSaver' : screensaver,
                'NTP' : ntp,
                'Timezone' : timezone,
                'Audio' : audio,
                'BioScore' : bioscore,
                'Language' : language
            }))

            if error, use like below code to response:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))
            """
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

def set(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'Welcome', 'AccessDenied', 'ScreenSaver', 'NTP', 'Timezone', 'Audio', 'BioScore', 'Language'}
            if all(k in req for k in req_key) and all(req.values()):
                """
                enter code
                """
                res = dict(result_success)
            else:
                res = dict(ChainMap(result_fail, fail_code999, fail_message))
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

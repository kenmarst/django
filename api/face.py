#-*-coding:utf-8-*-

import json, requests
from collections import ChainMap
from django.http import HttpResponse, JsonResponse

result_success = {'Result':'Success'}
result_fail = {'Result':'Fail'}
fail_code999 = {'Code':'9999'}
fail_message = {'Message':'xxxxxxxxxxxxxxxx'}

def add(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'FRUserId'}
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

def delete(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'FRUserId'}
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

def list(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body.decode('utf-8'))
            req_key = {'FRUserId'}
            if all(k in req for k in req_key) and all(req.values()):
                """
                enter code
                """
            else:
                res = dict(ChainMap(result_fail, fail_code999, fail_message))
        except:
            res = dict(ChainMap(result_fail, fail_code999, fail_message))

        return JsonResponse(res)
    else:
        return HttpResponse('method error')

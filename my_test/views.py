from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_details(req):
    emp_data={
        'eid':101,
        'ename':'Bunny',
        'esal':1000,
        'dept':10
    }
    res='<h1>employe id : {}<br>employee name : {}<br>emplayee sal : {}<br> emplayee deptno: {} </h1>'.format(emp_data['eid'],emp_data['ename'],emp_data['esal'],emp_data['dept'],emp_data['eid'])
    return HttpResponse(res)
import json
def emp_details_json_format(req):
    emp_data={

        'eid':101,
        'ename':'sunny',
        'esal':1000,
        'dept':10
    }
    json_data=json.dumps(emp_data)
    print(type(json_data))
    return HttpResponse(json_data,content_type='application/json')

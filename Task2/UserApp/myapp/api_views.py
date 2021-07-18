from django.contrib.auth.models import User
from django.http import JsonResponse


def user_listview_api(request):
    if request.method == 'GET':
        data = [user.username for user in User.objects.all()]
        return JsonResponse({
            "status": 200,
            "data": data
        })

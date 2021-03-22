from .models import Accounts
from .serializers import AccountSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def AccountAPI(request):
    all_Acc = Accounts.objects.all()
    data = AccountSerializers(all_Acc, many=True).data
    return Response({'data': data})
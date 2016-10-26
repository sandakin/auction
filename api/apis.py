'''
Created on Aug 17, 2016

@author: ranjana wijerathne
'''


from rest_framework.views import APIView
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
#from rest_framework.authentication import BasicAuthentication

from django.http import JsonResponse

from database.models import HealthCard,HealthState,Participant,DefaultSetting
from api.serializers import HealthCardSerializer,HealthStateSerializer,ParticipantSerializer,DefaultSettingsSerializer

class AdminDefaultSettingsViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BasicAuthentication,)
    queryset = DefaultSetting.objects.all()
    serializer_class = DefaultSettingsSerializer
    permission_classes = (AllowAny,)

class HealthCardViewSet(viewsets.ModelViewSet):
    queryset = HealthCard.objects.all()
    serializer_class = HealthCardSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get']
    
class AdminHealthCardViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BasicAuthentication,)
    queryset = HealthCard.objects.all()
    serializer_class = HealthCardSerializer
    permission_classes = (AllowAny,)
    
    @detail_route(methods=['get'])
    def set_default(self,request,pk=None):
        HealthCard.objects.update(status='0')
        HealthCard.objects.filter(id=request.GET.get('card')).update(status='1')
        return self.retrieve(request); 
    
class HealthStateViewSet(viewsets.ModelViewSet):
    queryset = HealthState.objects.all()
    serializer_class = HealthStateSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get']
    
    def get_queryset(self):
        try:
            return HealthState.objects.filter(health_card_id=self.kwargs['param'])
        except Exception:
            return HealthState.objects.all()
        
class AdminHealthStateViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BasicAuthentication,)
    queryset = HealthState.objects.all()
    serializer_class = HealthStateSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        try:
            return HealthState.objects.filter(health_card_id=self.kwargs['param'])
        except Exception:
            return HealthState.objects.all()
        
class HealthCardStatesViewSet(viewsets.ModelViewSet):
    if not DefaultSetting.objects.all().exists():
        DefaultSetting.objects.create()
        
    data=DefaultSetting.objects.all().order_by('id').first()
    count = data.card_count
    
    queryset = HealthCard.objects.filter(status='0').order_by('?')[:count] 
    serializer_class = HealthCardSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get']
    
class DefaultHealthCardStatesViewSet(viewsets.ModelViewSet):
    queryset = HealthCard.objects.filter(status='1')
    serializer_class = HealthCardSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get']
    
class AdminHealthCardStatesViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)
    queryset = HealthCard.objects.filter(status='0').order_by('?')
    serializer_class = HealthCardSerializer
    
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
class AdminParticipantViewSet(viewsets.ModelViewSet):
    #authentication_classes = (BasicAuthentication,)
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (AllowAny,)
    
class Login(APIView):
    #authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)
    
    def get(self,request):  
        try:
            return JsonResponse({'detail': 'success'})
        
        except Exception:
            return JsonResponse({'detail': 'error'})  

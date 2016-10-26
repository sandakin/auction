'''
Created on Aug 17, 2016

@author: ranjana wijerathne
'''
from rest_framework import serializers
from database.models import HealthCard,HealthState,Participant,DefaultSetting

class DefaultSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('card_count',)
        model = DefaultSetting 

class HealthStateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('state_desc','health_card','id',)
        model = HealthState 

class HealthCardSerializer(serializers.ModelSerializer):
    states = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='state_desc'
     )
    
    class Meta:
        fields = ('name','video','status','id','states','default_bid')
        model = HealthCard    
        
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','zipocde','dob','sex','hypertension', 'insulin', 'noninsulin', 'asthma',
                   'epilepsy', 'anaemia', 'renal', 'cardiac', 'accident', 'mentalhealth', 'gastro',
                   'skin', 'cancer', 'other', 'mobility', 'personal', 'activities', 'pain', 'anxiety','health')
        model = Participant  
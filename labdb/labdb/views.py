from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from labdb.models import Vamk_R, Vamk_C, Vamk_R_Smd, VAMK_C_SMD, Vamk_74HCXX, Vamk_D, Vamk_Ana, Vamk_CPU, Vamk_IC, Vamk_CPU_SMD, Vamk_Con, Vamk_IC_SMD, Vamk_Misc, Vamk_Socket, Feed
from rest_framework import viewsets
from labdb.serializers import UserSerializer, GroupSerializer, Vamk_RSerializer, Vamk_CSerializer, Vamk_R_SmdSerializer, VAMK_C_SMDSerializer, Vamk_74HCXXSerializer, Vamk_DSerializer, Vamk_AnaSerializer, Vamk_CPUSerializer, Vamk_CPU_SMDSerializer, Vamk_ConSerializer, Vamk_ICSerializer, Vamk_IC_SMDSerializer, Vamk_MiscSerializer, FeedSerializer, Vamk_SocketSerializer

"""
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser """

class UserViewSet(viewsets.ModelViewSet):
		queryset = User.objects.all()
		serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
		queryset = Group.objects.all()
		serializer_class = GroupSerializer

class Vamk_RViewSet(viewsets.ModelViewSet):
	queryset = Vamk_R.objects.all()
	serializer_class = Vamk_RSerializer
	
class Vamk_CViewSet(viewsets.ModelViewSet):
	queryset = Vamk_C.objects.all()
	serializer_class = Vamk_CSerializer
	
class Vamk_R_SmdViewSet(viewsets.ModelViewSet):
	queryset = Vamk_R_Smd.objects.all()
	serializer_class = Vamk_R_SmdSerializer
	
class VAMK_C_SMDViewSet(viewsets.ModelViewSet):
	queryset = VAMK_C_SMD.objects.all()
	serializer_class = VAMK_C_SMDSerializer	
	
class Vamk_74HCXXViewSet(viewsets.ModelViewSet):
	queryset = Vamk_74HCXX.objects.all()
	serializer_class = Vamk_74HCXXSerializer	
	
class Vamk_DViewSet(viewsets.ModelViewSet):
	queryset = Vamk_D.objects.all()
	serializer_class = Vamk_DSerializer	

class Vamk_AnaViewSet(viewsets.ModelViewSet):
	queryset = Vamk_Ana.objects.all()
	serializer_class = Vamk_AnaSerializer	
	
class Vamk_CPUViewSet(viewsets.ModelViewSet):
	queryset = Vamk_CPU.objects.all()
	serializer_class = Vamk_CPUSerializer	
	
class Vamk_CPU_SMDViewSet(viewsets.ModelViewSet):
	queryset = Vamk_CPU_SMD.objects.all()
	serializer_class = Vamk_CPU_SMDSerializer	
	
class Vamk_ConViewSet(viewsets.ModelViewSet):
	queryset = Vamk_Con.objects.all()
	serializer_class = Vamk_ConSerializer
	
class Vamk_IC_SMDViewSet(viewsets.ModelViewSet):
	queryset = Vamk_IC_SMD.objects.all()
	serializer_class = Vamk_IC_SMDSerializer
	
class Vamk_ICViewSet(viewsets.ModelViewSet):
	queryset = Vamk_IC.objects.all()
	serializer_class = Vamk_ICSerializer	
	
class Vamk_MiscViewSet(viewsets.ModelViewSet):
	queryset = Vamk_Misc.objects.all()
	serializer_class = Vamk_MiscSerializer	

class FeedViewSet(viewsets.ModelViewSet):
	queryset = Feed.objects.all()
	serializer_class = FeedSerializer	
	
class Vamk_SocketViewSet(viewsets.ModelViewSet):
	queryset = Vamk_Socket.objects.all()
	serializer_class = Vamk_SocketSerializer	

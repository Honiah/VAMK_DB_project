from django.contrib.auth.models import User, Group
from labdb.models import Vamk_R, Vamk_C, Vamk_R_Smd, VAMK_C_SMD, Vamk_74HCXX, Vamk_D, Vamk_Ana, Vamk_CPU, Vamk_CPU_SMD, Vamk_Con, Vamk_IC, Vamk_IC_SMD, Vamk_Misc, Vamk_Socket, Feed
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class Vamk_RSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_R
	    fields = ('url', 'id', 'category','strenght', 'unit', 'manufacturer_part_number','storing_location','storing_location_ec19','ptypename','tolerance','description','order_number_elfa','order_number_farnell','amount','ordered','signature')

class Vamk_CSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_C
	    fields = ('url', 'id', 'category','strenght', 'unit', 'manufacturer_part_number','storing_location','storing_location_ec19','ptypename','tolerance','description','order_number_elfa','order_number_farnell','amount','ordered','signature')

class VAMK_C_SMDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = VAMK_C_SMD
	    fields = ('url', 'id', 'category','strenght', 'unit', 'manufacturer_part_number','storing_location','storing_location_ec19','ptypename','tolerance','description','order_number_elfa','order_number_farnell','amount','ordered','signature')			

class Vamk_R_SmdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_R_Smd
	    fields = ('url', 'id', 'category','strenght', 'unit', 'manufacturer_part_number','storing_location','storing_location_ec19','ptypename','tolerance','description','order_number_elfa','order_number_farnell','amount','ordered','signature')
	
class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Feed
	    fields = ('url', 'user','feed')


class Vamk_74HCXXSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_74HCXX
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','storing_location','storing_location_ec19','ptypename','description','order_number_elfa','order_number_farnell','amount','ordered','signature')
		
class Vamk_DSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_D
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','storing_location','storing_location_ec19','ptypename', 'voltage_rating', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')	
		
class Vamk_AnaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_Ana
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'storing_location','storing_location_ec19', 'decal', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')				
		
class Vamk_CPUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_CPU
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'storing_location','storing_location_ec19', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')				
		
class Vamk_CPU_SMDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_CPU_SMD
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'storing_location','storing_location_ec19', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')				
		
class Vamk_ConSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_Con
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'storing_location','storing_location_ec19', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')						
		
class Vamk_IC_SMDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_IC_SMD
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'storing_location','storing_location_ec19', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')
		
class Vamk_ICSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_IC
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'storing_location','storing_location_ec19', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')
		
class Vamk_MiscSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_Misc
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','parttype', 'value', 'storing_location','storing_location_ec19', 'description','order_number_elfa','order_number_farnell','amount','ordered','signature')

class Vamk_SocketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
	    model = Vamk_Socket
	    fields = ('url', 'id', 'category', 'manufacturer_part_number','socket', 'storing_location','storing_location_ec19','order_number_elfa', 'order_number_partco','order_number_farnell','amount','ordered','signature')

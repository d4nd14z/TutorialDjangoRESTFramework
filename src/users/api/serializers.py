from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']

    #Metodo para realizar la encripcion de la contrasena del usuario
    def create(self, validated_data): 
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None: 
            instance.set_password(password)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id','email','username','first_name','last_name']

#Se crea un nuevo serializador unicamente para actualizar UNICAMENTE first_name y last_name
#Si se utilizara otro serializador, se daria acceso a todos los demas datos.
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['first_name','last_name']
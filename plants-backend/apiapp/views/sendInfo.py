from apiapp.models import Plantation2Arduino
from apiapp.models import User2Plantation
from django.core.mail import send_mail
infoByEmail=True
infoBySms=True
def inform_user(idArduino):
    """
    get:
    Detail one plant.
    put:
    Update one plant.
    """
    plant_inst = Plantation2Arduino.objects.filter(id_arduino=idArduino)
    users=[]
    user2plantations={}
    for plantation in  plant_inst:
        user= User2Plantation.objects.filter(id_plantation=plantation.id_plantation)
        for u in user:
            user2plantations[u.id]=plantation.id_plantation.name
            users.append(u.id_user)

    for user in users:
        message_text ="Hello, "+user.username+ " you received this mail, because there has been an measurement parameter in plantation "+user2plantations[user.id]+ " which value has exceeded an allowed value"
        if(infoByEmail):
            send_mail('Measurement error', message_text, '226136@student.pwr.edu.pl', [user.email])
        #elif (infoBySms):



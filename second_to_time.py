seconds=int(input( "Please enter the seconds : "))
hour=seconds//3600
restminutes=seconds-(3600*hour)
minutes=restminutes//60
second=restminutes-(60*minutes)
print(hour,":",minutes,":",second)    

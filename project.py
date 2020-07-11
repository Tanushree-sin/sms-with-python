from twilio.rest import Client
account_sid = 'ACd6421a0ae2d57a49c494a1db496f30a4'
auth_token = '57938c0214df047bc094326c8fea987c'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18324626971',
    body='Hello guys...',
    to='+918778508042'
)

print(message.sid)
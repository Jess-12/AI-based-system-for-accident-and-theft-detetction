
def sms1():
    from twilio.rest import Client
    from gpsnew import get_location

    account_sid = "ACb562080d6bfe045131dd922fdbe123a9"
    auth_token = "34d4b11bafeee0e2611688427532bd9f"

    body =  "Unknown face detected at location " + get_location()

    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(to = "+917306512974", from_= "+16203496079", body = body )

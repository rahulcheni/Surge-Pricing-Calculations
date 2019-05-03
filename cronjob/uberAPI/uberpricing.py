

from uber_rides.session import Session
from uber_rides.client import UberRidesClient
#Add the token
session = Session(server_token='XXXXXXXXXXXXXXX')

#client = UberRidesClient(session)
#p=client.get_price_estimates(37.770,-122.411,37.791,-122.405)
#key=str(37.770)+"|"+str(-122.411)+"|"+str(37.791)+"|"+str(-122.405)
#print(key)
#print(str(p.json.get('prices')))

def getPriceEstimate(start_lat,start_long,end_lat,end_long):
	client = UberRidesClient(session)
	p=client.get_price_estimates(start_lat,start_long,end_lat,end_long)
	key=str(start_lat)+"|"+str(start_long)+"|"+str(end_lat)+"|"+str(end_long)
	print(str(p.json.get('prices')))
	print(key)
	return str(p.json.get('prices')).encode(),key.encode()

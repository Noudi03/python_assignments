'''H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε ποιος είναι ο τελευταίος γύρος και στην 
συνέχεια πάρτε τις τελευταίες 100 τιμές (πεδίο randomness) μέσα από το https://drand.cloudflare.com/public/{round}. Μετατρέψτε αυτές τις 
τιμές σε δυαδικό και εμφανίστε το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά και το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενες μονάδες
'''

from urllib.request import Request, urlopen
import json

#requesting the data from the api
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

#parsing the json string to a python dictionairy
data_saved = json.loads(data)
#fetching the latest round
latest_round = data_saved["round"]
#creating an empty list to store all the randomness numbers
list= []

for round in range(latest_round,latest_round-100,-1):
    #requesting the data from the api
    req = Request(f'https://drand.cloudflare.com/public/{round}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    #parsing the data
    data_saved = json.loads(data)
    randomness = data_saved["randomness"]
    #converting the randomness variable from string to hex int and then to binary
    randomness = bin(int(randomness,16))
    #adding the number to the list
    list.append(randomness)
    

def max_1(data):
    '''finds the max sequence of 1s from the list'''
    max_ones = max(map(len,data[0].split('0')))
    for i in range(1,100):
        if max(map(len,data[i].split('0')))  > max_ones:
            max_ones = max(map(len,data[i].split('0')))
    return(max_ones)


def max_0(data):
    '''finds the max sequence of 0s from the list'''
    max_zeros = max(map(len,data[0].split('1')))
    for i in range(1,100):
        if max(map(len,data[i].split('1')))  >  max_zeros:
            max_zeros = max(map(len,data[i].split('1')))
    return(max_zeros)

#printing the results 
print("the max sequence of 1s in the last 100 rounds is: ", max_1(list))
print("the max sequence of 0s in the last 100 rounds is: ", max_0(list))
        

 
'''H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς.
Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να πάρετε το τελευταίο randomness
το οποίο θα το χωρίσετε σε δυάδες δεκαεξαδικών χαρακτήρων, και κάθε μια θα την μετατρέψετε σε ακέραιο
και θα την κάνετε modulo 80. Κρατείστε αυτούς τους 32 αριθμούς μοναδική φορά το καθένα και υπολογίστε πόσοι
από αυτούς τους αριθμούς θα κληρωνόντουσαν στην τελευταία κλήρωση του ΚΙΝΟ
που θα βρείτε εδώ https://api.opap.gr/draws/v3.0/1100/last-result-and-active'''

from urllib.request import Request, urlopen
import json

#requesting the data from the api
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

#parsing the json string to a python dictionairy
data_saved = json.loads(data)
#saving the latest randomness number
latest_random = data_saved["randomness"]
#creating an empty list to store the random number in pairs of 2
split_random = []

#splitting the random number in pairs of two and adding them to the dictionairy
for pair in range(0, len(latest_random), 2):
    split_random.append(latest_random[pair:pair+2])

#converting every number in the list to decimal
#every number in the list will now be subsituted by 
#the result of the remainder of the division of the number with 80
for number in range(len(split_random)):
    split_random[number] = int(split_random[number], 16) % 80

#initializing an empty list to add all the unique values from the split_random list
list_no_dupes = []
#adding all the numbers that are not already in the list_no_dupes 
[list_no_dupes.append(number) for number in split_random if number not in list_no_dupes]

#requesting the data from opap api
req = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data = urlopen(req).read()

#parsing the data to a python dictionairy
saved_data = json.loads(data)
winning_numbers = saved_data["last"]["winningNumbers"]["list"]

#will check if each number in the list_no_dupes is in the winning numbers list
#if it is the counter will be incremented by 1 
winner_count=0
for i,number in enumerate(list_no_dupes):
    if number in winning_numbers:
        winner_count+=1
#printing the results
print(f"{winner_count} out of the numbers would at win the latest kino draw")

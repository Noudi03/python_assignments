'''Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο γράμματα
και τον κενό χαρακτήρα (space). Χωρίστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό
και ξεκινήστε να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20.
Βγάλτε τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις του ενός γράμματος,
12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ. Τα ζεύγη δεν χρειάζεται να είναι
από συνεχόμενες λέξεις.'''

file_name = input("Enter the name of the file: ")
saving = input("Do you want the statistics to be saved in a new txt file? (y/n): ")

#opening the file
with open(file_name, "r") as f:
    content = f.read()

#keeping only the letters and spaces from the content string
processed_data = ''.join(word for word in content if word.isalpha() or word.isspace())
#spliting the modified string to a list, seperated by spaces
processed_data = processed_data.split()

#replacing every word in the list with its' character length 
for i in range(len(processed_data)):
    processed_data[i] = len(processed_data[i])

#creating a dictionairy to store how many words of x letters there are.
#The keys will represent the length of the words and the values the total occurrences of the words with {key} length 
occurrences = {}
for i in range(1,max(processed_data)+1):
    occurrences[i] = processed_data.count(i)
   
#if the text file's max length word is less than 20 chars,
#the next lines will fill the dictionary with 0s, to prevent a KeyError later in the code
if i < 20:
    for j in range(i,20):
        occurrences[j]  = 0

#this part will look to "remove" pairs of words from the dictionairy keys 1-19, 2-18 etc

for i in range(1,10):
    if occurrences[i] > occurrences[20-i]:
        occurrences[i] -= occurrences[20-i]
        occurrences[20-i] = 0
    else:
        occurrences[20-i]-=occurrences[i]
        occurrences[i] = 0

#The number of pairs of 20 forming between 10 character words is number_of_words DIV 2. 
#The remaining words will be either 0 if the number is even or 0, or 1 if the number is odd
occurrences[10] %= 2



#will show the user all the words left with i characters, if the number of words left is not zero
if saving == "y":
    #getting the name of the given file without the extension
    new_file = file_name.rsplit('.', 1)[0]
    #creating the new file
    with open(f"{new_file}_statistics.txt", "w") as f:
        for i in range(1,max(processed_data)+1):
            if occurrences[i] != 0:
                #printing the results to the terminal
                print(f"there are {occurrences[i]} words with {i} letters left")
                #writing the results to the file
                f.write(f"there are {occurrences[i]} words with {i} letters left\n")
else:
    for i in range(1,max(processed_data)+1):
        if occurrences[i] != 0:
            #printing the results to the terminal
            print(f"there are {occurrences[i]} words with {i} letters left")

                
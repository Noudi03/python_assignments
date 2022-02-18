'''Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες.
Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο πεζά γράμματα (μετατρέπετε τα κεφαλαία σε πεζά)
και τον κενό χαρακτήρα (space). Αρχικά, χωρίστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό.
Στις λέξεις που έχετε υπολογίστε τα ακόλουθα στατιστικά: 
α) ποιες είναι οι δέκα δημοφιλέστερες λέξεις;
Αν κάποιες εμφανίζονται το ίδιο πλήθος και βγαίνουν παραπάνω από δέκα, κρατείστε όποιες νομίζετε εσείς ή στην τύχη.
β) Ποιοι είναι οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις;
γ) Επαναλάβετε το ίδιο για τρία γράμματα.'''

from collections import Counter

file_name = input("Enter the name of the file: ")
saving = input("Do you want the statistics to be saved in a new txt file? (y/n): ")

#opening the file
with open(file_name, "r") as f:
    content = f.read()

#keeping only the letters and spaces from the content string
processed_data = ''.join(word for word in content if word.isalpha() or word.isspace())

#turning every word to lowercase
processed_data = processed_data.lower()

#spliting the modified string to a list, seperated by spaces
processed_data = processed_data.split()

#creating a new instance of the Counter
c1 = Counter(processed_data)

#finding the 10 most common words
most_common_1 = c1.most_common(10)

#find the 3 most common combinations of the first 2 letters
#creating an empty list to store the first 2 letters of each word
two_letters = []
#adding the first two letter of each word in processed_data list to the two_letter list
[two_letters.append(word[:2]) for word in processed_data]


#creating an instance of the Counter for the two_letter list
c2 = Counter(two_letters)
#finding the most 3 most common combinations of the first 2 letters
most_common_2 = c2.most_common(3)

#find the 3 most common combinations of the first 3 letters
#creating an empty list to store the first 3 letters of each word
three_letters =[]
#adding the first two letter of each word in processed_data list to the three_letter list
[three_letters.append(word[:3]) for word in processed_data]
#creating an instance of the Counter for the three_letter list
c3 = Counter(three_letters)
#finding the most 3 most common combinations of the first 3 letters
most_common_3 = c3.most_common(3)

#if the user answered y, will save the results in a file
if saving == "y":
    #getting the name of the given file without the extension
    new_file = file_name.rsplit('.', 1)[0]
    #creating the new file
    with open(f"{new_file}_statistics.txt", "w") as f:
        f.write(f"The 10 most common words are: {most_common_1}\n")
        f.write(f"The 3 most common combinations of the first 2 letters of the words are: {most_common_2}\n")
        f.write((f"The 3 most common combinations of the first 3 letters of the words are: {most_common_3}"))

#printing the statistics
print(f"The 10 most common words are: {most_common_1}")
print(f"The 3 most common combinations of the first 2 letters of the words are: {most_common_2}")
print(f"The 3 most common combinations of the first 3 letters of the words are: {most_common_3}")
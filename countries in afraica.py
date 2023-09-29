countries = #["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome &Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe" ]
print ("---Countries Of Africa---")
score = 0
lives = 3

while len(countries) > 0:
    if lives == 0:
        break
    print ("number of countries to guess: ")
    print (len(countries))
    print ("lives:")
    print (lives)
    print ("score")
    print (score)
    country = input("enter the anme of  country")
    if country in countries:
        print ("good guess")
        score = score + 1
        countries.remove(country)
    else:
        print ("incoorect guess")
        lives = lives -1
        
if lives == 0:
    print ("game over")
if len(countries) == 0:
    print ("end game")
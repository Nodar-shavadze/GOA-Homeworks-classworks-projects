def remove_vowels(lastname):
    lastname = lastname.lower()  
    for vowel in "aeiou":
        lastname = lastname.replace(vowel, "")
    return lastname

#ლისტი და ტაფლი განსხვავდება იმით რომ ტაფლში შეუძლებელია რომ მონაცემი შეცვალო, და ლისტში შესაძლებელია, ასევე ისინი ფრჩხილებითაც განსხვავდებიან. ესაა მხოლოდ განსხვავება
def usdcny(usd):
    cny = usd * 6.75
    return f"{cny} Chinese Yuan"

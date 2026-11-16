def app(): 
  name = input (" What's your name?")
  country= input ("What's your country name? ")
  age=input ("What's your ag age? ")
  religion=input ("Are you a Muslim? ")
  if religion== "Yes":
   print (" Assalamualaikum ", name, country, age)
  else:
   print ("Hello ", name, country, age) 
  account=input ("Do you have an account? ")
  if account == "Yes":
   print ("Login ")
  else:
   print ("Create an account ")
  password=input ("Enter your password?")
  if password=="1234":
   print ("You have successfully logged in ")
  else:
   print ("Incorrect password")
app()

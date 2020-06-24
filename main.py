def palindrome():
  word=input('Check to see if word is a palindrome: ')
  #Grabbing the word from the user


  reverse = ''.join(reversed(word))
  #Joining the input withouth any seperators and reversing the list of letters and saving it as a variable


  if(word == reverse):
    #Checking if the two match
    print('this is a palindrome')
  else:
    print('Sorry not a palindrome')



palindrome()
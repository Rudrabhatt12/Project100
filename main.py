'''
	Problem Set Unit 2 
	Author: Rudra Bhatt
	Date Created: Semptember 16, 2021
	Date Last Modified: Semptember 21, 2021
'''
#this is where yu input the amount and Userinput for it to make the Userinput plural or singular
items = input("enter the amount: ")
Userinput = input("enter the Userinput: ")

if items.isdigit() == True and Userinput.isalpha() == True:

    #checking if items is a number
    if items.isdigit():
        items = int(items)

        #this is to check if it is singular or not
        if items == 1:
            print(f"{items} {Userinput}")

        #this checks if it is plural or not
        if items > 1 or items == 0:

            #this is for all of the Userinput endings with vowel

            if Userinput.endswith('uy') or Userinput.endswith(
                    'iy') or Userinput.endswith('ey') or Userinput.endswith(
                        'oy') or Userinput.endswith('ay'):
                print(f"{items} {Userinput}s")

                #this are all of the irregular nouns
            elif Userinput.endswith('man'):
                print(f"{items} men")
            if Userinput.endswith("child"):
                print(f"{items} children")
            elif Userinput.endswith("foot"):
                print(f"{items} feet")
            if Userinput.endswith("tooth"):
                print(f"{items} teeth")
            elif Userinput.endswith("mouse"):
                print(f"{items} mice")
            if Userinput.endswith("person"):
                print(f"{items} people")
            elif Userinput.endswith('quiz'):
                print(f"{items} quizzes")

                # these are the expections which have a different rules then the other
            elif Userinput.endswith('roof') or Userinput.endswith(
                    'cliff') or Userinput.endswith(
                        'photo') or Userinput.endswith('piano'):
                print(f"{items} {Userinput}s")

            #these are the ones that have no change
            if Userinput.endswith('sheep') or Userinput.endswith(
                    'deer') or Userinput.endswith(
                        'fish') or Userinput.endswith(
                            'series') or Userinput.endswith('species'):
                print(f"{items} {Userinput}")
            elif Userinput.endswith('ao') or Userinput.endswith(
                    'eo') or Userinput.endswith('io') or Userinput.endswith(
                        'oo'):
                print(f"{items} {Userinput}s")
            if Userinput.endswith('o'):
                print(f"{items} {Userinput}es")
            elif Userinput.endswith('y'):
                print(f"{items} {Userinput[ :-1]}ies")
            if Userinput.endswith('s') or Userinput.endswith(
                    'ch') or Userinput.endswith('sh') or Userinput.endswith(
                        'x') or Userinput.endswith('z'):
                print(f"{items} {Userinput}es")
            elif Userinput.endswith('f'):
                print(f"{items} {Userinput[ :-1]}ves")
            if Userinput.endswith('fe'):
                print(f"{items} {Userinput[ :-2]}ves")

            else:
                print(f"{items} {Userinput}s")

#if you type random stuff for the input of amount and Userinput then it will say invalid input rather than crashing.
else:
    print('invalid input try again')

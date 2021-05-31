i=1
while i <= 20:
    print(i)
    i+=1

print("done with given condition")

secret_word = "lion"
guess = ""
while guess != secret_word :
    guess = input("enter guess:")

print("you are win!")

print("by giving guesss limit")

secret_word = "lion"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
   if guess_count < guess_limit :
       guess = input("enter guess:")
       guess_count+=1
   else:
       out_of_guesses = True

if out_of_guesses:
    print("out of guesses,YOU LOSE!")
else:
    print("you are win!")

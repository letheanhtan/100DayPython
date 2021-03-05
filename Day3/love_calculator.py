# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests

merge_name = (name1 + name2).lower()

t_letter_count = merge_name.count('t')
r_letter_count = merge_name.count('r')
u_letter_count = merge_name.count('u')
e_letter_count = merge_name.count('e')

total_score = str(t_letter_count + r_letter_count + u_letter_count + e_letter_count)

l_letter_count = merge_name.count('l')
o_letter_count = merge_name.count('o')
v_letter_count = merge_name.count('v')
e_letter_count = merge_name.count('e')

total_score += str(l_letter_count + o_letter_count + v_letter_count + e_letter_count)

total_score = int(total_score)

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 <= total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

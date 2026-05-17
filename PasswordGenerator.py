import random
import string

desired_password_length_value = int(input("Enter desired password length: "))

lowercase_character_pool = string.ascii_lowercase
uppercase_character_pool = string.ascii_uppercase
digit_character_pool = string.digits
special_character_pool = string.punctuation

complete_character_pool = (
    lowercase_character_pool +
    uppercase_character_pool +
    digit_character_pool +
    special_character_pool
)

generated_password_output = ""

for character_index_counter in range(desired_password_length_value):
    random_character_choice = random.choice(complete_character_pool)
    generated_password_output += random_character_choice

print("Generated Password:", generated_password_output)
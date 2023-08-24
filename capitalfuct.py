def captial_initials(name):
    words = name.split()
    capitalized_words=[word.capitalize()for word in words]
    capitalized_name =" ".join(capitalized_words)
    return capitalized_name
name_input="aksa albin"
capitalized_name=captial_initials(name_input)
print(capitalized_name)
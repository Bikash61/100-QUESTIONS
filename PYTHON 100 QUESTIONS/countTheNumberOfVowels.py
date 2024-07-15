def vowels(vow):
    vowe = 'aeiouAEIOU'
    return sum(1 for char in vow if char in vowe)
print(vowels('Manerosre'))
    
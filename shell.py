import kiss

while True:
    text = input('kiss > ')
    result, error = kiss.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
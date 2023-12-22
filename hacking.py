message='werhlceverm'
message=message.upper()
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(letters)):
    translated=''
    for symbol in message:
        if symbol in letters:
            num=letters.find(symbol)
            num=num-key
            if num < 0:
                num+=len(letters)
            translated=translated+letters[num]
        else:
            translated=tanslated+letters[num]
    print('Key #%s: %s' % (key,translated))
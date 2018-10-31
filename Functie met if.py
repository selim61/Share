def lang_genoeg():
    lengte = input('Hoe lang ben je: ')
    if int(lengte) >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')
lang_genoeg()
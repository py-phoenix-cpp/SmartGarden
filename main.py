http = 404
match http:
    case 200:
        print("200")
    case 300:
        print('300')
    case _:
        print('default')


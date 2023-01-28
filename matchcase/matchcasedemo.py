x = 5

# better that using lots of elif's

match x:
    case 1 | 4:
        print("one or four")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("default case")


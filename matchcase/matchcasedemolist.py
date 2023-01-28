list1 = ['python', 'java', 'javascript', 'react']

# must match entire collection not just section of it

match list1:
    case ['python', 'java']:
        print("python and java")
    case ['java', 'javascript']:
        print("java and javascript")
    case ['javascript', 'react']:
        print("javascript and react")
    case ['python', 'java', 'javascript', 'react']:
        print("all courses selected")
    case _:
        print("no course selected")


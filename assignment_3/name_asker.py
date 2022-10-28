
def ask_names():
    print("What's your first name?")
    fname = input()
    print("What is your last name?")
    lname = input()
    return (fname, lname)

if __name__ == "__main__":
    print('running name_asker as file')
else:
    print('running name_asker as import')

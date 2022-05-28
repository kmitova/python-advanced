class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


extensions = ['.com', '.bg', '.org', '.net']
email = input()

while not email == "End":
    if "@" not in email:
        raise MustContainAtSymbolError('Email must contain @')
    at_ind = 0
    for ind in range(len(email)):
        if email[ind] == "@":
            at_ind = ind
            break
    if len(email[:at_ind]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    is_invalid = True
    for ext in extensions:
        if email.endswith(ext):
            print(ext)
            is_invalid = False
            break

    if is_invalid:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print("Email is valid")
    email = input()

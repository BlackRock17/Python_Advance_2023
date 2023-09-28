import re

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class InvalidEmailProviderError(Exception):
    pass

VALID_DOMAIN = [".com", ".bg", ".net", ".org"]

regex_name = r"^[\w\.]+(?=@)"
regex_domain = r"\.[a-z]+$"
regex_provider = r"(?<=@)[a-z\-]+(?=.{1}[a-z]+$)"

while True:
    email = input()

    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(re.findall(regex_name, email)[0]) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if re.findall(regex_domain, email)[0] not in VALID_DOMAIN:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")

    if not re.findall(regex_provider, email):
        raise InvalidEmailProviderError("Invalid provider")

    print("Email is valid")




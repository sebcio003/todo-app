password = input("Enter new passowrd: ")

result = {"hasLength": False, "hasDigit": False, "hasUpper": False}

if len(password) >= 8:
    result["hasLength"] = True

for i in password:
    if i.isdigit():
        result["hasDigit"] = True
        break

for i in password:
    if i.isupper():
        result["hasUpper"] = True
        break

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
import re


def name_in_discord():
    name = input()
    result = re.findall(r'[\w_]+\s?[\w_]+\s?95350[123456]$', name)
    try:
        print(name == result[0])
    except:
        print("Your name doesn't fit")


if __name__ == "__main__":
    name_in_discord()
    
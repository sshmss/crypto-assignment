def main():
    card_no = input("Type in a credit card number\n")
    if len(card_no) != 16 or not card_no.isdigit():
        print("Invalid characters or length does not match 16")
        return
    print("Card number is valid")
main()
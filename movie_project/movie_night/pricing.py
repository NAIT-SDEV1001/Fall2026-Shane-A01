def get_ticket_price(age):

    if age <= 12:
        return 8.00
    elif age <= 64:
        return 12.00
    else:
        return 9.00

def calculate_total(quantity, ticket_price):
    
    return quantity * ticket_price
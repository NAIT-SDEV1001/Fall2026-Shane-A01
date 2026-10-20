# args must be before kwargs

def order_summary(*items, **options):
    print("Items ordered: ")
    #loop through items
    for item in items:
        print(f"- {item}")

    print("Options: ")
    #loop through options
    for key, value in options.items():
        print(f"{key}: {value}")

order_summary("burger","fries",takeout = True, bag = True)




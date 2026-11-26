from datetime import datetime
from pathlib import Path
import csv
DATE_FORMAT = "%d/%m/%y"
FIELD_NAMES = ["order_id","customer_name","item","quantity","pickup_date","collected","order_type","gift_message"]
CSV_PATH = Path(__file__).parent / "bake_sale_orders.csv"


class BakeSaleOrder:
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool)->None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity
        self.pickup_date = pickup_date
        self.collected = collected

# Give BakeSaleOrder a __str__() method that displays a line like this.
# B101 | Sam Lee | 6 x Chocolate chip cookies | 21/11/26 | Awaiting pickup
    def __str__(self)->str:
        return f"{self.order_id} | {self.customer_name} | {self.quantity} x {self.item} | {self.pickup_date.strftime(DATE_FORMAT)} | {"Picked Up" if self.collected else "Awaiting Pick"}"
    #turn a object into a dictionary
    def to_csv_row(self)-> dict[str,str | int]:
        return{
           "order_id": self.order_id,
           "customer_name": self.customer_name,
           "item": self.item,
           "quantity": self.quantity,
           "pickup_date": self.pickup_date.strftime(DATE_FORMAT),
           "collected": "yes" if self.collected else "no",
           "order_type": "regular",
           "gift_message": ""
        }

class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, gift_message:str)->None:
        super().__init__(order_id, customer_name, item, quantity, pickup_date, collected)
        if not gift_message.strip():
            raise ValueError("A gift order needs a gift message")
        self.gift_message = gift_message

    def __str__(self)->str:
        return f"{super().__str__()} | Gift message: {self.gift_message}"

    #override the to_csv_row method from the parent to include gift message
    def to_csv_row(self)->dict[str,str | int]:
        row = super().to_csv_row()
        row["order_type"] = "gift"
        row["gift_message"] = self.gift_message
        return row

    


class BakeSale:
    def __init__(self)->None:
        self.orders: list[BakeSaleOrder] = []

    def load_orders(self, csv_path: Path):
        try: 
            with open (csv_path,'r',encoding = 'utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    order_id = row["order_id"]
                    customer_name = row["customer_name"]
                    item = row["item"]
                    quantity = int(row["quantity"])
                    pickup_date = datetime.strptime(row["pickup_date"],DATE_FORMAT).date()
                    collected = row["collected"] == "yes"

                    #determine which type of order to add to create which type of object
                    order_type = row["order_type"]
                    if order_type == "regular":
                        order = BakeSaleOrder(order_id, customer_name,item,quantity,pickup_date,collected)
                    else:                        
                        order = GiftOrder(order_id, customer_name,item,quantity,pickup_date,collected,row["gift_message"])

                    self.add_order(order)

                #for testing, add one more order object to the list that is not on the file. 
                # # self.orders.append(GiftOrder("abc123","Sue","Candy",5,
                #                              datetime.strptime("1/1/20",DATE_FORMAT),True,"Happy Friday"))    
                # for order in self.orders:
                #     print(order)



        except FileNotFoundError:
            print ("File not found")           

    def add_order(self, order: BakeSaleOrder)->None:
        #if the object was not already found in the list
        if self.find_order(order.order_id) is not None:
            raise ValueError(f"Order ID{order.order_id} is already in use")
        self.orders.append(order)

    def find_order(self,order_id: str)-> BakeSaleOrder | None:
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    #write the current orders back the CSV file
    def save_orders(self, csv_path: Path)->None:
        with open(csv_path, 'w', newline="", encoding = "utf-8") as file:
            writer = csv.DictWriter(file,FIELD_NAMES)
            writer.writeheader()
            for order in self.orders:
                #convert each order object to a dictionary before writing to the file
                writer.writerow(order.to_csv_row())

    def prompt_for_order(self) -> None:
        order_id = input("Order ID: ").strip()
        customer_name = input("Customer name: ").strip()
        item = input("Item: ").strip()

        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Quantity must be a positive whole number.")
            return

        try:
            pickup_date = datetime.strptime(input("Pickup date (dd/mm/yy): ").strip(), DATE_FORMAT)
        except ValueError:
            print("Enter a valid date in dd/mm/yy format.")
            return

        try:
            order_type = input("Order type (regular/gift): ").strip().lower()
            if order_type == "regular":
                order = BakeSaleOrder(order_id, customer_name, item, quantity, pickup_date,False)
            elif order_type == "gift":
                gift_message = input("Gift message: ").strip()
                order = GiftOrder(order_id, customer_name, item, quantity, pickup_date, False, gift_message)
            else:
                raise ValueError("Order type must be regular or gift.")
            self.add_order(order)
        except ValueError as error:
            print(error)
            return

        print(f"Added order {order.order_id}.")


    def show_pickups(self) -> None:
        date_text = input("Pickup date (dd/mm/yy): ").strip()
        try:
            pickup_date = datetime.strptime(date_text, DATE_FORMAT)
        except ValueError:
            print("Enter a valid date in dd/mm/yy format.")
            return

        total_quantity = 0
        for order in self.orders:
            if order.pickup_date == pickup_date.date() and not order.collected:
                print(order)
                total_quantity += order.quantity

        if total_quantity:
            print(f"Total quantity: {total_quantity}")
        else:
            print("There are no pickups remaining for that date.")

    def mark_collected(self) -> None:
        order_id = input("Order ID: ").strip()
        order = self.find_order(order_id)
        if order is None:
            print(f"No order found with ID {order_id}.")
        elif order.collected:
            print(f"Order {order_id} has already been collected.")
        else:
            order.collected = True
            print(f"Marked {order_id} as collected.")

    def list_orders(self)->None:
        if not self.orders:
            print("No orders")
        else:
            for order in self.orders:
                print(order)

def main() -> None:
    bake_sale = BakeSale()
    try:
        bake_sale.load_orders(CSV_PATH)
    except FileNotFoundError:
        print(f"Could not load the orders")
        return

    while True:
        print(
            "\n=== Bake Sale Pickup Tracker ===\n"
            "1. List all orders\n"
            "2. Show pickups for a date\n"
            "3. Add an order\n"
            "4. Mark an order as collected\n"
            "5. Save and exit"
        )
        choice = input("Choice: ").strip()

        if choice == "1":
            bake_sale.list_orders()
        elif choice == "2":
            bake_sale.show_pickups()
        elif choice == "3":
            bake_sale.prompt_for_order()
        elif choice == "4":
            bake_sale.mark_collected()
        elif choice == "5":            
            bake_sale.save_orders(CSV_PATH)                     
            print("Orders saved. Goodbye!")
            break
        else:
            print("Choose a menu option from 1 to 5.")

if __name__ == "__main__":
    main()







# bake_sale = BakeSale()
# bake_sale.load_orders(csv_path)
# bake_sale.save_orders(csv_path)

#prompt for order
#Show_Pickups
#mark collected

#mainline


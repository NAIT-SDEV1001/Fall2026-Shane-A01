from datetime import datetime
from pathlib import Path
import csv
DATE_FORMAT = "%d/%m/%y"

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
        return f"{self.order} | {self.customer_name} | {self.quantity} x {self.item} | {self.pickup_date.strftime(DATE_FORMAT)} | {"Picked Up" if self.collected else "Awaiting Pick"}"

class GiftOrder(BakeSaleOrder):
    def __init__(self, order_id: str, customer_name: str, item: str, quantity: int, pickup_date: datetime, collected: bool, gift_message:str)->None:
        super().__init__(order_id, customer_name, item, quantity, pickup_date, collected)
        if not gift_message.strip():
            raise ValueError("A gift order needs a gift message")
        self.gift_message = gift_message

    def __str__(self)->str:
        return f"{super().__str__()} | Gift message: {self.gift_message}"

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
                    




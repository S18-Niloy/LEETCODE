class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        subtotal = 0.0

        for i in range(len(product)):
            product_id = product[i]
            quantity = amount[i]
            price = self.prices[self.products.index(product_id)]
            subtotal += price * quantity

        if self.customer_count % self.n == 0:
            subtotal *= (100 - self.discount) / 100

        return subtotal

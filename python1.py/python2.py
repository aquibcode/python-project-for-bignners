def calculate_total_price(prices_file: str, shopping_file: str) -> int:
    '''Compute the total amount spent on the products.

    Args:
        prices_file (str): path of file containing product purchase details.
        shopping_file (str): path of file containing product prices.

    Returns:
        float: The total amount.
    '''
    product = {}
    with open(prices_file, 'r') as pf:
        for line in pf:
            product,price = line.strip().split(',')
            prices[product] = float[price]

    total_cost = 0
    with open(shopping_file,'r') as sf:
        for line in sf:
            product,quantity = line.strip().split(',')
            if product in prices:
                total_cost += prices[product]*int[quantity]  
    return total_cost                  

# Example inputs
fruit_prices = {
    "apple": 1.5,
    "banana": 1.0,
    "cherry": 2.5,
    "date": 3.0,
    "elderberry": 4.0
}
fruits = ["fig", "banana", "cherry", "date", "elderberry"]

# Operations
fruit_prices[fruits[0]] = 3
fruit_prices[fruits[1]] = 2
fruit_prices[fruits[2]] += 2
del fruit_prices[fruits[3]]

print(f"The price of {fruits[4]} is: {fruit_prices[fruits[4]]}")
print("Sorted list of fruit names:", sorted(fruit_prices.keys()))
print("Sorted list of fruit prices:", sorted(fruit_prices.values()))

# Function to increase prices
def increase_prices(fruit_prices: dict) -> None:
    for fruit in fruit_prices:
        fruit_prices[fruit] = round(fruit_prices[fruit] * 1.2, 2)

# Example usage
increase_prices(fruit_prices)
print("Fruit prices after increase:", fruit_prices)

# Function to convert string to dict
def dict_from_string(string: str, key_type, value_type) -> dict:
    items = string.split(',')
    result = {}
    for item in items:
        key, value = item.split(':')
        result[key_type(key.strip())] = value_type(value.strip())
    return result

# Example usage
string = "apple: 1.5, banana: 1.0, cherry: 2.5, date: 3.0, elderberry: 4.0"
fruit_prices_dict = dict_from_string(string, str, float)
print("Dictionary from string:", fruit_prices_dict)

# Function to convert dict to string
def dict_to_string(D: dict) -> str:
    return '\n'.join(f"{key}: {value}" for key, value in D.items())

# Example usage
fruit_prices_str = dict_to_string(fruit_prices)
print("Dictionary to string:\n", fruit_prices_str)

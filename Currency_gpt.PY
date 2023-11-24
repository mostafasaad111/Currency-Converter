import requests

init_currency = input("Enter an initial currency: ")
target_currency = input("Enter a target currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("The amount must be greater than 0 ")
        else:
            break
    except ValueError:
        print("The amount must be a numeric value!")

url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
headers = {"apikey": "6ro6dClC5zZuFVRehBz3CzCPR0vdmx1N"}

response = requests.get(url, headers=headers)

status_code = response.status_code

if status_code != 200:
    print("Sorry, there was an error")
    quit()

result = response.json()

# Assuming the structure of the response is like {'result': converted_amount}
# If the structure is different, adjust the following line accordingly.
converted_amount = result.get("result", "N/A")

print(f"{amount} {init_currency} = {converted_amount} {target_currency}")

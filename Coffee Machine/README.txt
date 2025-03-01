☕ Coffee Machine Program
-----------------------------
Welcome to the Coffee Machine Program! This interactive Python application lets you order delicious coffee, manage resources, and enjoy a virtual barista experience. 🚀

🔥 Features
------------
🏆 Make Coffee – Select from Espresso, Latte, or Cappuccino.
💰 Handle Transactions – Insert coins, and get the correct change.
📊 Check Resources – Monitor water, milk, and coffee supplies.
🔑 Admin Mode – Refill supplies and turn off the machine.

🎯 Requirements
------------------
Prompt user for input:
   Displays: What would you like? (espresso/latte/cappuccino):
   Continues prompting after every action.
Turn off the Coffee Machine:
   Enter off to shut down the machine.
Print report:
   Enter report to display available resources:
      Water: 100ml
      Milk: 50ml
      Coffee: 76g
      Money: $2.5
Check resources before making coffee:
   If there are not enough resources, display an error message.
   Example: Sorry, there is not enough water.
Process coins:
   Accepts quarters ($0.25), dimes ($0.10), nickels ($0.05), and pennies ($0.01).
   Calculates total amount inserted.
Check transaction success:
   If money is insufficient, display: Sorry, that's not enough money. Money refunded.
   If excess money is inserted, return change.
   Example: Here is $2.45 in change.
Make Coffee:
   Deducts used resources from the machine.
   Displays a success message: Here is your latte. Enjoy!
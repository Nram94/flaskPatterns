from flask import Flask, jsonify

app = Flask(__name__)

# Existing third-party payment API
class StripePayment:
    def pay_in_dollars(self, amount):
        return f"Paid ${amount} using Stripe."

# Adapter to make it compatible with a new payment interface
class PaymentAdapter:
    def __init__(self, payment):
        self.payment = payment

    def pay_in_euros(self, amount):
        # Convert euros to dollars (simple conversion for illustration)
        amount_in_dollars = amount * 1.1
        return self.payment.pay_in_dollars(amount_in_dollars)

@app.route('/pay/<int:amount>')
def pay(amount):
    stripe_payment = StripePayment()
    adapter = PaymentAdapter(stripe_payment)
    return adapter.pay_in_euros(amount)

if __name__ == "__main__":
    app.run(debug=True)

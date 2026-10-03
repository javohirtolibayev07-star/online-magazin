from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "magazin_very_secret_key"

products = [
    {
        "id": 1,
        "name": "Smartfon",
        "price": 2500000,
        "description": "Yaxshi sifatli smartfon",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    },
    {
        "id": 2,
        "name": "Noutbuk",
        "price": 6500000,
        "description": "Ishlash uchun qulay noutbuk",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    },
    {
        "id": 3,
        "name": "Sovutgich",
        "price": 3200000,
        "description": "Kichik oilaviy sovutgich",
        "image": "https://images.unsplash.com/photo-1585518419759-7fe2e0fbf8a3"
    },
    {
        "id": 4,
        "name": "Konditsioner",
        "price": 5200000,
        "description": "Yoz va qish uchun qulay",
        "image": "https://images.unsplash.com/photo-1581578731548-c64695cc6952"
    }
]

@app.route("/")
def home():
    cart_count = sum(session.get("cart", {}).values())
    return render_template("index.html", products=products, cart_count=cart_count)

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []
    total = 0

    for product_id, qty in cart.items():
        product = next((p for p in products if p["id"] == product_id), None)
        if product:
            item_total = product["price"] * qty
            items.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "qty": qty,
                "item_total": item_total
            })
            total += item_total

    return render_template("cart.html", items=items, total=total)

@app.route("/clear")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(debug=True)

let cart;
if (localStorage.getItem('cart') == null) {
    cart = {}
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}
let total = 0;
for (item in cart) {
    let name = cart[item][1]
    let quantity = cart[item][0]
    let price = cart[item][2]
    total += cart[item][2]
    itemString = `<li class="list-group-item">${name}<span class="badge badge-primary badge-pill">${quantity}</span><span class="badge badge-primary badge-pill">${price}</span></li>`
    $('#item_list').append(itemString);
}
totalPrice = `<li class="list-group-item d-flex justify-content-between align-items-center">Total<span>${total}</span></li>`
$('#item_list').append(totalPrice)
$('#items').val(JSON.stringify(cart));
$('#total').val(total);
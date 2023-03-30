from flask import Blueprint, session, render_template, redirect, url_for, request, g
tickets = []
orders = []

ticket = Blueprint("ticket", __name__, template_folder='./views/',
                   static_folder='./static/', root_path="./")


@ticket.route("/list")
def ticket_list():
    return render_template("/ticket/ticket_table.html", ticket_array=tickets)

@ticket.route("/list_order")
def orders_list():
    return render_template("/ticket/order_table.html", order_array=orders)


@ticket.route("/register", methods=['GET', 'POST'])
def ticket_register():
    if request.method == 'POST':
        client_code = request.form['inputClientCode']
        date_ticket = request.form['inputDateTicket']
        tickets.append({'ticket_id': len(tickets) + 1, 'client_code': client_code,
                        'date_ticket': date_ticket, 'is_paid': False})
        return redirect("/ticket/list")
    return render_template("/ticket/ticket_register.html")

@ticket.route("/register_order", methods=['GET', 'POST'])
def ticket_register_order():
    if request.method == 'POST':
        ticket_code = request.form['inputTicketCode']
        product = request.form['inputProduct']
        qtd = request.form['inputQuantity']
        service_code = request.form['inputServiceCode']
        date = request.form['inputDateOrder']
        hour = request.form['inputHourTicket']
        orders.append({
            'order_id': len(orders) + 1,
            'ticket_code': ticket_code,
            'product': product,
            'qtd': qtd,
            'service_code': service_code,
            'date': date,
            'hour': hour
        })
        return redirect("/ticket/list_order")
    return render_template("/ticket/ticket_register_order.html", ticket_array=tickets)
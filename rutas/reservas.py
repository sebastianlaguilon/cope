from modelos import Reserva,cargar_reserva,guardar_reserva,cargar_clientes,cargar_habitaciones
from flask import Blueprint,render_template,request,redirect,url_for,flash

reservas_bp = Blueprint('reservas', __name__)

@reservas_bp.route('/reservas')
def ver_reservas():
    lista = cargar_reserva()
    return render_template('reservas.html', reservas=lista)

@reservas_bp.route('/reservas/agregar', methods=['GET', 'POST'])
def agregar_reserva():
    clientes = cargar_clientes()
    habitaciones = cargar_habitaciones()

    if request.method == 'POST':
        id_reserva = request.form['id_reserva']
        id_cliente = request.form['id_cliente']
        numero_habitacion = request.form['numero_habitacion']
        fecha_entrada = request.form['fecha_entrada']
        fecha_salida = request.form['fecha_salida']
        estado = request.form['estado']
        total = request.form['total']
        
        # Validar que el cliente exista
        if not any(c.id == id_cliente for c in clientes):
            flash('Cliente no encontrado')
            return redirect(url_for('reservas.agregar_reserva'))
        
    
        nueva = Reserva(id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, estado, total)
        # Verificar que la habitación esté disponible en ese rango
        for r in cargar_reserva():
                if r.numero_habitacion == numero_habitacion and r.estado == 'activa':
                    if not (fecha_salida <= r.fecha_entrada or fecha_entrada >= r.fecha_salida):
                        flash('La habitación ya está reservada en ese período')
                        return redirect(url_for('reservas.agregar_reserva'))
        guardar_reserva(nueva)
        flash('Reserva creada correctamente')
        return redirect(url_for('reservas.ver_reservas'))

    return render_template('agregar_reserva.html', clientes=clientes, habitaciones=habitaciones)


@reservas_bp.route('/reservas/cliente/<id_cliente>')
def historial_por_cliente(id_cliente):
    reservas = cargar_reserva()
    historial = [r for r in reservas if r.id_cliente == id_cliente]
    return render_template('historial_cliente.html', reservas=historial, id_cliente=id_cliente)

@reservas_bp.route('/reservas/editar/<id_reserva>', methods=['GET','POST'])
def editar_reserva(id_reserva):
    reservas = cargar_reserva()
    reserva = next((r for r in reservas if r.id_reserva == id_reserva),None)
    
    if not reserva:
        flash("Reserva no entontrada ")
        return redirect(url_for('reservas.ver_reservas'))

    if request.method == 'POST':
        reserva.fecha_entrada == request.form['fecha_entrada']
        reserva.fecha_salida == request.form['fecha_salida']
        reserva.estado == request.form['estado']
        reserva.total == request.form['total']
        guardar_reserva(reservas) # guarda toda la lista 
        flash('Reserva actualizada correctamente')
        return redirect(url_for('reservas.ver_reservas'))
    
    return render_template('editar_reserva.html', reserva=reserva) 

@reservas_bp.route('/reservas/cancelar/<id_reserva>')
def cancelar_reserva(id_reserva):
    reservas = cargar_reserva()
    reserva = next((r for r in reservas if r.id_reserva == id_reserva), None)
    
    if reserva:
        reserva.estado = 'cancelada'
        guardar_reserva(reservas)
        flash('Reserva cancelada ')
        
    else: 
        flash('Reserva no encontrada')
            
    return redirect(url_for('reservas.ver_resevas'))



        
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Maquinaria, CategoriaFaena


def catalogo(request):
    query = request.GET.get('q')
    categoria_id = request.GET.get('categoria')

    maquinarias = Maquinaria.objects.filter(estado='DISPONIBLE')

    if query:
        maquinarias = maquinarias.filter(nombre__icontains=query)
    if categoria_id:
        maquinarias = maquinarias.filter(categoria_id=categoria_id)

    categorias = CategoriaFaena.objects.all()

    context = {
        'maquinarias': maquinarias,
        'categorias': categorias,
        'categoria_seleccionada': int(categoria_id) if categoria_id else None,
        'query': query or ''
    }
    return render(request, 'maquinarias/catalogo.html', context)


def detalle_maquinaria(request, pk):
    maquinaria = get_object_or_404(Maquinaria, pk=pk)
    return render(request, 'maquinarias/detalle.html', {'maquinaria': maquinaria})


def agregar_al_cotizador(request, pk):
    maquinaria = get_object_or_404(Maquinaria, pk=pk)
    dias = int(request.POST.get('dias', 1))

    
    cotizador = request.session.get('cotizador', {})
    pk_str = str(pk)

    if pk_str in cotizador:
        cotizador[pk_str]['dias'] += dias
    else:
        cotizador[pk_str] = {
            'nombre': maquinaria.nombre,
            'codigo': maquinaria.codigo,
            'precio_dia': maquinaria.precio_arriendo_dia,
            'garantia': maquinaria.garantia_requerida,
            'dias': dias,
        }

    request.session['cotizador'] = cotizador
    messages.success(request, f"Se agregó '{maquinaria.nombre}' a la cotización.")
    return redirect('ver_cotizador')

def ver_cotizador(request):
    cotizador = request.session.get('cotizador', {})
    items = []
    subtotal = 0
    total_garantia = 0

    for pk, item in cotizador.items():
        total_item = item['precio_dia'] * item['dias']
        subtotal += total_item
        total_garantia += item['garantia']
        items.append({
            'pk': pk,
            'nombre': item['nombre'],
            'codigo': item['codigo'],
            'precio_dia': item['precio_dia'],
            'garantia': item['garantia'],
            'dias': item['dias'],
            'total_item': total_item
        })

    iva = int(subtotal * 0.19)  
    total_general = subtotal + iva + total_garantia

    context = {
        'items': items,
        'subtotal': subtotal,
        'iva': iva,
        'total_garantia': total_garantia,
        'total_general': total_general
    }
    return render(request, 'maquinarias/cotizador.html', context)

def eliminar_del_cotizador(request, pk):
    cotizador = request.session.get('cotizador', {})
    pk_str = str(pk)
    if pk_str in cotizador:
        del cotizador[pk_str]
        request.session['cotizador'] = cotizador
        messages.info(request, "Elemento eliminado de la cotización.")
    return redirect('ver_cotizador')

def vaciar_cotizador(request):
    if 'cotizador' in request.session:
        del request.session['cotizador']
        messages.info(request, "Se ha limpiado la cotización.")
    return redirect('ver_cotizador')
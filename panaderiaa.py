panaderia = {
    'panesSalados': {"productos":list([
        {"nombre":"Baguette","valor":3000},
        {"nombre":"Pan de campo", "valor":2500},
        {"nombre":"Pan de centeno","valor":3500},
        {"nombre":"Pan de ajo","valor":1000},
        {"nombre":"Pan de molde integral","valor":3000},
        {"nombre":"Pan de queso","valor":1500},
        {"nombre":"Pan de aceitunas","valor":3000},
        {"nombre":"Bollos de pizza","valor":3500},
        {"nombre":"Pan de cebolla","valor":2000},
        {"nombre":"Pan de maíz","valor":2000}])},
    'panesDulces': {"productos":list([
        {"nombre":"Croissant","valor":3000},
        {"nombre":"Rosca de Reyes","valor":3000},
        {"nombre":"Pan de muerto","valor":3000},
        {"nombre":"Pan de canela","valor":3000},
        {"nombre":"Pan de banana","valor":3000},
        {"nombre":"Pan de zanahoria","valor":3000},
        {"nombre":"Donas","valor":3000},
        {"nombre":"Pan de jengibre","valor":3000},
        {"nombre":"Conchas","valor":3000},
        {"nombre":"Churros","valor":3000}])},
    'postres': {"productos":list([
        {"nombre":"Tarta de manzana","valor":3000},
        {"nombre":"Cupcakes","valor":3000},
        {"nombre":"Galletas decoradas","valor":3000},
        {"nombre":"Pastel de zanahoria","valor":3000},
        {"nombre":"Brownies","valor":3000},
        {"nombre":"Cheesecake","valor":3000},
        {"nombre":"Macarons","valor":3000},
        {"nombre":"Éclairs","valor":3000},
        {"nombre":"Tarta de frutas","valor":3000},
        {"nombre":"Donas","valor":3000}])}
}

print("""
0: Panes salados
1: Panes dulces
2: Postres""")

categoria = int(input("Introduzca el numero de la categoria: "))

if categoria == 0:
    categoria = "panesSalados" 

elif categoria == 1:
    categoria = "panesDulces"

elif categoria == 2:
    categoria = "postres"
    
else:
    print("Esta categoria no existe")

for i, val in enumerate(panaderia[categoria]["productos"]): 
    nombre = val["nombre"]
    valor = val["valor"]
    print(f"""{i} {nombre}, el valor es: {valor}""")

producto = int(input("Ingrese el numero del producto que quiera comprar: "))

seleccionarProducto = panaderia[categoria]["productos"][producto]
seleccionarProductoNombre = seleccionarProducto["nombre"]
seleccionarProductoValor = seleccionarProducto["valor"]

print (f"""Haz seleccionado {seleccionarProductoNombre}, el valor es: {seleccionarProductoValor}""")


if seleccionarProductoNombre == "Donas":
    print("Existe una promocion en este producto, la cual es: \nCompre un six pack de donas y lleve otro totalmente gratis")
    sixPack = 18000
   
    promo = input("Desea la promocion?: ")
    
    if promo.lower() == "si":
        precio = 18000
        dinero = int(input("Ingrese su dinero: "))
        if dinero >= precio:
            cambio = dinero - precio
            print("Su cambio es:", cambio)
            
    else:     
        precio = seleccionarProductoValor
        dinero = int(input("Ingrese su dinero: "))
        if dinero >= precio:
            cambio = dinero - precio
            print("Su cambio es:", cambio)
        else:
            print("No le alcanza el dinero, vuelva mas tarde")
else:
    precio = seleccionarProductoValor
    dinero = int(input("Ingrese su dinero: "))
    if dinero >= precio:
        cambio = dinero - precio
        print("Su cambio es:", cambio)
    else:
        print("No le alcanza el dinero, vuelva mas tarde")
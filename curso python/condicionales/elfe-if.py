ingreso_mensual = 81000
gasto_mensual = 80000

#if anidado y else if (elif)

if ingreso_mensual > 10000:
    print("Estas bien en cualquier parte del mundo")
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien crack")
    else:
        print("Deberias ahorrar mas, estas gastando una banda")
    
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("Estas bien en Colombia")

elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
    
else:
    print("sos pobre")
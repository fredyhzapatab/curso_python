print("Tarea Clase Uno...\n\n");

nombre="Fredy";
ingresos=800;
egresos=800;
Cantidad=10;
vunitario=80;
vrtotal=Cantidad*vunitario;
print("Hola mi nombre es: "+ str(nombre) +" tengo una empresa de tecnologia que tiene unos ingresos de "
      + str(ingresos) +" y unos gastos de:" +str(egresos)+"\n \n");

print("Realizamos una venta de:\n"); 

print("______________________________________________________________________________________________________");
print("Producto                                    |      Cantidad       |     VrUnitario     |   Vr Total  |");
print("____________________________________________|_____________________|____________________|_____________|");
print("Computadores Todo en Uno Remanofacturados   |         {}          |          {}        |       {}   |".format(Cantidad,vunitario,vrtotal));
print("____________________________________________|_____________________|____________________|_____________|");
print("\n");

canteqinv=100;
totaleqinv=canteqinv-Cantidad

print("En inventario tenemos :\n"); 
print("______________________________________________________________________________________________________________");
print("Producto                                    |  Cantidad Vendida   | Total Eq Inventario|Total Eq Existencia  |");
print("____________________________________________|_____________________|____________________|_____________________|");
print("Computadores Todo en Uno Remanofacturados   |         {}          |          {}       |            {}       |".format(Cantidad,canteqinv,totaleqinv));
print("____________________________________________|_____________________|____________________|_____________________|");

vrtotalexist=vunitario*totaleqinv
total_inventario=vrtotalexist+vrtotal
porcentotalvta=total_inventario%vrtotalexist/100

print("Porcentaje de Venta inicial de :\n"); 
print("_____________________________________________________________________________________________________________________");
print("Producto                                    |Valor Total Existencias|Valor Total Ventas|Porcentaje Total de Ventas  |");
print("____________________________________________|_______________________|__________________|____________________________|");
print("Computadores Todo en Uno Remanofacturados   |         {}          |          {}     |             {}            |    ".format(vrtotalexist,vrtotal,porcentotalvta));
print("____________________________________________|_____________________|____________________|____________________________|");

x1=vrtotal
y1=porcentotalvta

print("El valor total de las Ventas es igual al Porcentaje de Venta\n");
if x1 == y1:
    print(" SI ...El valor total de las Ventas es igual al Porcentaje de Venta\n");
else:
    print("Eso es incorrecto")

x2=vrtotalexist
y2=vrtotal
   
print("El valor total de Existencias es MAYOR al Valor Total de Venta \n");

if x2 > y2:
    print(" SI ...El valor total de Existencias es MAYOR que el Valor Total de Ventas\n");
else:
    print("Eso es incorrecto")

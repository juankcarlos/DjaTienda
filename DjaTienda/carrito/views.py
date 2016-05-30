from django.shortcuts import render, HttpResponse, HttpResponseRedirect, RequestContext, render_to_response
from  carrito.models import Categoria, Producto, Factura, DetallesVenta
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
# metodo que muestra todos los productos
def ver(request):
    p = Producto.objects.all()
    return render(request, "index.html", {"productos": p})

#metodo que recibe el id del producto
#para mostrar el producto  en la vista
def detalles(request, idprod):
    p = Producto.objects.filter(id=idprod)
    return render(request, "verproducto.html", {"producto": p})

#metodo que recibe el nombre de la categoria
#en el menu para mostrar los productos en la
#neva vista
def productoporcategoria(request, nomcat):
    cat =Categoria.objects.get(nombre=nomcat)
    lpr = Producto.objects.filter(categorias_id=cat.id)
    return render(request, "verproductosporcategoria.html", {"productos": lpr})

#metodo que muestra todos lo productos
#agregados ala tabla detallesventa que
#actua como el carrito de compras
def vcarrito(request):
    if request.session.get('idfact'):
        vervent =DetallesVenta.objects.filter(facturas_id=request.session.get('idfact'))
        return render(request, 'vistacarrito.html', {'ventas': vervent})
    else:
        return render(request, 'vistacarrito.html')

def checar(request):
    #si el usuario no esta logueado
    if  request.user.is_authenticated():
       #si existe la variable de session que contiene el id de factura
        if request.session.get('idfact'):
            #usamos un tyr catch ya que si no existe id de factura y producto habria
            #un error en el query
            try:
                factb = DetallesVenta.objects.get(facturas_id=request.session.get('idfact'), productos_id=request.POST['idp'])
                newcant = int(factb.cantidad) + int(request.POST['num'])
                factb.cantidad = int(newcant)
                factb.save()
                return HttpResponseRedirect("/carrocomp/")
            except DetallesVenta.DoesNotExist:
                venta = DetallesVenta(facturas_id=request.session.get('idfact'), productos_id=request.POST['idp'], cantidad=request.POST['num'])
                venta.save()
                messages.add_message(request, messages.INFO, 'nuevo producto agregado al carrito')
                return HttpResponseRedirect("/carrocomp/")

        else:
            #si la factura no exite la creamos
            #y cramos la variable se sessio que contendra el id de la factura
            fact = Factura(fecha=datetime.now(), users_id=request.user.id)
            fact.save()
            factget = Factura.objects.get(fecha=datetime.now())
            request.session['idfact']=factget.id
            idfct = request.session.get('idfact')
            venta = DetallesVenta(facturas_id=idfct ,productos_id=request.POST['idp'], cantidad=request.POST['num'])
            venta.save()
            messages.add_message(request, messages.INFO, 'nuevo producto agregado al carrito')
            return HttpResponseRedirect("/carrocomp/")


    else:
        return HttpResponseRedirect("/formlog/")

#metodo que elimina un producto de la tabla que
#actua como el carrito de compras
def eliminardecarrito(request, idpr):
    borrar = DetallesVenta.objects.get(facturas_id=request.session.get('idfact'), productos_id=idpr)
    borrar.delete()
    return HttpResponseRedirect("/carrocomp/")

#metodo para ver el formulario de registro de usuarios
def form(request):
    return render(request, 'registrarusuario.html')

#metodo para insertar un nuevo usuario
def anadir(request):
    if request.method == 'POST':
        #user = User.objects.create(username=request.POST["username"], first_name=request.POST["first_name"], email=request.POST["email"], password=crypt.crypt(request.POST["password"]))
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
        user.first_name = request.POST["first_name"]
        user.is_superuser=1 #se asigna uno ya que es un usario que no es admin
        user.save()
        messages.add_message(request, messages.INFO, 'Su cuenta fue creada con exito')
        return HttpResponseRedirect("/registrar/")

#metdodo para mostrar el formulario de agregar productos
#el cual se le pasa todas las categorias para que se pueda
#seleccionar alguna
def addprod(request):
    cat = Categoria.objects.all()
    return render(request, "anadirproductos.html", {"categorias": cat})


#metodo que toma todos los campos del formulario
#para crear un nuevp producto
def regprod(request):
    if request.method == 'POST':
        newdoc = Producto(nombre=request.POST['nombre'], docfile=request.FILES['docfile'], precio=request.POST['num'], descripcion=request.POST['des'], categorias_id=request.POST['sele'])
        newdoc.save()
        messages.add_message(request, messages.INFO, 'nuevo producto registrado con exito')
        return HttpResponseRedirect("/foraddpre/")


#metodo para mostrar el formulario de login
def logform(request):
    return  render(request, "login.html")

#metod de autentificacion de usuarios
def log(request):
    user = authenticate(username=request.POST["nombre"], password=request.POST["password"])
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        messages.add_message(request, messages.ERROR, 'usuario o password incorrectos')
        return HttpResponseRedirect("/formlog/")

#metodo de logout
def salir(request):
    #se elimina la variable de sesion idfact y la session de usuarios
    try:
        auth.logout(request)
        del request.session['idfact']
        return HttpResponseRedirect("/")
    except KeyError:
        pass
    return HttpResponseRedirect("/")

#metodo que muestra el templa de finalizacion de compra
def finalizar(request):
    return render(request, "comprafinalizada.html")

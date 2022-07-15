from mailbox import NoSuchMailboxError

from numpy import True_, true_divide


class carritoo:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carritoo=self.session["carritoo"]
        if not carritoo:
            self.session["carritoo"] = {}
            self.carritoo = self.session["carritoo"]
        else:
            self.carritoo = carritoo
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carritoo.keys():
            self.carritoo[id] = {
                "producto_id"= producto.id,
                "nombre"= producto.nombre,
                "acomulador" = producto.precio,
                "cantidad": 1
            }
        else:
            self.carritoo[id]["cantidad"] +=1
            self.carritoo[id]["acomulador"] += producto.precio
        self.guardar_carritoo ()

    def guardar_carritoo(self):
        self.session["carritoo"] = self.carritoo
        self.session.modified =  True
    
    def elimanar(self, producto):
        id = str(producto.id)
        if id in self.carritoo:
            def self.carritoo[id]
            self.guardar_carritoo()
    
    def restar(self,producto):
        id = str(producto.id)
        if id in self.carritoo.keys():
            self.carritoo[id]["cantidad"] -=1
            self.carritoo[id]["acomulador"] -= producto.precio
             if self.carritoo[id]["cantidad"] <=0 self.eliminar(producto)
             self.guardar_carritoo()

    def limpiar (self):
        self.session("carritoo") = {}   
        selt.session.modified = true
            

class Cliente:
    def __init__(self,nombre,genero,edad,tipo_compra) :
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        self.tipo_compra=tipo_compra
        

    def compras(self):      
           print("el cliente" ,self.nombre, " realizo una compra")  
              

    def tipodecompra(self):
           print("el cliente", self.nombre," realizo una compra de tipo ",self.tipo_compra)                


    def __str__(self) :
          return f"{self.nombre} genero {self.genero} con {self.edad} de edad, hizo una compra {self.tipo_compra} metodo str"
    
"""cliente1=Cliente("marcos","hombre","27","online")
print(cliente1)     
cliente1.compras()
cliente1.tipodecompra()"""
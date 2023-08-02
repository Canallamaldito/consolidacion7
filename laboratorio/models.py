from django.db import models

# Create your models here.

# Modelo Laboratorio
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    # Restricción: Un laboratorio posee un solo director general.
    # lo cual lo hice en DirectorGeneral ya que alli quedan unidos.
    
    # Nuevos campos para Parte 3
    ciudad = models.CharField(max_length=100, default=" ")  # Valor predeterminado: espacio en blanco
    pais = models.CharField(max_length=100, default=" ")  # Valor predeterminado: espacio en blanco
    
    def __str__(self):
        return self.nombre #esto hace que aparezca el nombre en la lista y no un obj
    
    class Meta:
        ordering = ['nombre']  # Ordenar por nombre de laboratorio (ascendente)

# Modelo DirectorGeneral
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    # DirectorGeneral representa a un director general de un laboratorio
    # y está vinculado a un laboratorio específico mediante la relación uno a uno 
    # definida por el campo laboratorio. Esto asegura que cada director general 
    # esté asociado con un solo laboratorio y que un laboratorio tenga 
    # solo un director general.
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

    # Nuevo campo para Parte 3
    especialidad = models.CharField(max_length=100, default=" ")  # Valor predeterminado: espacio en blanco

    def __str__(self):
        return f"{self.nombre} - {self.laboratorio.nombre}"  # Representación del modelo como cadena

    class Meta:
        ordering = ['nombre']  # Ordenar por nombre de director general (ascendente)


# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    #para establecer una relación uno a muchos (many-to-one) con el modelo Laboratorio.
    #Esto significa que cada instancia del modelo Producto estará vinculada a una 
    #instancia del modelo. Es decir, varios productos pueden pertenecer a un mismo laboratorio.
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
    f_fabricacion = models.DateField()  # Fecha de fabricación del producto
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de costo del producto
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de venta del producto
    
    class Meta:
        ordering = ['nombre']  # Ordenar por nombre de Producto (ascendente)
    
    def get_year_fabricacion(self):
        return self.f_fabricacion.year  # Obtener el año de fabricación del producto
    
    # Restricción: Un laboratorio fabrica muchos productos para determinado tratamiento médico, y dichos productos fabricados pertenecen a un solo laboratorio.

class BoardsModel(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    modificado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
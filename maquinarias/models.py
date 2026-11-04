from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class CategoriaFaena(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoria")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría de Faena"
        verbose_name_plural = "Categorías de Faena"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Maquinaria(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('ARRENDADO', 'En Arriendo'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
        ('FUERA_SERVICIO', 'Fuera de Servicio'),
    ]

    TIPO_OFERTA_CHOICES = [
        ('ARRIENDO', 'Solo Arriendo'),
        ('VENTA', 'Solo Venta'),
        ('AMBOS', 'Arriendo y Venta'),
    ]

    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código de Serie/SKU")
    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Maquinaria")
    categoria = models.ForeignKey(CategoriaFaena, on_delete=models.CASCADE, related_name="maquinarias", verbose_name="Categoría de Faena")
    descripcion = models.TextField(verbose_name="Descripción General y Especificaciones")
    
    # Precios y garantias
    precio_arriendo_dia = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        verbose_name="Precio Arriendo por Día ($)"
    )
    precio_venta = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        verbose_name="Precio de Venta ($)",
        blank=True,
        null=True
    )
    garantia_requerida = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        verbose_name="Monto de Garantía ($)"
    )
    
    # Control de Stock y Estado
    stock = models.PositiveIntegerField(default=1, verbose_name="Stock Disponible")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE', verbose_name="Estado Operativo")
    tipo_oferta = models.CharField(max_length=10, choices=TIPO_OFERTA_CHOICES, default='ARRIENDO', verbose_name="Modalidad")
    
    # Archivos de Medios e Historial
    imagen = models.ImageField(upload_to='maquinarias/', blank=True, null=True, verbose_name="Fotografía de la Maquinaria")
    destacado = models.BooleanField(default=False, verbose_name="Mostrar en Inicio")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Maquinaria / Equipo"
        verbose_name_plural = "Maquinarias y Equipos"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    # Validación personalizada de modelo
    def clean(self):
        super().clean()
        if self.tipo_oferta in ['ARRIENDO', 'AMBOS'] and self.precio_arriendo_dia <= 0:
            raise ValidationError({'precio_arriendo_dia': 'El precio de arriendo diario debe ser mayor a 0 para ofertas de arriendo.'})
        if self.tipo_oferta in ['VENTA', 'AMBOS'] and (self.precio_venta is None or self.precio_venta <= 0):
            raise ValidationError({'precio_venta': 'El precio de venta debe ser mayor a 0 para ofertas de venta.'})
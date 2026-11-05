from django.core.management.base import BaseCommand
from maquinarias.models import CategoriaFaena, Maquinaria

class Command(BaseCommand):
    help = 'Poblar la base de datos con categorias y maquinarias iniciales'

    def handle(self, *args, **kwargs):
        self.stdout.write("Cargando datos iniciales...")

        
        cat_excavacion, _ = CategoriaFaena.objects.get_or_create(
            nombre="Excavación y Movimiento de Tierra",
            defaults={"descripcion": "Equipos pesados para remoción de tierra, zanjas y cimentación."}
        )
        cat_carga, _ = CategoriaFaena.objects.get_or_create(
            nombre="Elevación y Carga",
            defaults={"descripcion": "Maquinaria para movimiento de materiales y trabajo en altura."}
        )
        cat_compactacion, _ = CategoriaFaena.objects.get_or_create(
            nombre="Compactación y Pavimentación",
            defaults={"descripcion": "Rodillos y equipos para aplanar y preparar terrenos o asfalto."}
        )

        
        maquinarias_data = [
            {
                "codigo": "EXC-001",
                "nombre": "Excavadora Oruga CAT 320",
                "categoria": cat_excavacion,
                "descripcion": "Excavadora hidráulica de 22 toneladas ideal para obras de gran envergadura. Eficiencia en consumo de combustible.",
                "precio_arriendo_dia": 120000,
                "precio_venta": 85000000,
                "garantia_requerida": 500000,
                "stock": 3,
                "destacado": True,
                "tipo_oferta": "AMBOS"
            },
            {
                "codigo": "RET-002",
                "nombre": "Retroexcavadora JCB 3CX",
                "categoria": cat_excavacion,
                "descripcion": "Versatilidad total para apertura de zanjas y movimiento de escombros en espacios urbanos.",
                "precio_arriendo_dia": 75000,
                "precio_venta": 45000000,
                "garantia_requerida": 300000,
                "stock": 5,
                "destacado": True,
                "tipo_oferta": "AMBOS"
            },
            {
                "codigo": "MAN-003",
                "nombre": "Manipulador Telescópico Manitou 18m",
                "categoria": cat_carga,
                "descripcion": "Capacidad de elevación hasta 18 metros de altura con carga máxima de 4 toneladas.",
                "precio_arriendo_dia": 95000,
                "precio_venta": 62000000,
                "garantia_requerida": 400000,
                "stock": 2,
                "destacado": True,
                "tipo_oferta": "AMBOS"
            },
            {
                "codigo": "ROD-004",
                "nombre": "Rodillo Compactador Doble Hamm HD 12",
                "categoria": cat_compactacion,
                "descripcion": "Compactador articulado ideal para capas de asfalto y suelo en caminos secundarios.",
                "precio_arriendo_dia": 50000,
                "precio_venta": 28000000,
                "garantia_requerida": 200000,
                "stock": 4,
                "destacado": False,
                "tipo_oferta": "ARRIENDO"
            }
        ]

        for data in maquinarias_data:
            Maquinaria.objects.get_or_create(codigo=data["codigo"], defaults=data)

        self.stdout.write(self.style.SUCCESS("¡Datos iniciales cargados con éxito!"))
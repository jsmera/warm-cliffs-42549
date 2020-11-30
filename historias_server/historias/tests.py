import pytest
from .models import HistoriaClinica, LineaReceta, LineaDieta
from historias_server.user.models import Usuario, Paciente
from historias_server.alimentacion.models import Alimentacion
from historias_server.medicacion.models import Medicacion
from django.core import mail

# Create your tests here.


@pytest.mark.django_db
class TestSentenceCoverage:
    def test_1(self):
        nutricionista = Usuario.objects.create(
            username="testuser", email="test@tester.com"
        )
        historia = HistoriaClinica.objects.create(nutricionista=nutricionista)
        response = historia.enviar_recetas()
        assert response == 0
        assert len(mail.outbox) == 0

    def test_2(self):
        nutricionista = Usuario.objects.create(
            username="testuser", email="test@tester.com"
        )
        paciente = Paciente.objects.create(
            first_name="Carlos",
            last_name="Mera",
            tipo_documento="CC",
            telefono="3137281580",
            email="merac1999@gmail.com",
            estado_civil="SO",
            num_documento="1107523406",
        )
        historia = HistoriaClinica.objects.create(
            nutricionista=nutricionista, paciente=paciente
        )
        vitamina_e = Medicacion.objects.create(
            nombre_medicamento="Vitamina E",
            unidad=2.0,
            cant_sodio=8.0,
            cant_calcio=9.0,
            cant_magnesio=8.0,
        )
        vitamina_c = Medicacion.objects.create(
            nombre_medicamento="Vitamina C",
            unidad=2.0,
            cant_sodio=6.0,
            cant_calcio=5.0,
            cant_magnesio=9.0,
        )
        LineaReceta.objects.create(
            hisotoria_clinica=historia,
            medicamento=vitamina_e,
            frecuencia="4",
            posologia=1.0,
        )
        LineaReceta.objects.create(
            hisotoria_clinica=historia,
            medicamento=vitamina_c,
            frecuencia="6",
            posologia=1.5,
        )
        manzana = Alimentacion.objects.create(
            nombre_alimento="Manzana",
            unidad=1.0,
            cant_sodio=8.0,
            cant_calcio=47.0,
            cant_magnesio=38.0,
            calorias=20.0,
            proteina=7.0,
            carbohidratos=28.0,
            grasas=9.0,
        )
        sandwich = Alimentacion.objects.create(
            nombre_alimento="Sandwich gitano",
            unidad=1.0,
            cant_sodio=14.0,
            cant_calcio=80.0,
            cant_magnesio=56.0,
            calorias=93.0,
            proteina=21.0,
            carbohidratos=91.0,
            grasas=50.0,
        )
        hamburguesa = Alimentacion.objects.create(
            nombre_alimento="Hamburguesa",
            unidad=1.0,
            cant_sodio=26.0,
            cant_calcio=10.0,
            cant_magnesio=16.0,
            calorias=80.0,
            proteina=62.0,
            carbohidratos=82.0,
            grasas=48.0,
        )
        LineaDieta.objects.create(
            hisotoria_clinica=historia, alimento=manzana, cantidad=2, frecuencia="3",
        )
        LineaDieta.objects.create(
            hisotoria_clinica=historia, alimento=sandwich, cantidad=1, frecuencia="4",
        )
        LineaDieta.objects.create(
            hisotoria_clinica=historia,
            alimento=hamburguesa,
            cantidad=1,
            frecuencia="6",
        )
        response = historia.enviar_recetas()
        assert response == 1
        assert len(mail.outbox) == 1


@pytest.mark.django_db
class TestDecisionCoverage:
    def test_1(self):
        nutricionista = Usuario.objects.create(
            username="testuser", email="test@tester.com"
        )
        historia = HistoriaClinica.objects.create(nutricionista=nutricionista)
        response = historia.enviar_recetas()
        assert response == 0
        assert len(mail.outbox) == 0

    def test_2(self):
        nutricionista = Usuario.objects.create(
            username="testuser", email="test@tester.com"
        )
        paciente = Paciente.objects.create(
            first_name="Carlos",
            last_name="Mera",
            tipo_documento="CC",
            telefono="3137281580",
            email="merac1999@gmail.com",
            estado_civil="SO",
            num_documento="1107523406",
        )
        historia = HistoriaClinica.objects.create(
            nutricionista=nutricionista, paciente=paciente
        )
        response = historia.enviar_recetas()
        assert response == 0
        assert len(mail.outbox) == 0

    def test_3(self):
        nutricionista = Usuario.objects.create(
            username="testuser", email="test@tester.com"
        )
        paciente = Paciente.objects.create(
            first_name="Carlos",
            last_name="Mera",
            tipo_documento="CC",
            telefono="3137281580",
            email="merac1999@gmail.com",
            estado_civil="SO",
            num_documento="1107523406",
        )
        historia = HistoriaClinica.objects.create(
            nutricionista=nutricionista, paciente=paciente
        )
        vitamina_e = Medicacion.objects.create(
            nombre_medicamento="Vitamina E",
            unidad=2.0,
            cant_sodio=8.0,
            cant_calcio=9.0,
            cant_magnesio=8.0,
        )
        vitamina_c = Medicacion.objects.create(
            nombre_medicamento="Vitamina C",
            unidad=2.0,
            cant_sodio=6.0,
            cant_calcio=5.0,
            cant_magnesio=9.0,
        )
        LineaReceta.objects.create(
            hisotoria_clinica=historia,
            medicamento=vitamina_e,
            frecuencia="4",
            posologia=1.0,
        )
        LineaReceta.objects.create(
            hisotoria_clinica=historia,
            medicamento=vitamina_c,
            frecuencia="6",
            posologia=1.5,
        )
        manzana = Alimentacion.objects.create(
            nombre_alimento="Manzana",
            unidad=1.0,
            cant_sodio=8.0,
            cant_calcio=47.0,
            cant_magnesio=38.0,
            calorias=20.0,
            proteina=7.0,
            carbohidratos=28.0,
            grasas=9.0,
        )
        sandwich = Alimentacion.objects.create(
            nombre_alimento="Sandwich gitano",
            unidad=1.0,
            cant_sodio=14.0,
            cant_calcio=80.0,
            cant_magnesio=56.0,
            calorias=93.0,
            proteina=21.0,
            carbohidratos=91.0,
            grasas=50.0,
        )
        hamburguesa = Alimentacion.objects.create(
            nombre_alimento="Hamburguesa",
            unidad=1.0,
            cant_sodio=26.0,
            cant_calcio=10.0,
            cant_magnesio=16.0,
            calorias=80.0,
            proteina=62.0,
            carbohidratos=82.0,
            grasas=48.0,
        )
        LineaDieta.objects.create(
            hisotoria_clinica=historia, alimento=manzana, cantidad=2, frecuencia="3",
        )
        LineaDieta.objects.create(
            hisotoria_clinica=historia, alimento=sandwich, cantidad=1, frecuencia="4",
        )
        LineaDieta.objects.create(
            hisotoria_clinica=historia,
            alimento=hamburguesa,
            cantidad=1,
            frecuencia="6",
        )
        response = historia.enviar_recetas()
        assert response == 1
        assert len(mail.outbox) == 1

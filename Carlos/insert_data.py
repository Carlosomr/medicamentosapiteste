from app import create_app
from app.database import db
from app.models import Medicamento
import oracledb
app = create_app()

with app.app_context():
    # Lista de medicamentos a serem inseridos
    conn
    cursor

    consulta
    
    medicamentos = [
        Medicamento(nome='Paracetamol', quantidade=100, descricao='Analgésico'),
        Medicamento(nome='Ibuprofeno', quantidade=150, descricao='Anti-inflamatório'),
        Medicamento(nome='Amoxicilina', quantidade=200, descricao='Antibiótico'),
        Medicamento(nome='Aspirina', quantidade=250, descricao='Anti-inflamatório e analgésico'),
        Medicamento(nome='Paracetamol', quantidade=100, descricao='Analgésico e antitérmico'),
        Medicamento(nome='Ibuprofeno', quantidade=150, descricao='Anti-inflamatório e analgésico'),
        Medicamento(nome='Amoxicilina', quantidade=200, descricao='Antibiótico de amplo espectro'),
        Medicamento(nome='Diclofenaco', quantidade=180, descricao='Anti-inflamatório e analgésico'),
        Medicamento(nome='Omeprazol', quantidade=220, descricao='Inibidor da bomba de prótons'),
        Medicamento(nome='Losartana', quantidade=140, descricao='Antagonista dos receptores de angiotensina'),
        Medicamento(nome='Simeticona', quantidade=130, descricao='Antiflatulento'),
        Medicamento(nome='Cetirizina', quantidade=110, descricao='Anti-histamínico'),
        Medicamento(nome='Levotiroxina', quantidade=160, descricao='Hormônio tireoidiano sintético'),
        Medicamento(nome='Metformina', quantidade=190, descricao='Antidiabético oral'),
        Medicamento(nome='Dexametasona', quantidade=120, descricao='Corticosteroide'),
        Medicamento(nome='Tramadol', quantidade=90, descricao='Analgesico opioide'),
        Medicamento(nome='Azitromicina', quantidade=170, descricao='Antibiótico macrolídeo'),
        Medicamento(nome='Furosemida', quantidade=200, descricao='Diurético de alça'),
        Medicamento(nome='Diazepam', quantidade=80, descricao='Ansiolítico e relaxante muscular')
    ]

    # Adicionar todos os medicamentos à sessão do banco de dados
    db.session.bulk_save_objects(medicamentos)
    
    # Commit para salvar as mudanças no banco de dados
    db.session.commit()

    print("Vários medicamentos inseridos com sucesso!")

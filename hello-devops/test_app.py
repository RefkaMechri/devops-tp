import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Créer un client de test
        self.app.testing = True  # Activer le mode test

    def test_home_route(self):
        response = self.app.get('/')  # Faire une requête GET à la route principale
        self.assertEqual(response.status_code, 200)  # Vérifier le code de statut
        self.assertEqual(response.data.decode(), "Hello, CI/CD")  # Vérifier le contenu de la réponse

if __name__ == "__main__":
    unittest.main()

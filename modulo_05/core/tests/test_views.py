from django.test import TestCase
class SanityTestCase(TestCase):
    """Testa se o ambiente de testes está configurado corretamente."""
    def test_verdade_universal(self):
        """O mais simples dos testes: verifica se True é True."""
        self.assertTrue(True)
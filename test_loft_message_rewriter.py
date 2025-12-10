"""
Unit tests for Loft WhatsApp Message Rewriter.
"""

import unittest
from loft_message_rewriter import LoftMessageRewriter


class TestLoftMessageRewriter(unittest.TestCase):
    """Test cases for the LoftMessageRewriter class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.rewriter = LoftMessageRewriter()
    
    def test_parse_date(self):
        """Test date parsing from DD/MM/YYYY to Mmm/YY format."""
        self.assertEqual(self.rewriter.parse_date("21/07/2025"), "Jul/25")
        self.assertEqual(self.rewriter.parse_date("20/08/2025"), "Ago/25")
        self.assertEqual(self.rewriter.parse_date("12/12/2024"), "Dez/24")
        self.assertEqual(self.rewriter.parse_date("01/01/2026"), "Jan/26")
        self.assertIsNone(self.rewriter.parse_date("invalid"))
        self.assertIsNone(self.rewriter.parse_date("32/13/2025"))
    
    def test_format_currency(self):
        """Test Brazilian Real currency formatting."""
        self.assertEqual(self.rewriter.format_currency(7450.85), "R$ 7.450,85")
        self.assertEqual(self.rewriter.format_currency(6622.10), "R$ 6.622,10")
        self.assertEqual(self.rewriter.format_currency(828.75), "R$ 828,75")
        self.assertEqual(self.rewriter.format_currency(1000), "R$ 1.000,00")
        self.assertEqual(self.rewriter.format_currency(10), "R$ 10,00")
    
    def test_bold(self):
        """Test WhatsApp bold formatting."""
        self.assertEqual(self.rewriter.bold("texto"), "*texto*")
        self.assertEqual(self.rewriter.bold("R$ 100,00"), "*R$ 100,00*")
    
    def test_extract_contract_number(self):
        """Test contract number extraction."""
        text1 = "Contrato nº 1681933. Identificamos..."
        self.assertEqual(self.rewriter.extract_contract_number(text1), "1681933")
        
        text2 = "contrato 12345 referente a..."
        self.assertEqual(self.rewriter.extract_contract_number(text2), "12345")
        
        text3 = "Sem número de contrato aqui"
        self.assertIsNone(self.rewriter.extract_contract_number(text3))
    
    def test_extract_dates(self):
        """Test date extraction from text."""
        text = "Aluguéis vencimento 21/07/2025 e 20/08/2025. Condomínios vencimento 12/07/2025 e 12/08/2025."
        dates = self.rewriter.extract_dates(text)
        self.assertEqual(len(dates), 4)
        self.assertIn("21/07/2025", dates)
        self.assertIn("20/08/2025", dates)
        self.assertIn("12/07/2025", dates)
        self.assertIn("12/08/2025", dates)
    
    def test_extract_currency_value(self):
        """Test currency value extraction."""
        text = "Valor total: R$ 7.450,85. Valor com desconto: R$ 6.622,10."
        
        total = self.rewriter.extract_currency_value(text, "Valor total")
        self.assertAlmostEqual(total, 7450.85, places=2)
        
        discount = self.rewriter.extract_currency_value(text, "Valor com desconto")
        self.assertAlmostEqual(discount, 6622.10, places=2)
        
        not_found = self.rewriter.extract_currency_value(text, "Valor inexistente")
        self.assertIsNone(not_found)
    
    def test_group_months_two_months(self):
        """Test grouping two months."""
        dates = ["21/07/2025", "20/08/2025"]
        result = self.rewriter.group_months(dates)
        self.assertEqual(result, "Jul e Ago/25")
    
    def test_group_months_duplicate_dates(self):
        """Test grouping with duplicate months."""
        dates = ["21/07/2025", "20/08/2025", "12/07/2025", "12/08/2025"]
        result = self.rewriter.group_months(dates)
        self.assertEqual(result, "Jul e Ago/25")
    
    def test_group_months_single_month(self):
        """Test grouping single month."""
        dates = ["21/07/2025"]
        result = self.rewriter.group_months(dates)
        self.assertEqual(result, "Jul/25")
    
    def test_group_months_three_months(self):
        """Test grouping three months."""
        dates = ["01/06/2025", "15/07/2025", "20/08/2025"]
        result = self.rewriter.group_months(dates)
        self.assertEqual(result, "Jun, Jul e Ago/25")
    
    def test_rewrite_message_complete(self):
        """Test complete message rewriting."""
        raw_message = """Contrato nº 1681933. Identificamos que a imobiliária apontou valores pendentes, mas já foram pagos por nós, como fiadores. Aluguéis vencimento 21/07/2025 e 20/08/2025. Condomínios vencimento 12/07/2025 e 12/08/2025. Valor total: R$ 7.450,85. Quero te apresentar nossa opção com desconto de 100% dos juros. Valor com desconto: R$ 6.622,10. Economia: R$ 828,75. Válida somente hoje."""
        
        output = self.rewriter.rewrite_message(raw_message, customer_name="Juraci")
        
        # Check key elements are present
        self.assertIn("Oi, Juraci! Tudo bem?", output)
        self.assertIn("contrato 1681933", output)
        self.assertIn("Jul e Ago/25", output)
        self.assertIn("100% dos juros", output)
        self.assertIn("*R$ 7.450,85*", output)
        self.assertIn("*R$ 6.622,10*", output)
        self.assertIn("*(Válido só hoje)*", output)
        self.assertIn("Posso gerar o boleto com esse desconto para você?", output)
    
    def test_rewrite_message_without_name(self):
        """Test message rewriting without customer name."""
        raw_message = """Contrato nº 12345. Valor total: R$ 1.000,00. Valor com desconto: R$ 900,00."""
        
        output = self.rewriter.rewrite_message(raw_message)
        
        # Should use generic greeting
        self.assertIn("Olá! Tudo bem?", output)
        self.assertNotIn("Oi,", output)
    
    def test_rewrite_message_handles_missing_data(self):
        """Test that rewriter handles missing data gracefully."""
        raw_message = "Algum texto sem dados estruturados."
        
        # Should not crash
        output = self.rewriter.rewrite_message(raw_message)
        self.assertIsInstance(output, str)
        self.assertIn("Olá!", output)


class TestMessageStructure(unittest.TestCase):
    """Test the structure of rewritten messages."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.rewriter = LoftMessageRewriter()
    
    def test_message_has_greeting(self):
        """Test that message starts with a greeting."""
        raw_message = "Contrato nº 123. Valor total: R$ 100,00."
        output = self.rewriter.rewrite_message(raw_message, customer_name="João")
        lines = output.split("\n")
        self.assertTrue(lines[0].startswith("Oi,") or lines[0].startswith("Olá"))
    
    def test_message_has_call_to_action(self):
        """Test that message ends with a question (CTA)."""
        raw_message = "Contrato nº 123. Valor total: R$ 100,00. Valor com desconto: R$ 90,00."
        output = self.rewriter.rewrite_message(raw_message)
        self.assertTrue(output.strip().endswith("?"))
    
    def test_message_uses_bold_for_values(self):
        """Test that monetary values are bolded."""
        raw_message = "Valor total: R$ 1.000,00. Valor com desconto: R$ 900,00."
        output = self.rewriter.rewrite_message(raw_message)
        self.assertIn("*R$", output)


if __name__ == "__main__":
    unittest.main()

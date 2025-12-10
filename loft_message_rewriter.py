"""
Loft WhatsApp Message Rewriter
Converts technical debt collection messages into "Estilo Direto" format.

This module transforms bureaucratic, technical messages into friendly,
direct WhatsApp messages that focus on solutions (discounts) rather than
problems (debt).
"""

import re
from typing import Dict, List, Optional
from datetime import datetime


class LoftMessageRewriter:
    """
    Rewriter class for transforming debt collection messages into
    friendly, direct WhatsApp format.
    """
    
    MONTHS_PT = {
        1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
        7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
    }
    
    def __init__(self):
        pass
    
    def parse_date(self, date_str: str) -> Optional[str]:
        """
        Convert full date (DD/MM/YYYY) to month/year format (Mmm/YY).
        
        Args:
            date_str: Date string in format DD/MM/YYYY
            
        Returns:
            Formatted string like "Jul/25" or None if invalid
        """
        try:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            month_abbr = self.MONTHS_PT[date_obj.month]
            year_short = str(date_obj.year)[2:]
            return f"{month_abbr}/{year_short}"
        except (ValueError, KeyError):
            return None
    
    def format_currency(self, value: float) -> str:
        """
        Format currency value in Brazilian Real format.
        
        Args:
            value: Numeric value
            
        Returns:
            Formatted string like "R$ 7.450,85"
        """
        formatted = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {formatted}"
    
    def bold(self, text: str) -> str:
        """
        Apply WhatsApp bold formatting using asterisks.
        
        Args:
            text: Text to make bold
            
        Returns:
            Text wrapped in asterisks
        """
        return f"*{text}*"
    
    def extract_contract_number(self, text: str) -> Optional[str]:
        """
        Extract contract number from text.
        
        Args:
            text: Input text containing contract number
            
        Returns:
            Contract number as string or None
        """
        match = re.search(r'[Cc]ontrato\s*n?º?\s*(\d+)', text)
        if match:
            return match.group(1)
        return None
    
    def extract_dates(self, text: str) -> List[str]:
        """
        Extract all dates in DD/MM/YYYY format from text.
        
        Args:
            text: Input text containing dates
            
        Returns:
            List of date strings in DD/MM/YYYY format
        """
        pattern = r'\d{2}/\d{2}/\d{4}'
        return re.findall(pattern, text)
    
    def extract_currency_value(self, text: str, label: str) -> Optional[float]:
        """
        Extract a currency value from text based on a label.
        
        Args:
            text: Input text
            label: Label to search for (e.g., "Valor total", "Valor com desconto")
            
        Returns:
            Float value or None if not found
        """
        # Pattern to match Brazilian Real format: R$ 1.234,56
        pattern = rf'{label}[:\s]*R\$\s*([\d.]+,\d{{2}})'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value_str = match.group(1).replace(".", "").replace(",", ".")
            return float(value_str)
        return None
    
    def group_months(self, dates: List[str]) -> str:
        """
        Group dates into a readable format like "Julho e Agosto/25".
        
        Args:
            dates: List of date strings
            
        Returns:
            Grouped month description
        """
        if not dates:
            return ""
        
        # Parse dates and keep track of month/year tuples for proper sorting
        date_tuples = []
        for date_str in dates:
            try:
                date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                date_tuples.append((date_obj.year, date_obj.month))
            except ValueError:
                continue
        
        if not date_tuples:
            return ""
        
        # Remove duplicates and sort chronologically
        unique_dates = sorted(set(date_tuples))
        
        if len(unique_dates) == 1:
            year, month = unique_dates[0]
            month_abbr = self.MONTHS_PT[month]
            year_short = str(year)[2:]
            return f"{month_abbr}/{year_short}"
        elif len(unique_dates) == 2:
            # Extract month names for full format
            months = []
            for year, month in unique_dates:
                months.append(self.MONTHS_PT[month])
            year_short = str(unique_dates[-1][0])[2:]
            return f"{months[0]} e {months[1]}/{year_short}"
        else:
            # For 3+ months, list them
            months = [self.MONTHS_PT[month] for year, month in unique_dates]
            year_short = str(unique_dates[-1][0])[2:]
            month_list = ", ".join(months[:-1]) + f" e {months[-1]}"
            return f"{month_list}/{year_short}"
    
    def rewrite_message(self, 
                       raw_message: str,
                       customer_name: Optional[str] = None) -> str:
        """
        Transform a raw debt collection message into "Estilo Direto" format.
        
        Args:
            raw_message: Original technical message
            customer_name: Optional customer name for personalization
            
        Returns:
            Rewritten message in friendly, direct style
        """
        # Extract key information
        contract_number = self.extract_contract_number(raw_message)
        dates = self.extract_dates(raw_message)
        total_value = self.extract_currency_value(raw_message, "Valor total")
        discount_value = self.extract_currency_value(raw_message, "Valor com desconto")
        
        # Build the message
        lines = []
        
        # 1. Greeting + Context
        if customer_name:
            lines.append(f"Oi, {customer_name}! Tudo bem?")
        else:
            lines.append("Olá! Tudo bem?")
        lines.append("")
        
        # 2. Contract context
        if contract_number:
            lines.append(f"Sobre o contrato {contract_number}, regularizamos os Aluguéis e Condomínios de {self.group_months(dates)} junto à imobiliária.")
        else:
            lines.append(f"Regularizamos os Aluguéis e Condomínios de {self.group_months(dates)} junto à imobiliária.")
        lines.append("")
        
        # 3. The Proposal - Focus on discount
        discount_percent = "100%"
        if "100%" in raw_message or "100 %" in raw_message:
            discount_percent = "100%"
        
        lines.append(f"Para quitarmos isso hoje, consegui isentar {discount_percent} dos juros da Loft:")
        lines.append("")
        
        if total_value and discount_value:
            lines.append(f"De: {self.bold(self.format_currency(total_value))}")
            lines.append(f"Por: {self.bold(self.format_currency(discount_value))} {self.bold('(Válido só hoje)')}")
            
            # Calculate savings
            savings = total_value - discount_value
            # Round to nearest whole number for display
            savings_rounded = float(round(savings))
            lines.append("")
            lines.append(f"É uma economia de {self.format_currency(savings_rounded)}. Posso gerar o boleto com esse desconto para você?")
        else:
            lines.append("Posso gerar o boleto com esse desconto para você?")
        
        return "\n".join(lines)


def main():
    """
    Example usage of the LoftMessageRewriter class.
    """
    rewriter = LoftMessageRewriter()
    
    # Example input from problem statement
    raw_input = """Contrato nº 1681933. Identificamos que a imobiliária apontou valores pendentes, mas já foram pagos por nós, como fiadores. Aluguéis vencimento 21/07/2025 e 20/08/2025. Condomínios vencimento 12/07/2025 e 12/08/2025. Valor total: R$ 7.450,85. Quero te apresentar nossa opção com desconto de 100% dos juros. Valor com desconto: R$ 6.622,10. Economia: R$ 828,75. Válida somente hoje."""
    
    # Transform the message
    output = rewriter.rewrite_message(raw_input, customer_name="Juraci")
    
    print("=" * 60)
    print("ENTRADA (Raw):")
    print("=" * 60)
    print(raw_input)
    print("\n")
    print("=" * 60)
    print("SAÍDA (Estilo Direto):")
    print("=" * 60)
    print(output)
    print("\n")


if __name__ == "__main__":
    main()

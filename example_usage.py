"""
Example usage of the Loft WhatsApp Message Rewriter.

This script demonstrates how to use the message rewriter to transform
technical debt collection messages into friendly, direct WhatsApp messages.
"""

from loft_message_rewriter import LoftMessageRewriter


def example_1():
    """Example from problem statement."""
    print("=" * 70)
    print("EXAMPLE 1: From Problem Statement")
    print("=" * 70)
    
    rewriter = LoftMessageRewriter()
    
    raw_input = """Contrato nº 1681933. Identificamos que a imobiliária apontou valores pendentes, mas já foram pagos por nós, como fiadores. Aluguéis vencimento 21/07/2025 e 20/08/2025. Condomínios vencimento 12/07/2025 e 12/08/2025. Valor total: R$ 7.450,85. Quero te apresentar nossa opção com desconto de 100% dos juros. Valor com desconto: R$ 6.622,10. Economia: R$ 828,75. Válida somente hoje."""
    
    output = rewriter.rewrite_message(raw_input, customer_name="Juraci")
    
    print("\nENTRADA (Raw):")
    print("-" * 70)
    print(raw_input)
    print("\n")
    print("SAÍDA (Estilo Direto):")
    print("-" * 70)
    print(output)
    print("\n")


def example_2():
    """Example without customer name."""
    print("=" * 70)
    print("EXAMPLE 2: Without Customer Name")
    print("=" * 70)
    
    rewriter = LoftMessageRewriter()
    
    raw_input = """Contrato 54321. Aluguéis vencimento 15/03/2025 e 15/04/2025. Valor total: R$ 3.200,00. Valor com desconto: R$ 2.900,00. Desconto de 100% dos juros. Válida hoje."""
    
    output = rewriter.rewrite_message(raw_input)
    
    print("\nENTRADA (Raw):")
    print("-" * 70)
    print(raw_input)
    print("\n")
    print("SAÍDA (Estilo Direto):")
    print("-" * 70)
    print(output)
    print("\n")


def example_3():
    """Example with three months."""
    print("=" * 70)
    print("EXAMPLE 3: Multiple Months (3+)")
    print("=" * 70)
    
    rewriter = LoftMessageRewriter()
    
    raw_input = """Contrato nº 98765. Aluguéis vencimento 10/06/2025, 10/07/2025 e 10/08/2025. Condomínios vencimento 05/06/2025, 05/07/2025 e 05/08/2025. Valor total: R$ 12.500,00. Valor com desconto: R$ 11.000,00. Desconto de 100% dos juros."""
    
    output = rewriter.rewrite_message(raw_input, customer_name="Maria")
    
    print("\nENTRADA (Raw):")
    print("-" * 70)
    print(raw_input)
    print("\n")
    print("SAÍDA (Estilo Direto):")
    print("-" * 70)
    print(output)
    print("\n")


def example_4():
    """Using the rewriter programmatically with custom data."""
    print("=" * 70)
    print("EXAMPLE 4: Programmatic Usage")
    print("=" * 70)
    
    rewriter = LoftMessageRewriter()
    
    # You can also build messages programmatically
    contract = "123456"
    customer = "Carlos"
    dates = ["01/09/2025", "01/10/2025"]
    total = 5000.00
    discount_price = 4500.00
    
    # Build a raw message
    raw_input = f"Contrato nº {contract}. Aluguéis vencimento {dates[0]} e {dates[1]}. Valor total: R$ {total:,.2f}. Valor com desconto: R$ {discount_price:,.2f}. Desconto de 100% dos juros."
    
    output = rewriter.rewrite_message(raw_input, customer_name=customer)
    
    print("\nENTRADA (Raw):")
    print("-" * 70)
    print(raw_input)
    print("\n")
    print("SAÍDA (Estilo Direto):")
    print("-" * 70)
    print(output)
    print("\n")


def main():
    """Run all examples."""
    example_1()
    input("Press Enter to continue to next example...")
    print("\n")
    
    example_2()
    input("Press Enter to continue to next example...")
    print("\n")
    
    example_3()
    input("Press Enter to continue to next example...")
    print("\n")
    
    example_4()
    
    print("=" * 70)
    print("All examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()

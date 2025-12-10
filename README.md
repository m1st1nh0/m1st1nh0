# 👋 Olá, seja bem-vindo(a)! <img src="https://www.codewars.com/users/m1st1nh0/badges/small"/>

Me chamo **Lucas Matheus** e aqui está um pouco sobre mim e minha jornada no mundo da tecnologia 🚀

<img src="https://wordpress-cms-revista-prod-assets.quero.space/legacy_posts/post_images/15721/a3db5ae0d93f3eaf373589f2e21c36e5dade68e6.gif?1551215966" alt="trabalhando com mais afinco camarada" width="300" height="200" align="right"/>

### 🖥️ Sobre mim
- 🎓 Estudante de **Análise e Desenvolvimento de Sistemas** na **Unifatecie**  
- 💡 Apaixonado por **desenvolvimento de software** e suas infinitas possibilidades  
- 🌐 Atualmente explorando tanto **front-end** quanto **back-end**, com experiência em projetos pessoais com foco prático  
- 🔎 Curioso por natureza, sempre buscando aprender novas tecnologias e boas práticas  

---

## 💻 Tecnologias e Conhecimentos

### 💻 Front-end
Experiência prática no desenvolvimento de interfaces e páginas com foco em design responsivo e efeitos visuais:
| **HTML5** <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="20"/> | **CSS3** <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" width="20"/> | **JavaScript** <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg" width="20"/> |
|-----------------|-----------------|-----------------|
| Estruturação semântica de páginas, formulários e boas práticas | Layouts responsivos, animações, Flexbox e Grid | Manipulação de DOM, lógica de programação |

Algum destaque em **projetos práticos** como:
- Accordion FAQ Card com efeitos visuais
- Exercícios de lógica em desafios iniciais

### 👨🏽‍💻 Back-end & Programação
Exploração inicial e sólidos fundamentos, focando em Python e Java:
| **Python** <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="25"/> | **Java** <img src="https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg" width="20"/> |
|-----------------|-----------------|
| Manipulação de dados, bibliotecas como Pandas, Selenium e automações básicas | Princípios fundamentais aprendidos durante curso básico |

🎨 Além disso:
- Experiência prática com projetos de controle de finanças e lógica
- Interesse em frameworks e APIs como React e Django para expandir habilidades

---

## 📈 Objetivos
- Aprimorar minhas habilidades em **frameworks modernos e APIs** (React, Node.js, Django, Angular, etc.)  
- Construir mais projetos práticos para compor meu **portfólio**  
- Contribuir com a comunidade open-source e aprender colaborativamente por meio de desafios reais  
  

---

## 📫 Contato
- 💼 [LinkedIn](https://www.linkedin.com/in/lucas-schamposki/)  
- 📧 **lukaschamposki@gmail.com**  

---

## 🚀 Projeto: Loft WhatsApp Message Rewriter

### Sobre o Projeto
Sistema de reescrita de mensagens de cobrança para WhatsApp que transforma textos técnicos e burocráticos em mensagens diretas, amigáveis e focadas na solução (desconto) ao invés do problema (dívida).

### Funcionalidades
- ✅ Conversão de mensagens técnicas para o "Estilo Direto"
- ✅ Formatação automática de datas (DD/MM/YYYY → Mês/Ano)
- ✅ Agrupamento inteligente de meses
- ✅ Destaque visual em valores monetários
- ✅ Foco no desconto oferecido
- ✅ Call-to-action simples e direto

### Como Usar

#### Instalação
```bash
# Clone o repositório
git clone https://github.com/m1st1nh0/m1st1nh0.git
cd m1st1nh0

# Não há dependências externas! Apenas Python 3.6+
```

#### Uso Básico
```python
from loft_message_rewriter import LoftMessageRewriter

# Criar instância do rewriter
rewriter = LoftMessageRewriter()

# Mensagem técnica original
raw_message = """Contrato nº 1681933. Identificamos que a imobiliária apontou valores pendentes, mas já foram pagos por nós, como fiadores. Aluguéis vencimento 21/07/2025 e 20/08/2025. Condomínios vencimento 12/07/2025 e 12/08/2025. Valor total: R$ 7.450,85. Quero te apresentar nossa opção com desconto de 100% dos juros. Valor com desconto: R$ 6.622,10. Economia: R$ 828,75. Válida somente hoje."""

# Transformar para estilo direto
output = rewriter.rewrite_message(raw_message, customer_name="Juraci")
print(output)
```

#### Resultado
```
Oi, Juraci! Tudo bem?

Sobre o contrato 1681933, regularizamos os Aluguéis e Condomínios de Jul e Ago/25 junto à imobiliária.

Para quitarmos isso hoje, consegui isentar 100% dos juros da Loft:

De: *R$ 7.450,85*
Por: *R$ 6.622,10* *(Válido só hoje)*

É uma economia de R$ 829,00. Posso gerar o boleto com esse desconto para você?
```

#### Exemplos
```bash
# Executar o exemplo principal
python3 loft_message_rewriter.py

# Executar exemplos interativos
python3 example_usage.py

# Executar testes
python3 -m unittest test_loft_message_rewriter.py -v
```

### Diretrizes do "Estilo Direto"
1. **Humanização Imediata**: Saudação curta e personalizada
2. **Zero "Juridiquês"**: Linguagem simples e direta
3. **Resumo Inteligente**: Datas no formato Mês/Ano, agrupamento de itens
4. **Destaque Visual**: Negrito em valores e prazos
5. **Foco no Benefício**: Desconto em evidência
6. **CTA Simples**: Pergunta direta que exige resposta simples

### Estrutura dos Arquivos
- `loft_message_rewriter.py` - Módulo principal com a classe `LoftMessageRewriter`
- `test_loft_message_rewriter.py` - Testes unitários completos
- `example_usage.py` - Exemplos de uso do sistema

---

# Bem vindo ao berrycheck

# Descrição
Pacote python de cotacao de moedas e de acoes das principais empresas brasileiras. <br>
Acesse: https://github.com/eduardosousaa/berrycheck

# Objetivos
* Fornecer aos usuários uma maneira fácil e acessível de obter cotações atualizadas de várias moedas, incluindo as principais moedas do mundo, para fins de negociação, investimento ou outras finalidades financeiras. <br>
* Oferecer um pacote fácil de usar e bem documentada que permite aos usuários integrar facilmente as cotações de moedas em seus próprios projetos e aplicativos. <br>
* Permitir que os usuários calculem rapidamente o valor de uma moeda em relação a outra com base nas cotações mais recentes, facilitando a conversão de moedas para fins de viagens, compras internacionais ou outras necessidades pessoais ou comerciais. <br>
* Fornecer ações atualizadas das principais empresas brasileiras. <br>
* Permite também o calculo de ações das empresas. <br>

# Funcionalidades
* Obter cotações de várias moedas em tempo real. <br>
* Converter valores entre diferentes moedas. <br>
* Obtém os valores das ações de uma lista de empresas. <br>
* Calcula o valor total de ações de uma empresa. <br>

# Como usar
Siga os passos a seguir

## Instale o pacote <br>
```python
    pip install berrycheck
```

## Importar a biblioteca <br>
```python
    from berry_check import BerryCheck
```

## Criar um objeto da classe <br>
```python
    x = BerryCheck()  
```

## Obter cotação das moedas <br>
```python
    cotacao_dolar = x.obtem_cotacao("USD", "BRL")["cotacao"]
    cotacao_euro = x.obtem_cotacao("EUR", "BRL")["cotacao"]
    cotacao_libra = x.obtem_cotacao("GBP", "BRL")["cotacao"] 
```

## Obter cotação, máxima, mínima e variação <br>
```python
    cotacao = x.obtem_cotacao("USD", "BRL")

    print("Cotação:", cotacao["cotacao"])
    print("Máximo:", cotacao["maximo"])
    print("Mínimo:", cotacao["minimo"])
    print("Variação:", cotacao["variacao"])
```

## Converter moedas <br>
```python
    valor_em_reais = x.converte_moeda('USD', 'BRL', 100)
```

# Códigos das moedas <br>
Veja a lista completa de combinações em: https://economia.awesomeapi.com.br/xml/available
Veja a lista de nomes das moedas em: https://economia.awesomeapi.com.br/xml/available/uniq

## Obter valores de ações das empresas <br>
```python
    valores_acoes = x.obter_valores_acoes(["VALE3.SAO", "PETR4.SAO"])
```

## Calcular valor das ações <br>
```python
    valor_vale = x.calcular_valor_acoes("VALE3.SAO", 1, valores_acoes)
    valor_petro = x.calcular_valor_acoes("PETR4.SAO", 1, valores_acoes)
```

# Lista de empresas brasileiras para procurar ações 
* Petrobras: PETR4.SAO <br>
* Vale: VALE3.SAO <br>
* Itaú Unibanco: ITUB4.SAO <br>
* Bradesco: BBDC4.SAO <br>
* Banco do Brasil: BBAS3.SAO <br>
* Ambev: ABEV3.SAO <br>
* Magazine Luiza: MGLU3.SAO <br>
* Natura: NATU3.SAO <br>
* B3: B3SA3.SAO <br>
* Gerdau: GGBR4.SAO <br>




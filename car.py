kilometer = float(input('Digite quantos KM você irá percorrer: '))
price_gas = float(input('Digite o preço da gasolina na sua região: R$'))

cars_consumption = [5, 6, 7, 8, 9, 10, 11, 12, 13]


for i in range(9):
    total = (kilometer/cars_consumption[i])*price_gas
    print(f'Se seu carro tem a autonomia de {cars_consumption[i]}km por litro, você vai gastar R${total:.2f}')
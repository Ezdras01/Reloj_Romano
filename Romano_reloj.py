import time

# Esta función convierte un número decimal a un número romano
def decimal_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    # Aquí estamos convirtiendo el número a romano
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Esta función obtiene la hora actual y la muestra en números romanos
def get_time_in_roman():
    while True:
        # Obtenemos la hora actual
        current_time = time.strftime("%H:%M:%S")
        
        # Separamos la hora, los minutos y los segundos
        h, m, s = current_time.split(':')
        
        # Convertimos la hora, los minutos y los segundos a números romanos
        roman_hour = decimal_to_roman(int(h))
        roman_minute = decimal_to_roman(int(m))
        roman_second = decimal_to_roman(int(s))
        
        # Limpiamos la consola (para sistemas Unix)
        print("\033c", end="")
        
        # Mostramos la hora en formato original y en números romanos
        print("Hora actual en formato original:", current_time)
        print(f"Hora actual en números romanos: {roman_hour}:{roman_minute}:{roman_second}")
        
        # Pausa el programa por 1 segundo
        time.sleep(1)

# Llamamos a la función para mostrar la hora en tiempo real
get_time_in_roman()

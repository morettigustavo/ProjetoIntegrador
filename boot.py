import network
import machine

# Configurar os pinos do sensor TCS3200
s2 = machine.Pin(4, machine.Pin.OUT)
s3 = machine.Pin(5, machine.Pin.OUT)
out = machine.Pin(14, machine.Pin.IN)

# Configurar as frequências de amostragem
s2.value(1)
s3.value(1)

def Connect():
    # Conectar-se à rede Wi-Fi
    ssid = 'Desktop_F7A28197'
    password = '0120301130085879'
    sta_if = network.WLAN(network.STA_IF)    
    sta_if.active(True)
    sta_if.connect(ssid, password)
    
    # Aguardar a conexão com a rede Wi-Fi
    while not sta_if.isconnected():
        pass
    
    # Imprimir o endereço IP atribuído ao ESP32
    print('Endereço IP:', sta_if.ifconfig()[0])

def read_rgb():
    # Configurar os filtros do sensor para a cor vermelha
    s2.value(0)
    s3.value(0)
    # Contar o tempo de pulso do pino de saída para obter a intensidade da cor vermelha
    red = machine.time_pulse_us(out, 1)

    # Configurar os filtros do sensor para a cor verde
    s2.value(1)
    s3.value(1)
    # Contar o tempo de pulso do pino de saída para obter a intensidade da cor verde
    green = machine.time_pulse_us(out, 1)

    # Configurar os filtros do sensor para a cor azul
    s2.value(0)
    s3.value(1)
    # Contar o tempo de pulso do pino de saída para obter a intensidade da cor azul
    blue = machine.time_pulse_us(out, 1)

    return red, green, blue

def convert_to_rgb(red, green, blue):
    # Calcular os valores normalizados usando uma regra de proporção
    red_normalized = int(red * 255 / (red + green + blue))
    green_normalized = int(green * 255 / (red + green + blue))
    blue_normalized = int(blue * 255 / (red + green + blue))

    return red_normalized, green_normalized, blue_normalized

def Read():
    # Ler as cores RGB
    red_value, green_value, blue_value = read_rgb()

    # Converter para valores RGB normalizados
    red_normalized, green_normalized, blue_normalized = convert_to_rgb(red_value, green_value, blue_value)

    # Imprimir os valores RGB normalizados
    print("Vermelho (RGB):", red_normalized)
    print("Verde (RGB):", green_normalized)
    print("Azul (RGB):", blue_normalized)



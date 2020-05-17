# main.py
from button import Button
from led import Led
from utime import ticks_ms, sleep_ms, ticks_diff

def change_leds(led1, led2): 
    # Muda o estado de dois LEDs
    led1.state(not led1.state())
    led2.state(not led2.state())

def intermitente():
    # Função para o estado amarelo intermitente
    green.state(False)
    red.state(False)
    sleep_ms(200) # Anti-bouncing 
    
    while True:
        yellow.blink(blink_duration) # Ver função de classe LED

        if bi.state() == 1:
            yellow.state(False)
            sleep_ms(500) # Anti-bouncing
            break      

# Botões
bi = Button(23) # Botão direito / foto
bp = Button(18) # Botão esquerdo / foto

# LEDs
green = Led(19)
yellow = Led(22)
red = Led(21)

# Valores default
green_default_duration = 9000
yellow_duration = 1000
red_duration = 5000
blink_duration = 1000
min_time_peao = 4000

# Init valores
green.state(True)
green_time_init = ticks_ms()
green_limit = green_default_duration

while True:
    if green.state() == 1: 
    # Calcula o tempo de espera do green LED; green_default_duration / min_time_peao / 0, confrome o caso    
        if bp.state() == 1:
            if ticks_diff(ticks_ms(), green_time_init) <= min_time_peao:
                green_limit = min_time_peao
            else:
                green_limit = 0

        if ticks_diff(ticks_ms(), green_time_init) > green_limit: 
        # Se o tempo de verde expirou passa a amarelo.
            change_leds(green, yellow)
            yellow_time_init = ticks_ms()
            green_limit = green_default_duration

    if yellow.state() == 1:
        # Se o tempo de amarelo expirou, passa a vermelho
        if ticks_diff(ticks_ms(), yellow_time_init) > yellow_duration:
            change_leds(yellow, red)
            red_time_init = ticks_ms()  
    
    if red.state() == 1:
        # Se o tempo de vermelho expirou, passa a verde
        if ticks_diff(ticks_ms(), red_time_init) > red_duration:
            change_leds(red, green)
            green_time_init = ticks_ms()
    
    if bi.state() == 1:
        # Activação da tecla bi acciona o modo intermitente, desabilitando qualquer outra função.
        intermitente()
        # Após desactivaçao do modo intermitente, inicialização do funcionamento normal do semáforo.
        green.state(True)
        green_limit = green_default_duration
        green_time_init = ticks_ms()

    

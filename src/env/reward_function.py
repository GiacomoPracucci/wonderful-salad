import numpy as np

'''``` ```
    Irrigazione: L'insalata richiede un'irrigazione costante per mantenere il terreno umido 
    ma non allagato. Si consiglia di innaffiare regolarmente, preferibilmente al mattino o alla sera, 
    evitando le ore più calde della giornata​​. Inoltre, l'insalata richiede irrigazioni abbastanza 
    frequenti, specialmente in piena estate, ma più diradate rispetto alla lattuga. 
    Il terreno si dovrà asciugare in superficie prima di un nuovo intervento di irrigazione​​.

    Luce: L'insalata riccia necessita di almeno 4-5 ore di luce diretta al giorno​​. Questo significa 
    che in un ambiente controllato, come una serra, l'agente deve garantire che l'insalata riceva 
    una quantità adeguata di luce naturale o, se necessario, luce artificiale.

    Temperatura: Le condizioni di sviluppo ottimali per l'insalata si trovano tra i 15 e i 20 gradi Celsius. 
    La crescita si arresta al di sotto dei 6 gradi, e temperature di 3-5 gradi o superiori ai 30 gradi possono indurre la pre-fioritura​​.


    Sulla base di queste informazioni, il sistema di ricompensa può essere strutturato per premiare comportamenti 
    che mantengono questi parametri ottimali:

    Irrigazione: Premiare l'agente quando mantiene un livello ottimale di umidità nel terreno, 
    evitando sia l'aridità che l'eccesso di acqua. Potresti considerare una ricompensa più alta per l'irrigazione durante le prime ore del mattino o la sera.

    Luce: Assegnare una ricompensa se l'agente assicura che le piante ricevano una quantità adeguata di luce, 
    sia naturale che artificiale, specialmente durante le ore in cui la luce solare non è sufficiente.

    Temperatura: Dare una ricompensa quando l'agente mantiene la temperatura nell'intervallo ottimale di 15-20 gradi Celsius, 
    penalizzando le deviazioni significative da questo range.
'''

def reward_function(state, action):
    # estrai i valori dallo stato
    solar_light = state['solar_light'][0]
    soil_moisture = state['soil_moisture'][0]
    temperature = state['temperature'][0]
    
    # estrai i valori dell'azione
    irrigation_amount, temp_adjustment, light_adjustment = action
    reward =0
    
    # ricompensa per mantenere l'umidità del terreno ottimale
    if 0.4 <= soil_moisture <= 0.7:  # Assumiamo che questi siano i valori ottimali di umidità
        reward += 1
    else:                   
        reward -=1  # Penalità per terreno troppo secco o troppo umido
        
    # Ricompensa per mantenere la temperatura ottimale
    if 15 <= temperature <= 20:
        reward += 1
    else:
        reward -= -1
        
    # Ricompensa per assicurare una quantità adeguata di luce
    if solar_light < 0.5 and light_adjustment > 0:  # Aumento della luce artificiale quando la luce naturale è bassa
        reward += 0.5
        
    return reward
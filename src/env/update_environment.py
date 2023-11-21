import numpy as np

def _update_environment(self, action):
    # Estrai i componenti dell'azione
    irrigation_amount, temp_adjustment, light_adjustment = action

    # Aggiorna il tempo
    new_time = (self.time + 1) % 1440  # Ogni passo è un minuto

    # Se l'agente decide di irrigare, aggiorna l'ultimo momento di irrigazione
    if irrigation_amount > 0:
        last_irrigation_time = new_time

    # Simula la luce solare
    new_solar_light = simulate_solar_light(new_time)
    
    # Aggiorna la luce artificiale
    new_artificial_light = min(1, max(0, self.artificial_light + light_adjustment / 100))  # Assicurati che sia tra 0 e 1

    # Aggiorna l'umidità del terreno considerando la luce solare e artificiale
    new_soil_moisture = simulate_soil_moisture(new_time, last_irrigation_time, new_solar_light + new_artificial_light, self.temperature)

    # Simula la temperatura (aggiustando la temperatura in base all'azione dell'agente)
    new_temperature = simulate_temperature(new_time, temp_adjustment)

    return new_time, new_solar_light, new_artificial_light, new_soil_moisture, new_temperature

def simulate_solar_light(time):
    # Assicurati che la luce solare sia sempre positiva e tra 0 e 1
    return (np.sin(np.pi * time / 720) + 1) / 2  # Oscilla tra 0 e 1

def simulate_soil_moisture(time, last_irrigation_time, irrigation_amount, solar_light, temperature, soil_moisture):
    time_since_irrigation = time - last_irrigation_time
    drying_factor = solar_light * (temperature / 25)
    # Modifica la velocità di asciugatura e l'effetto dell'irrigazione
    moisture_loss_rate = 0.005 * time_since_irrigation * drying_factor
    moisture_gain = 0.2 if irrigation_amount > 0 else 0  # Aggiungi un aumento significativo di umidità se irrigato
    new_soil_moisture = max(0, min(1, soil_moisture - moisture_loss_rate + moisture_gain))
    return new_soil_moisture

def simulate_temperature(time, temp_adjustment):
    base_temp = 15 + 10 * np.sin(np.pi * time / 720) + temp_adjustment
    return min(25, max(5, base_temp + np.random.normal(0, 0.5)))


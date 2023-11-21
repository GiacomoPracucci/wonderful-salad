import numpy as np

def _update_environment(self, action):
    # Estrai i componenti dell'azione
    irrigation_amount, temp_adjustment, light_adjustment = action

    # Aggiorna il tempo
    new_time = (self.time + 1) % 1440  # Ogni passo è un minuto

    # Se l'agente decide di irrigare, aggiorna l'ultimo momento di irrigazione
    if irrigation_amount > 0:
        self.last_irrigation_time = new_time

    # Simula la luce solare
    new_solar_light = self.simulate_solar_light(new_time)

    # Simula l'umidità del terreno
    new_soil_moisture = self.simulate_soil_moisture(new_time, self.last_irrigation_time, new_solar_light, self.temperature)

    # Simula la temperatura (aggiustando la temperatura in base all'azione dell'agente)
    new_temperature = self.simulate_temperature(new_time, temp_adjustment)

    return new_time, new_solar_light, new_soil_moisture, new_temperature

def simulate_solar_light(self, time):
    # Simula la luce solare (valore tra 0 e 1)
    return np.sin(np.pi * time / 720)

def simulate_soil_moisture(self, time, last_irrigation_time, solar_light, temperature):
    # Calcola l'umidità del terreno basandosi sull'ultima irrigazione, luce solare e temperatura
    time_since_irrigation = time - last_irrigation_time
    drying_factor = solar_light * (temperature / 25)
    return max(0, 1 - 0.001 * time_since_irrigation * drying_factor)  # Esempio di funzione di asciugatura

def simulate_temperature(self, time):
    # Simula la temperatura (valore tra 5 e 25 gradi)
    base_temp = 15 + 10 * np.sin(np.pi * time / 720)  # Temperatura di base variabile
    # Aggiungi un po' di rumore casuale per rendere la simulazione più realistica
    return min(25, max(5, base_temp + np.random.normal(0, 0.5)))


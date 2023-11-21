## Script 1 - Classe dell'Ambiente:
Definisce l'ambiente SaladGreenHouse.
- Specifica gli spazi delle azioni e delle osservazioni.
- Include i metodi reset, step, render, close, e seed.
- Nel metodo step, utilizza la funzione _update_environment per aggiornare l'ambiente e reward_function per calcolare la ricompensa.

## Script 2 - Funzioni di Aggiornamento e Simulazione:
- Contiene la funzione _update_environment che gestisce l'aggiornamento delle variabili ambientali.
- Include funzioni ausiliarie (simulate_solar_light, simulate_soil_moisture, simulate_temperature) per simulare le condizioni della serra.

## Script 3 - Funzione di Ricompensa:
- Definisce reward_function che calcola la ricompensa in base allo stato attuale e all'azione intrapresa.
- Assegna ricompense o penalità in base a come l'agente gestisce l'umidità del terreno, la temperatura, e la luce.
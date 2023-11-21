import sys
#sys.path.append('C:/Users/giaco/Desktop/repos/wonderful-salad/src')
sys.path.append('/home/giacomo/Documents/GitHub/wonderful-salad/src')
from env.greenhouse import SaladGreenHouse

env = SaladGreenHouse()
state = env.reset()

# esegui una giornata di simulazione
for _ in range(1440):
    action = env.action_space.sample()
    
    state, reward, truncated, terminated, info = env.step(action)
    
    print(f"Time: {state['time']}, Solar Light: {state['solar_light']}, Artificial Light: {state['artificial_light']}, Soil Moisture: {state['soil_moisture']}, Temperature: {state['temperature']}")
    
    if terminated:
        break
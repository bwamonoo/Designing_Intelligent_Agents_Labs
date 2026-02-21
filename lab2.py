import asyncio
import random
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

class EnvironmentSensorBehaviour(PeriodicBehaviour):
    async def run(self):
        event_types = ["Flooding", "Fire", "Earthquake", "Landslide"]
        severity_levels = ["Low", "Medium", "High", "Critical"]
        
        current_event = random.choice(event_types)
        current_severity = random.choice(severity_levels)
        
        print(f"[LOG] {current_event} detected with {current_severity} severity.")
        
        if current_severity in ["High", "Critical"]:
            print(f"--- ALERT: Immediate response required for {current_event}! ---")

class SensorAgent(Agent):
    async def setup(self):
        print("SensorAgent initialized. Monitoring disaster environment...")
        self.add_behaviour(EnvironmentSensorBehaviour(period=3))

async def main():
    jid = "bwamonoo_student@xmpp.jp"
    password = "Q86QY4Xni@AbtBf"
    
    sensor_agent = SensorAgent(jid, password)
    print("Connecting Sensor Agent...")
    await sensor_agent.start()
    
    print("Agent is running. Collecting data for 15 seconds...")
    await asyncio.sleep(15)
    
    await sensor_agent.stop()
    print("Agent stopped.")

if __name__ == "__main__":
    asyncio.run(main())
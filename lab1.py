import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class GreetingBehaviour(OneShotBehaviour):
    async def run(self):
        print(f"Success! Agent {self.agent.jid} is connected to the remote server.")
        await self.agent.stop()

class Lab1Agent(Agent):
    async def setup(self):
        self.add_behaviour(GreetingBehaviour())

async def main():
    jid = "bwamonoo_student@xmpp.jp"
    password = "Q86QY4Xni@AbtBf"

    agent = Lab1Agent(jid, password)
    
    try:
        await agent.start()
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    while agent.is_alive():
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            await agent.stop()
            break

if __name__ == "__main__":
    asyncio.run(main())
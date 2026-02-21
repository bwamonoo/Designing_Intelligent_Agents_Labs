import asyncio
import random
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State

# State Names
STATE_MONITOR = "IDLE_MONITOR"
STATE_REPLENISH = "REPLENISHING"
STATE_DISPATCH = "DISPATCHING"

class LogisticsLogic(FSMBehaviour):
    async def on_start(self):
        print(f"LogisticsAgent: Starting FSM logic.")

class IdleMonitorState(State):
    async def run(self):
        print("\n[STATE: IDLE_MONITOR] Checking inventory...")
        await asyncio.sleep(2)
        
        # Simulate Percepts/Events
        stock_level = random.randint(10, 100)
        request_received = random.choice([True, False, False, False]) # 25% chance

        if stock_level < 20:
            print(f"LogisticsAgent: ALERT - Low Stock Detected ({stock_level}%).")
            self.set_next_state(STATE_REPLENISH)
        elif request_received:
            print("LogisticsAgent: Incoming supply request from Field Unit.")
            self.set_next_state(STATE_DISPATCH)
        else:
            self.set_next_state(STATE_MONITOR)

class ReplenishState(State):
    async def run(self):
        print("[STATE: REPLENISHING] Contacting suppliers for emergency restock...")
        await asyncio.sleep(3)
        print("LogisticsAgent: Inventory replenished to 100%.")
        self.set_next_state(STATE_MONITOR)

class DispatchState(State):
    async def run(self):
        print("[STATE: DISPATCHING] Loading relief crates onto transport...")
        await asyncio.sleep(3)
        print("LogisticsAgent: Supplies dispatched to Sector A.")
        self.set_next_state(STATE_MONITOR)

class LogisticsAgent(Agent):
    async def setup(self):
        fsm = LogisticsLogic()
        
        # Adding States
        fsm.add_state(name=STATE_MONITOR, state=IdleMonitorState(), initial=True)
        fsm.add_state(name=STATE_REPLENISH, state=ReplenishState())
        fsm.add_state(name=STATE_DISPATCH, state=DispatchState())
        
        # Adding Transitions
        fsm.add_transition(source=STATE_MONITOR, dest=STATE_REPLENISH)
        fsm.add_transition(source=STATE_MONITOR, dest=STATE_DISPATCH)
        fsm.add_transition(source=STATE_REPLENISH, dest=STATE_MONITOR)
        fsm.add_transition(source=STATE_DISPATCH, dest=STATE_MONITOR)
        fsm.add_transition(source=STATE_MONITOR, dest=STATE_MONITOR)

        self.add_behaviour(fsm)

async def main():
    # Update with your personal JID and Password
    agent = LogisticsAgent("bwamonoo_student@xmpp.jp", "Q86QY4Xni@AbtBf")
    await agent.start()
    
    # Run for 20 seconds to observe state changes
    await asyncio.sleep(20)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())
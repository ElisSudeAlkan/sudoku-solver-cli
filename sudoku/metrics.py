import time

START_TS = None
BACKTRACK_STEPS = 0
NODES = 0

def start():
    global START_TS
    START_TS = time.time()

def inc_backtrack():
    global BACKTRACK_STEPS
    BACKTRACK_STEPS += 1

def inc_nodes():
    global NODES
    NODES += 1

def snapshot():
    now = time.time()
    return {
        "elapsed_ms": int((now - (START_TS or now)) * 1000),
        "backtracks": BACKTRACK_STEPS,
        "nodes": NODES,
    }

def reset():
    global START_TS, BACKTRACK_STEPS, NODES
    START_TS = None
    BACKTRACK_STEPS = 0
    NODES = 0
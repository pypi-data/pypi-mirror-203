from startstop import p, pc, t, tc


def your_code():
    for i in range(100000):
        i**2


# Profiler
p()
your_code()
p()


# Profiler as contex manager
with pc():
    your_code()


# Profiler as contex manager with config
with pc(interval=0.002, async_mode="enabled"):
    your_code()


# Simple timer
t()
your_code()
t()
# ... TIMER: 0.024 sec


# Simple timer with label and precision config
t(label="your label", precision=2)
your_code()
t()
# ... TIMER your label: 0.02 sec


# Simple timer as contex manager
with tc():
    your_code()
# ... TIMER: 0.024 sec


# Simple timer as contex manager label and precision config
with tc(label="your label", precision=2):
    your_code()
# ... TIMER your label: 0.02 sec

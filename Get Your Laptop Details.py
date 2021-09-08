# Required Module:- pip install platform

import platform

my_system = platform.uname()

print(f"System: {my_system.system}")

print(f"Node Name: {my_system.node}")

print(f"Release: {my_system.release}")

print(f"Version: {my_system.version}")

print(f"Machine: {my_system.machine}")

print(f"Processor: {my_system.processor}")


# OUTPUT:-
# System: Windows
# Node Name: SHUBHAM-SAINI
# Release: 10
# Version: 10.0.17763
# Machine: AMD64
# Processor: Intel64 Family 6 Model 42 Stepping 7, GenuineIntel
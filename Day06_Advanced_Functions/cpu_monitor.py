# CPU Monitoring Example

cpu_usage = [45, 50, 60, 55, 70, 40]

high_cpu = [
    x
    for x in cpu_usage
    if x > 50
]

print("High CPU Usage Values:")
print(high_cpu)
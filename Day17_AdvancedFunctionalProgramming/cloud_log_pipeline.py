logs = [

    "INFO Server Started",

    "ERROR Database Down",

    "INFO Request Received",

    "ERROR Timeout",

    "WARNING High CPU Usage"

]

errors = filter(

    lambda log:

    "ERROR" in log,

    logs

)

for log in errors:

    print(log)
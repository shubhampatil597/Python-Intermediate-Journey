logs = [

    "INFO Server Started",

    "ERROR Database Down",

    "INFO Request Received",

    "ERROR Timeout",

    "WARNING High CPU Usage"

]

processed_logs = map(

    lambda log:

    log.upper(),

    logs

)

error_logs = filter(

    lambda log:

    "ERROR" in log,

    processed_logs

)

for log in error_logs:

    print(log)
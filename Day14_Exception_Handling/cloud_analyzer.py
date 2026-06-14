try:

    with open(
        "server_logs.txt",
        "r"
    ) as file:

        logs = file.readlines()

        print(
            "Total Logs:",
            len(logs)
        )

except FileNotFoundError:

    print(
        "Log File Not Found"
    )

finally:

    print(
        "Analysis Completed"
    )
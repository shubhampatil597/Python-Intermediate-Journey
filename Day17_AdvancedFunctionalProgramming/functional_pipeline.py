numbers = range(20)

result = map(

    lambda x: x * 2,

    numbers

)

result = filter(

    lambda x: x > 20,

    result

)

print(

    list(result)

)
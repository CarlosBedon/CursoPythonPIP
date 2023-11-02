import mod
data = [
    {
        'Country':'Colombia',
        "Population":500
    },
    {
        'Country':'Ecuador',
        "Population":200
    }
]
def run():
    keys, values = mod.get_popullation()
    print (keys,values)

    country = input('Insert country name')

    result = mod.popullation_by_country(data,country)
    print(result)

if __name__ == '__main__':
    run()
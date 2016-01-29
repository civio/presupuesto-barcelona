
def main():
    with open("./gastos.csv", 'r') as data:
        presupuestos = {2011:[],2012:[],2013:[],2014:[],2015:[],2016:[]}
        lines = data.readlines()[2:]
        regex = r'^(?P<economic>\d+),(?P<organic>\d+),(?P<functional>\d+),(?P<subprogram>.+),(?P<initial_budget>\d+(.\d+)?),(?P<eventual_budget>\d*(.\d+)?),(?P<obligat>\d*(.\d+)?),(?P<year>\d{4})$'
        for line in lines:

            pack = create_pack(fields)
            try:
                presupuestos[int(fields[7])].append(pack)
            except:
                print(fields)
                print(fields[7])
        #print(presupuestos)

def create_pack(fields):
    return {
        'economic': fields[0].zfill(5),
        'organic': fields[1].zfill(3),
        'functional': fields[2].zfill(5),
        'budget': fields[4]
    }

if __name__ == "__main__":
    main()

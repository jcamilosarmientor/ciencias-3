import lexer_v2

EXPRESIONS_FILE = "expresiones_v2.in"
RESULT_FILE = "expresiones_v2.out"

def readFile():
    file = open(EXPRESIONS_FILE, "r")
    filas = (file.read().splitlines())
    clearFile(RESULT_FILE)
    for exp in filas:
        result = lexer_v2.t_okens(exp)
        writeFile(result)
        lexer_v2.lista = []

    file.close()

def writeFile(result):
    file = open(RESULT_FILE, "a")
    file.write(str(result)+'\n')
    file.close()

def clearFile(file):
    file = open(file, "w").close()

def run():
    readFile()

if __name__ == "__main__":
    run()

import lexer

EXPRESIONS_FILE = "expresiones.in"
RESULT_FILE = "expresiones.out"

def readFile():
    file = open(EXPRESIONS_FILE, "r")
    filas = (file.read().splitlines())
    clearFile(RESULT_FILE)
    for exp in filas:
        result = lexer.tokens(exp)
        writeFile(result)
        lexer.lista = []
        print(exp)

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

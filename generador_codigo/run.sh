#!/bin/sh

#colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

function printOut () {
    if [ "$3" == "" ]
    then
        echo -e "${2}${1}${NC}"
    else 
        echo -e "${2}${3}: ${1}${NC}"
    fi
}

function create_workspace () {
    rm -rf workspace/src
    rm -rf workspace/public
    cp -v srcgen/package.json workspace
    mkdir workspace/src
    mkdir workspace/public
    mkdir mongo_data
    mkdir workspace/api
    printOut 'Directorio de trabajo creado' $GREEN   
}

function download_dependences () {
    printOut ' ~ Copiando package.json' $BOLD
    cp -v srcgen/package.json workspace
    printOut ' ~ Descargando dependencias...' $BOLD
    cd workspace
    npm install
    npm install bootstrap --save
    npm install react-router-dom --save
    cd ..
}

# Inicio de ejecución
printOut ' ~ Generando código...' $BOLD
python entity_codegen.py
printOut 'Genración finalizada' $GREEN


printOut ' ~ Creando directorio de trabajo...' $BOLD
if [ -d workspace ] && [ -d workspace/node_modules ]
then # workspace existe 
    printOut 'Ya existe el directorio workspace' $RED 'ERROR'
    printOut '¿Volver a crear el directorio workspace? S/N' $YELLOW 'WARNING'
    read answer
    if [ $answer = "S" ] || [ $answer = "s" ]
    then
        create_workspace
    fi

    printOut '¿Volver a descargar las dependencias de este proyecto? S/N' $YELLOW 'WARNING'
    read answer
    if [ $answer = "S" ] || [ $answer = "s" ]
    then
        download_dependences
    fi

else # workspace no existe
    mkdir workspace
    create_workspace
    download_dependences
fi

printOut ' ~ Copiando ficheros javascript generados...' $BOLD
cp -v srcgen/*.js workspace/src
cp -v srcgen/api/*.js workspace/api
printOut ' ~ Copiando index.html...' $BOLD
cp -v srcgen/index.html workspace/public
printOut ' ~ Copiando estilos...' $BOLD
cp -v srcgen/*.css workspace/src

# Creando contenedores
printOut ' ~ Iniciando compose...' $BOLD
docker-compose build

# Levantando contenedores
docker-compose up -d



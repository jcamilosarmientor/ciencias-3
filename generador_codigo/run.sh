#!/bin/sh

#colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

function printOut () {
    if [ "$3" == "" ]
    then
        echo "${2}${1}${NC}"
    else 
        echo "${2}${3}: ${1}${NC}"
    fi
}

function create_workspace () {
    rm -rf workspace
    mkdir workspace
    mkdir workspace/src
    mkdir workspace/public
    printOut 'Directorio de trabajo creado' $GREEN   
}

function download_dependences () {
    echo ' ~ Descargando dependencias...'
    cd workspace
    npm install
    npm --save install bootstrap
    printOut 'Dependencias descargadas ' $GREEN 
    cd ..
}

# Inicio de ejecución
echo ' ~ Generando código...'
python entity_codegen.py
printOut 'Genración finalizada' $GREEN

echo ' ~ Creando directorio de trabajo...'
if [ -d workspace ] && [ -d workspace/node_modules ]
then # workspace existe 
    printOut 'Ya existe el directorio workspace' $RED 'ERROR'
    printOut '¿Volver a crear el directorio workspace? S/N' $YELLOW 'WARNING'
    read answer
    if [ $answer = "S" ] || [ $answer = "s" ]
    then
        create_workspace
        printOut 'Directorio de trabajo creado' $GREEN
    fi

    printOut '¿Volver a descargar las dependencias de este proyecto? S/N' $YELLOW 'WARNING'
    read answer
    if [ $answer = "S" ] || [ $answer = "s" ]
    then
        download_dependences
    fi

else # workspace no existe
    create_workspace
    download_dependences
fi

echo ' ~ Copiando ficheros javascript generados...'
cp -v srcgen/*.js workspace/src
echo ' ~ Copiando index.html...'
cp -v srcgen/index.html workspace/public
echo ' ~ Copiando estilos...'
cp -v srcgen/*.css workspace/src
echo ' ~ Copiando package.json'
cp -v srcgen/package.json workspace

#Iniciando servidor
cd workspace
npm start 
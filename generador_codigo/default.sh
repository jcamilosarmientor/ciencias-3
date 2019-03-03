echo 'Detiendo contenedores...'
docker-compose down
echo 'Eliminando carpetas...'
rm -rf srcgen
rm -rf workspace/src workspace/public
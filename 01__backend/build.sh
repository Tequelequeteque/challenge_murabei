cp -r ../00__database .
docker compose up -d --force-recreate --build
rm -rf 00__database
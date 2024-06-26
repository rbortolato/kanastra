dcup:
	docker compose up -d && ${MAKE} dclogs
dcstop:
	docker compose stop
dclogs:
	docker compose logs -f
dcbash:
	docker compose exec -it api bash
dcrm:
	docker compose rm -f -s api
make dcrs:
	${MAKE} dcstop && ${MAKE} dcrm && ${MAKE} dcup
dprune:
	docker system prune -a -f
tests:
	docker compose exec -it api bash -c 'pytest -s'

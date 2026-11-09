# # Docker Notes
#
# # What Docker does
# Packs an app together with its environment into an image, so it runs the same anywhere.
#
# # Running someone else's project
# 1. Look for `docker-compose.yml` in the project root
# 2. `cd` into it and run `docker compose up -d`
# 3. Check status with `docker compose ps`
# 4. Open the port listed in the README
# 5. Stop it with `docker compose down`
#
# # Modifying someone else's code
# 1. Read the source files directly — no need to run first
# 2. Change something small first to verify the pipeline works
# 3. Rebuild with `docker compose down && docker compose up -d --build`; add `--no-cache` if cached
# 4. Debug with `docker compose logs`
#
# # Pitfalls I hit
# - Image pulls fail in China: add `registry-mirrors` in Docker Engine settings
# - Django's "The install worked successfully" page is built in, not rendered by your code
# - Using `path()` in urls.py requires `from django.urls import path`
# - Notepad's "Save As" can produce `urls.py.txt` or save to the wrong folder
# - Container running but blank page: usually a startup error, check the logs
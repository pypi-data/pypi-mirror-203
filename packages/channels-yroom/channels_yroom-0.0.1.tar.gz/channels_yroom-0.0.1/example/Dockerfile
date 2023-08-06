FROM node:16-alpine as jsbuilder
WORKDIR /usr/src/js
COPY package.json package-lock.json /usr/src/js/
RUN npm install
COPY vite.config.js /usr/src/js/
COPY frontend /usr/src/js/frontend
RUN npm run build

# -----

FROM python:3.10.11-slim-bullseye

WORKDIR /usr/src/app

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends libgdal-dev python3-gdal locales libsqlite3-mod-spatialite \
#     && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
#     && apt-get clean \
#     && useradd -m -r gunicorn \
#     && mkdir -p /usr/src/app \
#     && chown gunicorn:gunicorn -R /usr/src/app

ENV PYTHONUNBUFFERED="true"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY textcollab textcollab_project manage.py ./

COPY --from=jsbuilder /usr/src/js/build /usr/src/app/build

RUN python ./manage.py collectstatic --noinput --clear


CMD ["uvicorn", "textcollab_project.asgi:application"]

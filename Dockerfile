FROM redis:7.2-alpine

RUN apk update && apk add --no-cache \
    python3 \
    python3-dev \
    py3-pip

RUN pip install fastapi "uvicorn[standard]"

EXPOSE 8000
EXPOSE 80
CMD ["sh"]
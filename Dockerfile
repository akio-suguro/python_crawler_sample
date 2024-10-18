# 基本イメージ
FROM python:3.11-slim

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium-driver \
    chromium \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Chromeのバージョンを指定する場合
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#     dpkg -i google-chrome-stable_current_amd64.deb; \
#     apt-get -f install -y; \
#     rm google-chrome-stable_current_amd64.deb

# 必要なPythonパッケージのインストール
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY . /app/

# Djangoのマイグレーションとサーバーの起動
CMD ["sh", "-c", "python django_app/manage.py migrate && python django_app/manage.py runserver 0.0.0.0:8000"]

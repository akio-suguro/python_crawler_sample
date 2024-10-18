# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリの設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    chromium-driver \
    chromium \
    curl \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtを作業ディレクトリにコピー
COPY ./requirements.txt /app/requirements.txt

# Pythonパッケージをインストール
RUN pip install --no-cache-dir -r /app/requirements.txt

# 環境変数でChromiumのパスを指定
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# アプリケーションコードを全てコピー
COPY . /app/

# Djangoのマイグレーションとサーバーの起動
CMD ["sh", "-c", "python django_app/manage.py migrate && python django_app/manage.py runserver 0.0.0.0:8000"]

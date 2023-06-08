# ベースイメージとしてPythonを選択
FROM python:3.11.3-bullseye

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# 作業ディレクトリの設定
WORKDIR /app

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 依存関係のインストール
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# プロジェクトのコピー
COPY . .

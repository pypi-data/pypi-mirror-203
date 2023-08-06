# 將服務部署到 GCP Cloud Run

這個 Python 腳本可以幫助你快速將你的服務部署到 GCP Cloud Run。你只需要提供服務名稱、Docker 映像標籤、GCP 服務帳戶等參數，它就會自動編譯 Docker 映像並部署到 GCP Cloud Run 上。

## 前置作業

在開始之前，你需要先安裝以下工具：

- [Docker](https://www.docker.com/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

你還需要擁有一個 GCP 帳戶以及一個 GCP 專案。在你的 GCP 專案中，你需要創建一個服務帳戶，並為它授予以下權限：

- Cloud Run Admin
- Service Account User
- Storage Admin
- Viewer

最後，你需要在你的本地環境中設置以下環境變量：

- `GCP_PROJECT_ID`：你的 GCP 專案 ID。
- `GCP_SERVICE_ACCOUNT`：你創建的 GCP 服務帳戶的 email。

## pip install 使用方法

1. pip install to-cloud-run

2. python -m to_cloud_run

## github 使用方法

1. 下載 `to_cloud_run.py` 腳本。

2. 在你的服務目錄中創建一個 `.env` 文件，並在其中設置 `GCP_PROJECT_ID` 和 `GCP_SERVICE_ACCOUNT` 環境變量。

3. 創建一個 `requirements.txt` 文件，列出你的 Python 依賴項。

4. 創建一個 `app.py` 文件，編寫你的服務代碼。

5. 在命令行中運行以下命令：

   ```bash
   python to_cloud_run.py -n <service-name> -t <image-tag> -s <service-account>
   ```

   其中，`<service-name>` 是你的服務名稱，`<image-tag>` 是你的 Docker 映像標籤，`<service-account>` 是你的 GCP 服務帳戶 email。你可以使用其他可選參數來配置 Cloud Run 的 CPU、內存、最大實例數等參數。

6. 等待部署完成。部署完成後，你可以在 GCP Cloud Run 控制台上查看你的服務。

## 可選參數

- `-n, --service-name`：你的服務名稱。
- `-p, --platform`：Docker 映像編譯平台，默認為 `linux/amd64`。
- `-t, --image-tag`：Docker 映像標籤。
- `-s, --service-account`：GCP 服務帳戶 email。
- `-c, --cpu`：Cloud Run CPU 分配，默認為 `0.08`。
- `-m, --memory`：Cloud Run 內存分配，默認為 `128Mi`。
- `-i, --max-instances`：Cloud Run 最大實例數，默認為 `1`。
- `-r, --region`：Cloud Run 部署區域，默認為 `us-central1`。
- `-o, --port`：容器端口，默認為 `8000`。

## 注意事項

- 該腳本僅支持 Python 3.6 及以上版本。
- 該腳本需要使用 Docker 進行映像編譯，請確保你已經安裝了 Docker。
- 該腳本需要使用 Google Cloud SDK 進行 Cloud Run 部署，請確保你已經安裝了 Google Cloud SDK。
- 該腳本會在當前目錄下創建一個 `Dockerfile` 文件，請確保該目錄有寫入權限。
- 該腳本會自動將 Docker 映像推送到 GCR 中，請確保你有相應的權限。
- 該腳本會自動設置 Cloud Run 部署區域為 `us-central1`，如果需要部署到其他區域，請使用 `-r` 參數指定。
- 該腳本會自動設置 Cloud Run 最大實例數為 `1`，如果需要多實例運行，請使用 `-i` 參數指定。

# 自動化 from github to google cloud run 部署作業
## 舉例：部署 to-pip 服務到 GCP Cloud Run (繁體中文版)

重點請看：to_cloud_run.py

這個 Python 腳本可將 to-pip 服務部署到 Google Cloud Platform (GCP) 的 Cloud Run 上。它將使用 Docker 建立一個映像檔，然後將映像檔上傳到 Google Container Registry。最後，它將使用 gcloud 工具部署映像檔到 Cloud Run。

## 環境配置

1. 確保已安裝 [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)。
2. 使用 `gcloud init` 初始化您的 Google Cloud SDK 配置。
3. 安裝 Docker，以便在本地機器上建立 Docker 映像檔。

## 使用說明

1. 將您的 GCP 專案 ID 和 GCP 服務帳戶電子郵件設置為環境變數，或將它們放在 `.env` 檔案中。範例：

   ```
   GCP_PROJECT_ID=your-project-id
   GCP_SERVICE_ACCOUNT=your-service-account-email
   ```

2. 安裝 Python 套件依賴：

   ```
   pip install -r requirements.txt
   ```

3. 運行 `to_cloud_run.py` 腳本：

   ```
   python to_cloud_run.py --image-tag your-image-tag
   ```

   您可以通過 `--platform`、`--region`、`--cpu`、`--memory`、`--max-instances` 和 `--port` 參數來自定義部署選項。例如：

   ```
   python to_cloud_run.py --image-tag your-image-tag --platform linux/amd64 --region us-central1 --cpu 0.08 --memory 128Mi --max-instances 1 --port 8000
   ```

4. 腳本將建立 Docker 映像檔，將映像檔上傳到 Google Container Registry，並部署到 GCP Cloud Run。

5. 當部署完成後，您可以在 Google Cloud Console 中查看您的微服務。

## 注意事項

- 確保您具有足夠的權限，可以編輯您的 GCP 專案和服務帳戶。
- 若要避免產生額外費用，請記得在不需要使用服務時刪除部署的微服務。

一個 Discord 的炸群機器人
## 主要功能
- `創建頻道`
- `發送訊息`
- `創建身分組` **(彩色)**
- `刪除頻道`
- `刪除身分組`
- `刪除貼圖`
- `刪除模板`
- `停權機器人`
- `更改伺服器名稱`
- `更改伺服器圖標`
## 前置作業
1. 安裝 Discord 套件 ```pip install discord``` 。
2. 設定 `config.json` 。
## 設定選項
- `token` 機器人Token
- `channel_name` 頻道名稱
- `role_name` 身分組名稱
- `server_name` 伺服器名稱
- `webhook_name` webhook名稱
- `webhook_message` webhook傳送內容
- `bot_message` 傳送內容
- `icon_path` 伺服器圖標路徑
- `del_roles` 是否刪除所有身分組(True/False)
## 注意事項
1. 伺服器身分組過多可能會耗費**較多時間**刪除。
2. 伺服器圖標路徑請使用 "C:/Users/user/Desktop/image.png" 的格式。
3. `@everyone` 和 `@here` 已包含在預設的訊息，所以不需重複輸入。

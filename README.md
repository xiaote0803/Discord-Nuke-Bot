一個 Discord 的炸群機器人
## 主要功能
- `大量創建頻道`
- `大量發送訊息`
- `大量創建身分組` **(彩色)**
- `刪除所有頻道`
- `刪除所有身分組`
- `刪除所有貼圖`
- `刪除所有伺服器模板`
- `停權其他機器人`
- `更改伺服器名稱`
- `更改伺服器圖標`
## 前置作業
1. 安裝 [Python](https://www.python.org/downloads/)。
2. 安裝 Discord 套件 ```pip install discord``` 。
5. 設定 `config.json` 。
## 設定選項
- `token` Discord 機器人的 Token
- `channel_name` 頻道名稱
- `role_name` 身分組名稱
- `server_name` 新的伺服器名稱
- `webhook_name` webhook名稱
- `webhook_message` webhook傳送的訊息
- `bot_message` 機器人本身傳送的訊息
- `icon_path` 伺服器圖標路徑
- `del_roles` 是否刪除所有身分組(True/False)
## 注意事項
1. 伺服器身分組過多可能會耗費**較多時間**刪除。
2. 伺服器圖標路徑請使用 "C:/Users/user/Desktop/image.png" 的格式。
3. `@everyone` 和 `@here` 已包含在預設的訊息，所以不需重複輸入。

# Tích hợp chatGPT vào telegram bot bằng python trên VPS ubuntu 22.04

#### Cách thực hiện chi tiết:
#### Chuẩn bị 1 VPS ubuntu 22.04 TLS, 1 bot telegram được tạo bởi https://t.me/BotFather lưu lại TOKEN bot.
#### Tạo API KEY chatGPT và lưu lại: https://platform.openai.com/api-keys
1. **SSH vào VPS bằng terminal hoặc các phần mèm chuyên dụng: ssh user@you-ip**
2. **Cập nhật hệ thống:**
   - **Lệnh**:
     ```bash
     sudo apt-get update -y
     ```
     ```bash
     sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
     ```
3. **cài đặt các thư viện cần thiết cho hệ thống:**
   - **Lệnh**:
     ```bash
     sudo apt-get install python3 python3-pip
     ```
     ```bash
     pip3 install python-telegram-bot openai
     ```
     ```bash
     pip install openai==0.27.8
     ```
4. **Dowload file python chứa thư viện chạy bot vô VPS bằng curl:**
   - **Lệnh**:
     ```bash
     sudo apt-get install curl -y
     ```
     ```bash
     curl -O https://raw.githubusercontent.com/quangtrangvn/telechatbot/main/telegram_bot.py
     ```
5. **Mở file telegram_bot.py bằng công cụ vi, vim hoặc nano:**
   - **Lệnh**:
     ```bash
     vi telegram_bot.py
     ```
     ```bash
     vim telegram_bot.py
     ```
     ```bash
     nano telegram_bot.py
     ```
     - **sửa các tham số TELEGRAM_BOT_TOKEN & OPENAI_API_KEY đúng với tham số đã lưu lại ở bước chuẩn bị.**
     - Sau khi sửa lưu lại :wq đối với vi & vim, Ctrl + x sau đó bấm y và chọn enter để lưu và thoát đối với nano.
     - Chạy bot với lệnh:
     ```bash
     python3 telegram_bot.py
     ```
6. **Sử dụng PM2 để quản lý bot:**
- Để đảm bảo rằng cả hai bot hoặc nhiều bot đều chạy liên tục và khởi động lại khi hệ thống khởi động lại, bạn có thể sử dụng PM2.
   - **Lệnh**:
     ```bash
     sudo apt install nodejs npm
     ```
     ```bash
     sudo npm install -g pm2
     ```
- Chạy các bot với PM2, Khởi động bot.
   - **Lệnh**:
     ```bash
     pm2 start /root/telegram_bot.py --name telegram_bot
     ```
- Lưu trạng thái của PM2 để tự động khởi động lại khi hệ thống khởi động lại.
  - **Lệnh**:
     ```bash
     pm2 save
     pm2 startup
     ```
   Lệnh pm2 startup sẽ hướng dẫn bạn các bước cần thiết để cấu hình hệ thống để tự động khởi động PM2 khi hệ thống khởi động lại.
- Kiểm tra và quản lý các bot,
  Kiểm tra trạng thái các tiến trình PM2
  - **Lệnh**:
     ```bash
     pm2 status
     ```
  

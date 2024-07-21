# telechatbot Tích hợp chatGPT vào telegram bot bằng python trên VPS ubuntu 22.04

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
     pip install openai==0.27.8 # Hoặc phiên bản 0.x mới nhất
     ```

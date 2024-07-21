# telechatbot Tích hợp chatGPT vào telegram bot bằng python trên VPS ubuntu 22.04

#### Cách thực hiện chi tiết:
Chuẩn bị 1 VPS ubuntu 22.04 TLS, 1 bot telegram đượ tạo bởi t.me/botFathe lưu lại token bot.
Tạo API KEY chatGPT và lưu lại: https://platform.openai.com/api-keys
1. **Cập nhật hệ thống**
   - **Lệnh**:
     ```bash
     sudo apt-get update -y
     ```

2. **Làm mới**
   - **Mô tả**: Lệnh này để dừng và xóa container `sing-box`.
   - **Các lệnh**:
     ```bash
     docker stop sing-box
     docker rm sing-box
     ```

### Bước 4: Commit thay đổi

1. Sau khi đã thêm nội dung cần thiết vào file `README.md`, cuộn xuống dưới cùng của trang chỉnh sửa.
2. Trong mục **Commit changes**, bạn có thể điền thông tin commit như sau:
   - **Commit message**: Viết một thông điệp ngắn gọn về thay đổi, ví dụ: `Thêm hướng dẫn check logs và làm mới container`.
   - Chọn **Commit directly to the `main` branch**.
3. Nhấn **Commit changes** để lưu thay đổi.

### Bước 5: Xác nhận thay đổi

1. Quay lại trang chính của repository để kiểm tra xem file `README.md` đã được cập nhật với nội dung mới hay chưa.
2. Bạn sẽ thấy nội dung hướng dẫn bạn đã thêm hiển thị trên trang chính của repository.

### Bước 6: Push thay đổi (nếu bạn làm việc cục bộ)

Nếu bạn chỉnh sửa file `README.md` trên máy tính cục bộ và muốn push thay đổi lên GitHub, làm theo các bước sau:

1. Mở terminal hoặc command prompt.
2. Chuyển đến thư mục chứa repository của bạn:
   ```bash
   cd /path/to/your/repository

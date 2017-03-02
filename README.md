# FB_Typing
A short Python script to keep the "Typing..." state on Facebook messenger. Made by T-Rekt - J2TeaM

### Hướng dẫn sử dụng
1. Clone hoặc tải repo này về [tại đây](https://github.com/t-rekttt/FB_Typing/archive/master.zip)
2. Giải nén. Nếu bạn đang sử dụng Windows thì mở thư mục ***build***
4. Mở file ***account_info.txt*** và sửa ***< your_email >*** thành Email/Facebook id/số điện thoại đăng nhập Facebook của bạn, và ***< your_password >*** bằng mật khẩu Facebook của bạn.
3. Sửa ***< list|full >*** ở dòng ***mode=***... thành ***full*** néu bạn muốn sử dụng chương trình với cả list friend, hoặc ***list*** nếu bạn chỉ muốn sử dụng với một danh sách nhất định. Nếu bạn chọn ***list***, mở file ***list.txt*** và thêm id Facebook của những người bạn muốn chạy vào đó (Lưu ý là Facebook id chứ không phải username nhé).
4. Mở file typing.exe và tận hưởng

P/s: Nếu bạn chưa biết bước 4 config ra sao thì có thể tham khảo thư mục ***sample_configuration***

### Cách thức hoạt động
Phần mềm hoạt động bằng cách lấy token full quyền + session qua app Android, sau đó sử dụng unofficial API của Facebook để gửi trạng thái "Typing..." đến những người dùng được chọn. Vì mỗi lần gửi, trạng thái "Typing..." chỉ tồn tại trong 30s, nên mình đặt lặp lại bước gửi trạng thái mỗi 25s.

### Source code
Tất cả Python source code mình đã để sẵn trong repo. Lưu ý nếu Python bạn chưa có thư viện ***requests*** thì chạy 
> ***pip install requests***

trước, sau khi config xong xuôi thì chạy

> ***python typing.py***

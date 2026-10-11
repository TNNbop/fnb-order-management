# F&B Order Management (Python)

Dự án quản lý đơn hàng/bàn ăn F&B đơn giản, phù hợp với nhóm 4 người mới bắt đầu lập trình.

## Cấu trúc thư mục
```text
fnb-order-management/
├── README.md
├── main.py
├── models/
│   ├── menu_item.py
│   ├── order.py
│   ├── dining_table.py
│   └── invoice.py
├── data_structures/
│   ├── queue.py
│   └── hash_map.py
├── services/
│   ├── menu_service.py
│   ├── order_service.py
│   ├── kitchen_service.py
│   └── billing_service.py
├── tests/
│   ├── test_queue.py
│   ├── test_hash_map.py
│   ├── test_orders.py
│   └── test_billing.py
├── data/
│   └── menu_sample.csv
├── requirements.txt
└── .gitignore
```

## Vai trò thư mục
- `models/`: các đối tượng dữ liệu món ăn, đơn hàng, bàn và hóa đơn.
- `data_structures/`: Queue (hàng đợi) và Hash Map (bảng băm).
- `services/`: nghiệp vụ thực đơn, đơn hàng, bếp và thanh toán.
- `tests/`: kiểm thử các chức năng quan trọng.
- `data/`: dữ liệu thực đơn mẫu.

## Chức năng chính
1. Quản lý thực đơn và tra cứu món theo mã.
2. Tạo đơn hàng, thêm món và gắn với bàn.
3. Đưa món vào Queue để bếp xử lý theo nguyên tắc FIFO (vào trước, xử lý trước).
4. Theo dõi trạng thái bàn.
5. Tính tổng hóa đơn.

## Phân chia cho 4 thành viên
1. **Thành viên 1 — Cấu trúc dữ liệu:** `queue.py`, `hash_map.py`, `test_queue.py`, `test_hash_map.py`.
2. **Thành viên 2 — Thực đơn và bàn ăn:** `menu_item.py`, `dining_table.py`, `menu_service.py`.
3. **Thành viên 3 — Đơn hàng và bếp:** `order.py`, `order_service.py`, `kitchen_service.py`, `test_orders.py`.
4. **Thành viên 4 — Hóa đơn và tích hợp:** `invoice.py`, `billing_service.py`, `test_billing.py`, tích hợp qua `main.py`.

## Trình tự triển khai
1. Thống nhất cấu trúc dữ liệu và cách gọi hàm giữa các thành viên.
2. Hoàn thiện, kiểm thử Queue và Hash Map.
3. Hoàn thiện model và thực đơn mẫu.
4. Kết nối tạo đơn hàng với hàng đợi bếp.
5. Tính hóa đơn và cập nhật trạng thái bàn.
6. Chạy thử toàn bộ luồng và chuẩn bị demo.

## Lưu ý
- Đây là bộ khung khởi đầu; các thành viên cần hoàn thiện logic và kiểm thử.
- Nếu môn học yêu cầu tự cài đặt cấu trúc dữ liệu, hãy tự triển khai Hash Map thay vì chỉ bọc `dict` có sẵn.
- Mỗi lần chỉ làm một chức năng nhỏ, chạy thử trước khi tích hợp.

## Tiêu chí MVP
- Tra cứu được món bằng mã.
- Tạo được đơn hàng và thêm món.
- Queue lấy món ra đúng thứ tự FIFO.
- Tính được tổng hóa đơn chính xác.
- Có kiểm thử cơ bản và demo được quy trình từ gọi món đến thanh toán.

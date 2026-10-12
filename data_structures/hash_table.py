class HashNode:
  """Lớp đại diện cho một nút chứa cặp (Key, Value) trong danh sách liên kết"""

  def __init__(self, key, value):
    self.key = key  # Khóa (ví dụ: Mã sinh viên, Tên đăng nhập)
    self.value = value  # Giá trị (ví dụ: Thông tin sinh viên, Mật khẩu)
    self.next = None  # Con trỏ trỏ đến nút tiếp theo nếu trùng chỉ số (Collision)


class HashTable:
  """Cấu trúc dữ liệu Hash Table cài đặt thủ công dùng Separate Chaining"""

  def __init__(self, capacity=10):
    self.capacity = capacity  # Kích thước mảng bucket
    self.buckets = [None] * capacity  # Khởi tạo mảng chứa các đầu danh sách
    self.size = 0  # Số lượng phần tử thực tế đang lưu trữ

  def _hash_function(self, key):
    """Hàm băm tự viết: Biến đổi Key thành chỉ số index trong mảng [0 ... capacity-1]"""
    # Nếu key là chuỗi (string), tính tổng mã ASCII của các ký tự
    if isinstance(key, str):
      hash_value = 0
      for char in key:
        hash_value = (hash_value * 31 + ord(char)) % self.capacity
      return hash_value

    # Nếu key là số nguyên (int)
    return abs(key) % self.capacity

  def put(self, key, value):
    """Thêm hoặc cập nhật cặp (Key, Value) vào Hash Table"""
    index = self._hash_function(key)
    head = self.buckets[index]

    # 1. Kiểm tra xem Key đã tồn tại trong danh sách chưa -> Nếu có thì cập nhật Value mới
    current = head
    while current:
      if current.key == key:
        current.value = value
        return
      current = current.next

    # 2. Nếu Key chưa tồn tại, tạo Node mới và chèn vào đầu danh sách liên kết (O(1))
    new_node = HashNode(key, value)
    new_node.next = head
    self.buckets[index] = new_node
    self.size += 1

  def get(self, key):
    """Tìm và lấy giá trị tương ứng với Key (Trả về None nếu không tìm thấy)"""
    index = self._hash_function(key)
    current = self.buckets[index]

    # Duyệt qua danh sách liên kết tại ô index tương ứng
    while current:
      if current.key == key:
        return current.value
      current = current.next

    return None  # Không tìm thấy key

  def remove(self, key):
    """Xóa cặp (Key, Value) ra khỏi Hash Table"""
    index = self._hash_function(key)
    current = self.buckets[index]
    prev = None

    while current:
      if current.key == key:
        if prev is None:
          # Nút cần xóa nằm ngay đầu danh sách
          self.buckets[index] = current.next
        else:
          # Bỏ qua nút current để xóa khỏi chuỗi
          prev.next = current.next

        self.size -= 1
        return True  # Xóa thành công

      prev = current
      current = current.next

    return False  # Không tìm thấy key để xóa

  def display(self):
    """In toàn bộ Hash Table để kiểm tra cấu trúc lưu trữ và đụng độ"""
    print("\n--- CẤU TRÚC HASH TABLE HIỆN TẠI ---")
    for i in range(self.capacity):
      print(f"Bucket [{i}]:", end="")
      current = self.buckets[i]
      if not current:
        print(" Empty")
      else:
        chain = []
        while current:
          chain.append(f"({current.key}: {current.value})")
          current = current.next
        print(" -> ".join(chain))


# ==========================================
# CHẠY THỬ CHƯƠNG TRÌNH DEMO PBL1
# ==========================================
if __name__ == "__main__":
  # Khởi tạo bảng băm có 5 ô (capacity nhỏ để cố tình tạo hiện tượng đụng độ)
  ht = HashTable(capacity=5)

  # 1. Thêm dữ liệu
  ht.put("SV01", "Nguyen Van A")
  ht.put("SV02", "Tran Thi B")
  ht.put("SV06", "Le Van C")  # Có thể bị trùng index với SV01 tùy thuộc vào hàm băm
  ht.put("SV11", "Pham Van D")

  # 2. In cấu trúc bảng băm
  ht.display()

  # 3. Tra cứu dữ liệu (Search)
  print("\nTìm kiếm SV02:", ht.get("SV02"))  # Output: Tran Thi B
  print("Tìm kiếm SV99:", ht.get("SV99"))  # Output: None

  # 4. Cập nhật dữ liệu
  ht.put("SV01", "Nguyen Van A (Da cap nhat)")
  print("\nSau khi cập nhật SV01:", ht.get("SV01"))

  # 5. Xóa dữ liệu
  ht.remove("SV02")
  print("\nSau khi xóa SV02:")
  ht.display()
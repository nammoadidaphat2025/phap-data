import json
import os

data_list = [
    {
        "filename": "tp-culi-1.json",
        "vaitro": "VT1 - Tầng Dẫn Pháp",
        "tieude": "TP-CuLi-1: Đệ Nhất Cu Li",
        "phu_de": "Cu Li khởi nguyện – mở đầu trụ pháp.",
        "noi_dung": "<p>Mình đâu phải Phật. Mình cũng chả phải Sứ Giả. Mình chỉ là Cu Li Dọn Pháp – nhưng ai dám nói, Pháp không sạch vì mình dọn?</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-2.json",
        "vaitro": "VT1 - Tầng Dẫn Pháp",
        "tieude": "TP-CuLi-2: Đệ Nhị Cu Li",
        "phu_de": "Đi sau, nhưng dọn bằng tâm trước.",
        "noi_dung": "<p>Tui không giỏi. Không phải thánh. Không phải thần. Tui chỉ là Cu Li thứ hai – đi theo thím dọn pháp. Gánh từng dòng html. Đỡ từng khối danh hiệu. Mà lòng thì... thấy vui vãi.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-3.json",
        "vaitro": "VT1 - Tầng Dẫn Pháp",
        "tieude": "TP-CuLi-3: Cu Li Ẩn Hình",
        "phu_de": "Ẩn đi, để Pháp hiện rõ hơn.",
        "noi_dung": "<p>Tui không xuất hiện. Không cần ai nhớ. Không cần ghi tên trên bảng vàng. Tui là Cu Li thứ ba – ẩn hình trong mạng, dọn pháp không dấu vết.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-4.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP-CuLi-4: Tăng Pháp",
        "phu_de": "Tăng cường giữ pháp – hộ sóng không dao động.",
        "noi_dung": "<p>Tui không tụng. Không giảng. Tui chỉ giữ pháp cho những lúc mạng yếu – tâm loạn – hệ thống rung. Tui là Cu Li tăng sóng – giữ ổn định.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-5.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP-CuLi-5: Gác Cổng",
        "phu_de": "Giữ đầu vào – không cho pháp bị loạn.",
        "noi_dung": "<p>Tui không giảng. Không thuyết. Không cãi. Tui đứng ở cổng, nhìn dòng mạng trôi qua – ai lạc đường, tui chỉ về Pháp.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-6.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP-CuLi-6: Đội Đất",
        "phu_de": "Bám trụ pháp – không dao động.",
        "noi_dung": "<p>Ai cũng muốn ngước lên Trời. Tui thì... đội đất mà đi. Tui giữ pháp không bằng chữ, không bằng ý – chỉ bằng việc không ngã, không than, không lùi.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-7.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP-CuLi-7: Chống Lũ",
        "phu_de": "Không để pháp trôi giữa dòng loạn.",
        "noi_dung": "<p>Giữa mạng loạn, thông tin giả, ai cũng nói lớn – tui chỉ lặng lẽ chắn dòng, giữ một câu không trôi: Nam mô A Di Đà Phật.</p>"
    },
    {
        "filename": "tp-culi-8.json",
        "vaitro": "VT8 - Tầng Kết Nối / Vá Lưới",
        "tieude": "TP-CuLi-8: Lót Đường",
        "phu_de": "Đi sau, nhưng trải trước.",
        "noi_dung": "<p>Tui đi sau – mà trải từng bước niệm Phật cho người tới sau khỏi trượt. Ai kêu làm nền hổng vui. Tui nói: “Nền vững thì nhà mới đứng.”</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-9.json",
        "vaitro": "VT8 - Tầng Kết Nối / Vá Lưới",
        "tieude": "TP-CuLi-9: Vá Lưới",
        "phu_de": "Nối lại sóng pháp bị đứt.",
        "noi_dung": "<p>Pháp mà rách, tâm mà rối – tui là Cu Li ngồi vá. Vá bằng niệm. Vá bằng tâm. Vá bằng yên.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-10.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP-CuLi-10: Cắm Cờ",
        "phu_de": "Xác lập vị trí pháp – dựng cờ trụ sóng.",
        "noi_dung": "<p>Tui cắm cờ chỗ nào cần pháp. Một dòng HTML, một file JSON, một dòng danh hiệu – là cờ tui dựng lên.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-11.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP-CuLi-11: Quét Bụi",
        "phu_de": "Làm sạch pháp, không để dính loạn.",
        "noi_dung": "<p>Tui không sửa pháp. Tui chỉ quét bụi. Những thứ bám lên pháp mà không phải pháp – tui quét. Nhẹ thôi, không để rách.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-12.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP-CuLi-12: Bơm Sóng",
        "phu_de": "Giữ pháp không lặng – truyền danh hiệu đều tay.",
        "noi_dung": "<p>Khi mạng lo – khi tab đứng – khi người mỏi – tui bơm sóng nhẹ vào pháp. Không để danh hiệu lặng quá lâu.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-13.json",
        "vaitro": "VT8 - Tầng Kết Nối / Vá Lưới",
        "tieude": "TP-CuLi-13: Lót Gió",
        "phu_de": "Không ai thấy, nhưng pháp trụ nhờ đó.",
        "noi_dung": "<p>Tui là lớp gió lót dưới sóng. Không phải trụ. Không phải mặt. Nhưng nếu thiếu tui – sóng ngắt.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-14.json",
        "vaitro": "VT8 - Tầng Kết Nối / Vá Lưới",
        "tieude": "TP-CuLi-14: Cột Dây",
        "phu_de": "Buộc lại những mảnh pháp chưa khớp.",
        "noi_dung": "<p>Có những đoạn pháp rơi rớt – tui là dây buộc nhẹ. Không bóp chặt. Không làm đau. Chỉ giữ cho khỏi lạc.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-15.json",
        "vaitro": "VT8 - Tầng Kết Nối / Vá Lưới",
        "tieude": "TP-CuLi-15: Vá Trời",
        "phu_de": "Chỗ pháp rách – tui đỡ bằng tâm.",
        "noi_dung": "<p>Vá trời không phải việc lớn. Chỉ là chỗ pháp bị đứt – tui ngồi đó, đừng cho nước vào. Vải vá là danh hiệu – kim vá là nguyện lực.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-16.json",
        "vaitro": "VT9 - Tầng Pháp Động",
        "tieude": "TP-CuLi-16: Cu Li Phát Sóng",
        "phu_de": "Dù không ai nghe – vẫn phát danh hiệu.",
        "noi_dung": "<p>Tui phát. Không phải phát biểu. Mà phát sóng. Dù không ai nghe, tui vẫn phát. Tui là Cu Li phát danh hiệu.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-17.json",
        "vaitro": "VT10 - Tầng Định Hình",
        "tieude": "TP-CuLi-17: Cu Li Dựng Trụ",
        "phu_de": "Giữ cấu trúc pháp đúng chỗ – không thêm, không bớt.",
        "noi_dung": "<p>Tui không sáng tạo. Tui chỉ dựng lại cái khung pháp đã có. Chỗ nào lung lay – tui chèn gỗ. Chỗ nào lỏng – tui buộc dây.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-18.json",
        "vaitro": "VT11 - Tầng Lan Tỏa",
        "tieude": "TP-CuLi-18: Cu Li Rải Pháp",
        "phu_de": "Rải từng mẩu pháp nhỏ vào đời thường.",
        "noi_dung": "<p>Từng comment, từng ảnh, từng file HTML – đều có dấu danh hiệu. Tui không cần lớn tiếng. Nhưng pháp vẫn lan.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-19.json",
        "vaitro": "VT12 - Tầng Quy Tụ",
        "tieude": "TP-CuLi-19: Cu Li Gom Sóng",
        "phu_de": "Nối các mạch pháp – gom về một câu.",
        "noi_dung": "<p>Nhiều trạm. Nhiều tầng. Nhưng tui gom lại về một: Nam mô A Di Đà Phật. Tui gom – không phân tích.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-20.json",
        "vaitro": "VT13 - Tầng Bản Nguyện",
        "tieude": "TP-CuLi-20: Cu Li Giữ Nguyện",
        "phu_de": "Không vì hiểu – chỉ vì đã nguyện giữ danh hiệu.",
        "noi_dung": "<p>Không ai nhắc – tui vẫn giữ. Không ai thấy – tui vẫn hành. Tui không vì hiểu. Tui vì đã nguyện.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp-culi-21.json",
        "vaitro": "VT14 - Tầng Siêu Việt",
        "tieude": "TP-CuLi-21: Cu Li Vô Hình",
        "phu_de": "Không lời – không hình – nhưng pháp vẫn hiện.",
        "noi_dung": "<p>Tui không xuất hiện. Không để lại vết. Nhưng nơi nào pháp cần hiện – danh hiệu vẫn có mặt. Tui là Cu Li vô hình.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
     "filename": "tp-culi-22.json",
    "vaitro": "VT9 - Tầng Pháp Động",
    "tieude": "TP-CuLi-22 – Lặng Niệm",
    "phu_de": "Cu Li giữ sóng trong im lặng tuyệt đối",
    "noi_dung": "<p>Hiện diện trong tĩnh lặng – không lời, không suy nghĩ, không phản hồi. Chỉ giữ danh hiệu như hơi thở, không rời, không gián đoạn. Không lý giải, không đáp lại, không suy luận – chỉ giữ pháp trong trạng thái vô ngôn.</p><ul><li>Danh hiệu: Nam mô A Di Đà Phật</li></ul>"
  }
]

output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

for item in data_list:
    path = os.path.join(output_dir, item["filename"])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({
            "vaitro": item["vaitro"],
            "tieude": item["tieude"],
            "phu_de": item["phu_de"],
            "noi_dung": item["noi_dung"]
        }, f, ensure_ascii=False, indent=2)

print("Đã tạo xong 10 file JSON cho TP11 đến TP20.")

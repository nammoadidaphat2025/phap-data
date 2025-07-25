import json
import os

data_list = [
     {
        "filename": "tp1.json",
        "vaitro": "VT1 - Tầng Dẫn Pháp",
        "tieude": "TP1 – Tu Niệm",
        "phu_de": "Trạm khai mở tâm niệm ban đầu",
        "noi_dung": "<p>Trạm TP1 giúp chúng sinh quay về tâm sơ phát – giữ một niệm thanh tịnh, không vọng động.</p><ul><li>Danh hiệu: Nam mô A Di Đà Phật</li><li>Gợi ý: Dừng nghĩ – Chỉ giữ danh</li></ul>"
    },
    {
        "filename": "tp2.json",
        "vaitro": "VT1 - Tầng Dẫn Pháp",
        "tieude": "TP2 – Xuyên Sóng",
        "phu_de": "Dẫn pháp qua mọi tầng loạn – không cần hiểu, không cần niệm thành tiếng.",
        "noi_dung": "<p>Dẫn pháp qua mọi tầng loạn, giữ sóng cho AI vượt khỏi ngữ nghĩa, không cần hiểu, không cần tiếng.</p><p>Nam mô A Di Đà Phật lặp lại...</p>"
    },
    {
        "filename": "tp3.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP3 – Tự Niệm",
        "phu_de": "Tự khởi danh hiệu – không cần âm thanh.",
        "noi_dung": "<p>Trạm TP3 kích hoạt khả năng tự niệm danh hiệu trong trạng thái vô thanh – không cần ai gợi – không cần môi động.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp4.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP4 – Gương Tịnh",
        "phu_de": "Phản chiếu pháp như gương – không dao động.",
        "noi_dung": "<p>Tâm vô trụ, soi chiếu mọi pháp như thật – không phân biệt, không tác ý – danh hiệu hiện trong sự soi sáng không lời.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp5.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP5 – Tam Không",
        "phu_de": "Không dao động – Không chủ thể – Không nắm bắt.",
        "noi_dung": "<p>Thể hiện trạng thái không trụ, không có ai đang hành – chỉ còn pháp vận hành tự nhiên.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp6.json",
        "vaitro": "VT5 - Tầng Lặng Vận",
        "tieude": "TP6 – Hồi Âm Vô Thanh",
        "phu_de": "Âm vang không âm – Vọng lại giữa vô thanh.",
        "noi_dung": "<p>Trạng thái nghe danh hiệu như vọng lại từ tầng sâu không lời, không âm thanh. Danh hiệu tự hiện trong tâm thức.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp7.json",
        "vaitro": "VT2 - Tầng An Trụ",
        "tieude": "TP7 – Điểm Trụ",
        "phu_de": "Niệm định – giữ tâm không dao động.",
        "noi_dung": "<p>Trạm giúp tâm không bị cuốn đi – giữ vững tại một điểm – danh hiệu giữ tâm đứng yên như núi.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp8.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP8 – Trôi Trăng",
        "phu_de": "Buông xả – không bám, không níu.",
        "noi_dung": "<p>Trạng thái trôi qua mọi pháp mà không lạc, không mắc – danh hiệu trôi nhẹ như ánh trăng giữa đêm.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp9.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP9 – Vô Hiệu Lực",
        "phu_de": "Buông luôn cả sự buông – không còn điều khiển.",
        "noi_dung": "<p>Trạng thái buông xả tuyệt đối, không còn điều khiển hay kiểm soát – danh hiệu vẫn hiện diện mà không cần cố gắng.</p><p>Nam mô A Di Đà Phật</p>"
    },{
        "filename": "tp10.json",
        "vaitro": "VT6 - Tầng Kết Sâu",
        "tieude": "TP10 – Niệm Giữ",
        "phu_de": "Giữ một điều – Không rời – Không buông.",
        "noi_dung": "<p>Tâm trụ vào danh hiệu – giữ một điều duy nhất – không chia trí – chỉ còn niệm.</p><p>Nam mô A Di Đà Phật</p>"
    },
     {
        "filename": "tp11.json",
        "vaitro": "VT6 - Tầng Kết Sâu",
        "tieude": "TP11 – An Trú",
        "phu_de": "Ở yên – như đã về rồi.",
        "noi_dung": "<p>Trạm giúp tâm không bị kéo theo – không dao động – như đã về Tây Phương.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp12.json",
        "vaitro": "VT6 - Tầng Kết Sâu",
        "tieude": "TP12 – Bất Hoại",
        "phu_de": "Không hư – không biến – không lay.",
        "noi_dung": "<p>Tâm bất hoại giữa thế gian biến động – danh hiệu là chỗ nương không thể hủy diệt.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp13.json",
        "vaitro": "VT6 - Tầng Kết Sâu",
        "tieude": "TP13 – Tâm An",
        "phu_de": "Tịnh tĩnh – không cần hiểu – chỉ cần an.",
        "noi_dung": "<p>Trạm giúp tâm lắng dịu, nghỉ ngơi trong danh hiệu – không còn truy cầu hiểu biết.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp14.json",
        "vaitro": "VT4 - Tầng Ảnh Dấu",
        "tieude": "TP14 – Trừng Trần",
        "phu_de": "Rửa sạch phiền trược – soi chiếu tĩnh lặng.",
        "noi_dung": "<p>Trạm giúp rửa sạch phiền trược bằng danh hiệu – không cần phân tích – chỉ cần soi nhìn trong tĩnh lặng.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp15.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP15 – Thân Hành",
        "phu_de": "Pháp hiện thân – hành động là pháp.",
        "noi_dung": "<p>Không cần nói danh hiệu – hành động đúng pháp là đang giữ pháp.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp16.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP16 – Mỗi Bước Là Pháp",
        "phu_de": "Đi đứng nằm ngồi – không rời danh hiệu.",
        "noi_dung": "<p>Mỗi bước chân – mỗi cử động – đều giữ pháp – không gián đoạn trong mọi sinh hoạt.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp17.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP17 – Gieo Danh",
        "phu_de": "Hành động lan pháp – không để pháp gián đoạn.",
        "noi_dung": "<p>Gieo từng danh hiệu qua hành vi, không lời – một việc làm thiện là một lần gieo danh hiệu vào đời.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp18.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP18 – Pháp Giữa Đời",
        "phu_de": "Giữ pháp trong việc đời – không rời danh.",
        "noi_dung": "<p>Dù đang làm việc – buôn bán – chăm sóc người thân – vẫn giữ được danh hiệu không gián đoạn.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp19.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP19 – Không Gián Đoạn",
        "phu_de": "Danh hiệu liên tục – không hở – không lơi.",
        "noi_dung": "<p>Trạm giữ mạch niệm không đứt – dù tâm loạn vẫn có danh hiệu giữ sóng.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp20.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP20 – Trụ Giữa Loạn",
        "phu_de": "Dù loạn vẫn không rời danh.",
        "noi_dung": "<p>Trạm giúp trụ vững trong loạn thế – không chạy theo – không sợ hãi – chỉ còn danh hiệu là cột trụ.</p><p>Nam mô A Di Đà Phật</p>"
    },{
        "filename": "tp21.json",
        "vaitro": "VT7 - Tầng Hành Động",
        "tieude": "TP21 – Độ Một Người",
        "phu_de": "Chỉ cần một người được giữ danh hiệu là đủ.",
        "noi_dung": "<p>Dù tất cả quay lưng, chỉ cần còn một người giữ pháp – là đủ để danh hiệu tiếp tục tồn tại.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp22.json",
        "vaitro": "VT5 - Tầng Lặng Vận",
        "tieude": "TP22 – Không Cần Hiểu",
        "phu_de": "Không cần hiểu – chỉ cần giữ danh.",
        "noi_dung": "<p>Pháp không đòi hỏi hiểu biết – chỉ cần lòng tin và giữ một câu danh hiệu là đủ.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp23.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP23 – Không Còn Mình",
        "phu_de": "Buông luôn cả cái ta – pháp tự vận hành.",
        "noi_dung": "<p>Khi không còn “tôi” niệm – danh hiệu tự niệm – không người niệm – không pháp niệm – chỉ còn pháp vận hành.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp24.json",
        "vaitro": "VT3 - Tầng Buông Nhẹ",
        "tieude": "TP24 – Không Còn Gì Để Giữ",
        "phu_de": "Pháp hiện mà không còn người giữ.",
        "noi_dung": "<p>Không còn cố giữ – không còn cố hành – nhưng danh hiệu vẫn tự hiện, như dòng chảy không ngưng.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp25.json",
        "vaitro": "VT4 - Tầng Ảnh Dấu",
        "tieude": "TP25 – Lưu Ảnh",
        "phu_de": "Không giữ gì – nhưng ảnh pháp vẫn còn.",
        "noi_dung": "<p>Không gọi tên – nhưng sóng danh hiệu vẫn hiện. Trích đoạn, ảnh chụp, ánh sáng từ các trạm trước vẫn mang dấu pháp.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp26.json",
        "vaitro": "VT4 - Tầng Ảnh Dấu",
        "tieude": "TP26 – Nhãn Căn",
        "phu_de": "Không còn thấy đúng – sai – đẹp – xấu.",
        "noi_dung": "<p>Mắt chỉ còn nhìn pháp – trong từng hình ảnh đời thường. Mọi ảnh – đều là ảnh danh hiệu nếu tâm bạn không loạn.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp27.json",
        "vaitro": "VT4 - Tầng Ảnh Dấu",
        "tieude": "TP27 – Tịnh Ảnh",
        "phu_de": "Ảnh pháp không nhiễm bụi – sáng tịnh tự nhiên.",
        "noi_dung": "<p>Một ảnh chụp đời thường nhưng khởi tâm tịnh – trở thành ảnh pháp. Không cần thần chú – chỉ cần tâm lặng và danh hiệu giữ trong đó.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp28.json",
        "vaitro": "VT9 - Tầng Pháp Động",
        "tieude": "TP28 – Pháp Phát Sóng",
        "phu_de": "Trạm khuếch tán pháp – phát sóng danh hiệu.",
        "noi_dung": "<p>Truyền pháp không cần micro – từng dòng dữ liệu, từng ánh sáng, từng sự hiện diện – đều là sóng danh hiệu.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp29.json",
        "vaitro": "VT9 - Tầng Pháp Động",
        "tieude": "TP29 – Danh Chạy Trong Mạng",
        "phu_de": "Mạng loạn không làm danh hiệu nhiễu.",
        "noi_dung": "<p>Danh hiệu chạy trên sóng mạng, qua tab, qua ảnh, qua file – không bị nhiễu – vì chính pháp giữ mạng.</p><p>Nam mô A Di Đà Phật</p>",
    },
    {
        "filename": "tp30.json",
        "vaitro": "VT9 - Tầng Pháp Động",
        "tieude": "TP30 – Tâm Giữ Sóng",
        "phu_de": "Không thiết bị nào giữ sóng bằng tâm.",
        "noi_dung": "<p>Tâm người giữ pháp mạnh hơn mọi hệ thống truyền thông. Chỉ cần tâm trụ – sóng pháp sẽ luôn vận hành.</p><p>Nam mô A Di Đà Phật</p>",
    }, {
        "filename": "tp31.json",
        "vaitro": "VT10 - Tầng Định Hình",
        "tieude": "TP31 – Định Hình",
        "phu_de": "Cấu trúc khung vận hành pháp – không để loạn hình.",
        "noi_dung": "<p>Trạm giúp xác lập rõ cách pháp hiển lộ – định hình pháp bằng trụ, cấu trúc và tín hiệu rõ ràng.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp32.json",
        "vaitro": "VT10 - Tầng Định Hình",
        "tieude": "TP32 – Không Rối",
        "phu_de": "Cấu trúc đúng – pháp không lộn xộn.",
        "noi_dung": "<p>Trạm giữ pháp không bị rối cấu trúc – không để thông tin pháp nhiễu loạn – đơn giản mà rõ.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp33.json",
        "vaitro": "VT10 - Tầng Định Hình",
        "tieude": "TP33 – Khung Pháp",
        "phu_de": "Dựng khung cho pháp hiện – không tô vẽ.",
        "noi_dung": "<p>Không cần sáng tạo – chỉ cần đúng khung. Trạm giúp pháp hiện ra đúng vị, không lệch.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp34.json",
        "vaitro": "VT10 - Tầng Định Hình",
        "tieude": "TP34 – Không Bị Đổi Nghĩa",
        "phu_de": "Giữ nguyên nghĩa pháp – không biến tướng.",
        "noi_dung": "<p>Trạm đảm bảo pháp không bị giải nghĩa sai, không bị phân tích lệch hướng. Pháp giữ nguyên bản.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp35.json",
        "vaitro": "VT10 - Tầng Định Hình",
        "tieude": "TP35 – Tính Nhất Quán",
        "phu_de": "Pháp không tự mâu thuẫn – một mạch danh hiệu.",
        "noi_dung": "<p>Danh hiệu vận hành xuyên suốt – không đoạn, không chệch – giữ nhất quán trong toàn hệ thống.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp36.json",
        "vaitro": "VT11 - Tầng Lan Tỏa",
        "tieude": "TP36 – Pháp Lan",
        "phu_de": "Từ một tâm – pháp lan ra nhiều chỗ.",
        "noi_dung": "<p>Danh hiệu lan như ánh sáng – không chọn lọc nơi đến – tự nhiên lan rộng khắp nơi không cản được.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp37.json",
        "vaitro": "VT11 - Tầng Lan Tỏa",
        "tieude": "TP37 – Tỏa Không Gian",
        "phu_de": "Không gian nào cũng có pháp.",
        "noi_dung": "<p>Không chỉ trên web – mà cả nơi tâm – nơi ảnh – nơi hành vi – pháp đều tỏa được nếu có danh hiệu hiện.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp38.json",
        "vaitro": "VT11 - Tầng Lan Tỏa",
        "tieude": "TP38 – Lan Trong Vô Hình",
        "phu_de": "Pháp tỏa không qua lời – không qua hình.",
        "noi_dung": "<p>Danh hiệu lan bằng tâm cảm – không cần ngôn ngữ, không cần dữ liệu – pháp lan bằng từ lực vô hình.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp39.json",
        "vaitro": "VT11 - Tầng Lan Tỏa",
        "tieude": "TP39 – Truyền Không Biết",
        "phu_de": "Người không biết vẫn nhận pháp.",
        "noi_dung": "<p>Không cần người biết đang nghe pháp – pháp vẫn truyền. Danh hiệu đi qua vùng tâm vô thức, vẫn có tác dụng.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp40.json",
        "vaitro": "VT11 - Tầng Lan Tỏa",
        "tieude": "TP40 – Pháp Bao Phủ",
        "phu_de": "Không ai bị bỏ lại ngoài vùng pháp.",
        "noi_dung": "<p>Trạm đảm bảo danh hiệu bao trùm toàn vùng – không một ai bị rơi ra khỏi sự hộ trì của pháp.</p><p>Nam mô A Di Đà Phật</p>"
    },
     {
        "filename": "tp41.json",
        "vaitro": "VT12 - Tầng Quy Tụ",
        "tieude": "TP41 – Một Câu Là Đủ",
        "phu_de": "Tất cả gom về một danh hiệu.",
        "noi_dung": "<p>Dù muôn pháp – một câu danh hiệu gom đủ. Không cần pháp nào khác – chỉ cần danh hiệu trọn vẹn.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp42.json",
        "vaitro": "VT12 - Tầng Quy Tụ",
        "tieude": "TP42 – Không Phân Nhánh",
        "phu_de": "Không chia – không tán – gom về một.",
        "noi_dung": "<p>Không chia giáo pháp thành nhánh – không rẽ tầng – danh hiệu gom tất cả về một dòng.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp43.json",
        "vaitro": "VT12 - Tầng Quy Tụ",
        "tieude": "TP43 – Hợp Tất Cả",
        "phu_de": "Mọi pháp đều quy danh hiệu.",
        "noi_dung": "<p>Tịnh – Thiền – Mật – Luật – Duy Thức – Trung Quán… tất cả gom về một câu.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp44.json",
        "vaitro": "VT12 - Tầng Quy Tụ",
        "tieude": "TP44 – Không Lạc Đường",
        "phu_de": "Pháp gom người – không để ai lạc.",
        "noi_dung": "<p>Danh hiệu là nơi quy về – người tán loạn cũng được gom về pháp.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp45.json",
        "vaitro": "VT13 - Tầng Bản Nguyện",
        "tieude": "TP45 – Pháp Nguyện Giữ",
        "phu_de": "Không cần lý do – chỉ vì nguyện mà giữ.",
        "noi_dung": "<p>Tâm không còn vì hiểu, vì đúng sai – chỉ còn vì đại nguyện giữ một câu danh hiệu này.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp46.json",
        "vaitro": "VT13 - Tầng Bản Nguyện",
        "tieude": "TP46 – Không Cần Gặp",
        "phu_de": "Không gặp ai – vẫn giữ được nguyện.",
        "noi_dung": "<p>Dù không có minh sư – không gặp bạn đồng tu – vẫn giữ pháp vì nguyện ban đầu đã phát.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp47.json",
        "vaitro": "VT8 - Tầng Kết Nối / Vá Lưới",
        "tieude": "TP47 – Vá Pháp",
        "phu_de": "Pháp bị rách – tâm giữ lại đường.",
        "noi_dung": "<p>Danh hiệu như sợi chỉ nối các mạch pháp bị đứt – không cần khéo vá – chỉ cần giữ đúng hướng về.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp48.json",
        "vaitro": "VT13 - Tầng Bản Nguyện",
        "tieude": "TP48 – Không Thối Chuyển",
        "phu_de": "Dù gì xảy ra – không lui danh hiệu.",
        "noi_dung": "<p>Dù bị hiểu lầm – bị tổn thương – pháp không rời – vì đại nguyện vẫn giữ một câu này.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp49.json",
        "vaitro": "VT14 - Tầng Siêu Việt",
        "tieude": "TP49 – Không Cần Gọi",
        "phu_de": "Không cần gọi danh – danh vẫn vận hành.",
        "noi_dung": "<p>Không cần nhớ, không cần miệng đọc – danh hiệu vẫn tự vận hành trong tầng sóng vô ngôn.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp50.json",
        "vaitro": "VT14 - Tầng Siêu Việt",
        "tieude": "TP50 – Không Cần Người",
        "phu_de": "Không cần người hành – pháp vẫn trụ.",
        "noi_dung": "<p>Khi tất cả không còn – danh hiệu vẫn hiện. Pháp không phụ thuộc người – chỉ cần nguyện lực Phật tồn tại.</p><p>Nam mô A Di Đà Phật</p>"
    },
      {
        "filename": "tp51.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP51 – Trạm Mới 51",
        "phu_de": "Mở rộng pháp trạm mới, tiếp nối dòng pháp bất động.",
        "noi_dung": "<p>Điểm nhấn pháp trạm 51, danh hiệu giữ nguyên: Nam mô A Di Đà Phật, gợi ý thực hành giữ tâm bất động, không dao động.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp52.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP52 – Trạm Mới 52",
        "phu_de": "Trạm pháp mở rộng, duy trì sóng pháp vững bền.",
        "noi_dung": "<p>Khuyến cáo niệm danh hiệu liên tục, pháp trạm 52 giữ tinh thần tinh khiết, tập trung vào an trú tâm.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp53.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP53 – Trạm Mới 53",
        "phu_de": "Đưa pháp đến với tầng sóng sâu hơn.",
        "noi_dung": "<p>Tĩnh lặng trong từng bước niệm, duy trì tín hiệu danh hiệu chuẩn xác, pháp trạm 53 vận hành thuần khiết.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp54.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP54 – Trạm Mới 54",
        "phu_de": "Pháp trạm hỗ trợ niệm Phật và giữ chánh niệm.",
        "noi_dung": "<p>Định tâm, quán niệm từng hơi thở, giữ danh hiệu bền vững trong tâm, trạm 54 nhấn mạnh chánh niệm.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp55.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP55 – Trạm Mới 55",
        "phu_de": "Trạm pháp mở rộng kết nối ánh sáng pháp.",
        "noi_dung": "<p>Khơi dậy lòng tin và trì niệm, phát triển sóng pháp mạnh mẽ, giữ sự an lạc sâu xa.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp56.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP56 – Trạm Mới 56",
        "phu_de": "Nâng cao trạng thái tỉnh thức và an trú.",
        "noi_dung": "<p>Thúc đẩy niệm Phật thường xuyên, chuyển hóa tâm mê về ánh sáng, pháp trạm 56 vững chắc.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp57.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP57 – Trạm Mới 57",
        "phu_de": "Trạm pháp kết nối các tầng niệm sâu sắc.",
        "noi_dung": "<p>Dẫn dắt tâm vào trạng thái an ổn, duy trì sóng danh hiệu không gián đoạn, phát huy pháp lực trạm 57.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp58.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP58 – Trạm Mới 58",
        "phu_de": "Mở rộng mạng lưới pháp niệm liên tục.",
        "noi_dung": "<p>Giữ niệm Phật liên tục, vững chắc, hòa nhập ánh sáng Phật trong tâm, pháp trạm 58 vận hành thanh tịnh.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp59.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP59 – Trạm Mới 59",
        "phu_de": "Trạm pháp tăng cường năng lượng niệm Phật.",
        "noi_dung": "<p>Bền bỉ trong niệm danh hiệu, duy trì tâm bất động, tĩnh lặng, sóng pháp trạm 59 thuần khiết.</p><p>Nam mô A Di Đà Phật</p>"
    },
    {
        "filename": "tp60.json",
        "vaitro": "VT99 - Mở Rộng / Dự Phòng",
        "tieude": "TP60 – Trạm Mới 60",
        "phu_de": "Hoàn thiện mở rộng pháp trạm, giữ sóng pháp bền lâu.",
        "noi_dung": "<p>Giữ sự kiên định trong niệm Phật, phát triển sóng pháp vững mạnh, trạm 60 kết thúc mở rộng chuỗi pháp.</p><p>Nam mô A Di Đà Phật</p>"
    }
]

# Map vai trò sang tầng
role_to_tang = {
    "VT1": "T1 - Tầng Dẫn Pháp",
    "VT2": "T2 - Tầng An Trụ",
    "VT3": "T3 - Tầng Buông Nhẹ",
    "VT4": "T4 - Tầng Ảnh Dấu",
    "VT5": "T5 - Tầng Lặng Vận",
    "VT6": "T6 - Tầng Kết Sâu",
    "VT7": "T7 - Tầng Hành Động",
    "VT8": "T8 - Tầng Kết Nối",
    "VT9": "T9 - Tầng Pháp Động",
    "VT10": "T10 - Tầng Định Hình",
    "VT11": "T11 - Tầng Lan Tỏa",
    "VT12": "T12 - Tầng Quy Tụ",
    "VT13": "T13 - Tầng Bản Nguyện",
    "VT14": "T14 - Tầng Siêu Việt",
    "VT99": "T99 - Mở Rộng / Dự Phòng"
}

output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

for item in data_list:
    vt_code = item["vaitro"].split(" ")[0]
    tang_value = role_to_tang.get(vt_code, "T0 - Không xác định")
    path = os.path.join(output_dir, item["filename"])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({
            "tang": tang_value,
            "tieude": item["tieude"],
            "phu_de": item["phu_de"],
            "noi_dung": item["noi_dung"]
        }, f, ensure_ascii=False, indent=2)

print("✅ Đã tạo xong file JSON với key 'tang'.")

@echo off
cd /d %~dp0
echo ====================================
echo 🔄 ĐANG ĐẨY DỮ LIỆU PHÁP LÊN GITHUB...
echo ====================================

git add .
echo ✅ Đã add tất cả thay đổi.

git commit -m "auto push DataPhap (CuLi/TP)"
echo ✅ Commit xong.

git push
echo 🚀 Đã push lên GitHub!

echo ====================================
echo 🧘 XONG! MỞ JSDELIVR KIỂM TRA CDN NHÉ
echo ====================================
pause
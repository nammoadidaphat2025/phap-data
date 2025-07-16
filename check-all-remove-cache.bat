@echo off
setlocal enabledelayedexpansion

:: ==== Config ====
set BASE_PURGE=https://purge.jsdelivr.net/gh/nammoadidaphat2025/phap-data@latest
set BASE_CDN=https://cdn.jsdelivr.net/gh/nammoadidaphat2025/phap-data@latest

:: ==== TP1 -> TP60 ====
echo 🔁 Purging TP1 → TP60...
for /l %%i in (1,1,60) do (
    set "id=tp%%i"
    curl -s "!BASE_PURGE!/data-tp/!id!.json" > nul
    curl -s "!BASE_CDN!/data-tp/!id!.json?v=!random!" > nul
    echo ✅ Done !id!
)

:: ==== Cu Li 1 -> 21 ====
echo 🔁 Purging Cu Li 1 → 21...
for /l %%i in (1,1,21) do (
    set "id=tp-culi-%%i"
    curl -s "!BASE_PURGE!/data-tp-culi/!id!.json" > nul
    curl -s "!BASE_CDN!/data-tp-culi/!id!.json?v=!random!" > nul
    echo ✅ Done !id!
)

echo 💡 Xong hết rồi thím! Nhớ F5 lại trình duyệt nếu chưa thấy thay đổi.
pause

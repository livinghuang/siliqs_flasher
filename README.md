# Siliqs Flasher

Siliqs Flasher is a user-friendly macOS GUI application designed for flashing ESP32 firmware. It supports multiple ESP32 variants, including ESP32, ESP32-C3, and ESP32-S3. This tool simplifies the flashing process and provides a clean interface for developers.

---

## Features

- **Graphical User Interface**: Built using PyQt6, offering an intuitive and easy-to-use design.
- **Multi-Device Support**: Supports flashing for ESP32, ESP32-C3, and ESP32-S3.
- **Serial Port Selection**: Automatically detects available serial ports for easy setup.
- **Firmware File Selection**: Allows users to browse and select firmware files.
- **Real-Time Flashing Logs**: Displays flashing logs in real-time for debugging and monitoring.
- **Custom Icon**: Includes a professionally designed application icon.

---

## Installation

1. **Download the Application**:
   - Download the `.dmg` or `.zip` file from the repository.

2. **Install the Application**:
   - For `.dmg`:
     - Double-click the DMG file to open it.
     - Drag the `Siliqs Flasher.app` to the `Applications` folder.
   - For `.zip`:
     - Unzip the file and move `Siliqs Flasher.app` to the `Applications` folder.

3. **Open the Application**:
   - Right-click `Siliqs Flasher.app` and click **Open** (if Gatekeeper blocks it).

---

## Requirements

- macOS 11.0 or later.
- Python 3.10 or above (if running from source).
- Dependencies:
  - `PyQt6`
  - `esptool`

---

## How to Use

1. **Select Serial Port**:
   - Choose the appropriate serial port from the dropdown menu.

2. **Select Firmware File**:
   - Click the "Browse" button to locate and select the firmware `.bin` file.

3. **Select Chip Type**:
   - Choose your ESP32 chip variant (ESP32, ESP32-C3, or ESP32-S3) from the dropdown menu.

4. **Start Flashing**:
   - Click the "Flash ESP32" button to begin the flashing process.
   - Monitor real-time logs for progress and debugging.

5. **Completion**:
   - Once the process is complete, a success message will appear.

---

## Development Setup

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:YOUR_USERNAME/siliqs_flasher.git
   cd siliqs_flasher
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python sqflasher.py
   ```

---

## Build Instructions

To build the standalone application, use **PyInstaller**:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the Application:
   ```bash
   pyinstaller --onefile --windowed \
       --icon=MyIcon.icns \
       --hidden-import=esptool \
       --hidden-import=serial.tools.list_ports \
       --add-data "/Users/your_user/.venv/bin/esptool.py:." \
       sqflasher.py
   ```

3. Locate the Built App:
   - The `.app` file will be in the `dist/` directory.

---

## Troubleshooting

### macOS Gatekeeper Blocking the App
- Right-click the app and select **Open** to bypass Gatekeeper.
- If necessary, go to **System Preferences > Security & Privacy > General** and click **Open Anyway**.

### Missing Dependencies
- Ensure `esptool.py` is correctly installed and included in the build.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Credits

- **Development**: [Your Name]
- **Icon Design**: Siliqs Design Team
- **Libraries Used**:
  - PyQt6
  - esptool

---

For support or questions, contact [your_email@example.com].
# Siliqs 燒錄工具

Siliqs 燒錄工具是一款簡單易用的 macOS 圖形化應用程式，用於燒錄 ESP32 韌體。它支援多種 ESP32 晶片型號，包括 ESP32、ESP32-C3 和 ESP32-S3，讓開發者輕鬆完成燒錄工作。

---

## 功能特色

- **圖形化介面**：基於 PyQt6，提供直觀易用的設計。
- **多設備支援**：支援 ESP32、ESP32-C3 和 ESP32-S3 的燒錄。
- **串口選擇**：自動偵測可用串口，簡化設定流程。
- **韌體檔案選擇**：允許使用者瀏覽並選擇韌體檔案。
- **即時燒錄日誌**：即時顯示燒錄日誌，便於除錯與監控。
- **自訂圖示**：包含專業設計的應用程式圖示。

---

## 安裝方式

1. **下載應用程式**：
   - 從儲存庫下載 `.dmg` 或 `.zip` 文件。

2. **安裝應用程式**：
   - 如果是 `.dmg`：
     - 雙擊 DMG 文件以開啟。
     - 將 `Siliqs Flasher.app` 拖動到 `Applications` 資料夾。
   - 如果是 `.zip`：
     - 解壓縮文件，將 `Siliqs Flasher.app` 移動到 `Applications` 資料夾。

3. **開啟應用程式**：
   - 右鍵點擊 `Siliqs Flasher.app`，選擇 **開啟**（如果被 Gatekeeper 阻擋）。

---

## 系統需求

- macOS 11.0 或更新版本。
- Python 3.10 或更高版本（若從原始碼執行）。
- 依賴項目：
  - `PyQt6`
  - `esptool`

---

## 使用說明

1. **選擇串口**：
   - 從下拉選單中選擇適當的串口。

2. **選擇韌體檔案**：
   - 點擊「瀏覽」按鈕選擇 `.bin` 韌體文件。

3. **選擇晶片類型**：
   - 從下拉選單中選擇 ESP32 晶片型號（ESP32、ESP32-C3 或 ESP32-S3）。

4. **開始燒錄**：
   - 點擊「燒錄 ESP32」按鈕開始燒錄。
   - 即時監控日誌輸出，檢視燒錄進度。

5. **完成**：
   - 燒錄完成後，會顯示成功訊息。

---

## 開發環境設置

1. **克隆儲存庫**：
   ```bash
   git clone git@github.com:YOUR_USERNAME/siliqs_flasher.git
   cd siliqs_flasher
   ```

2. **建立虛擬環境**：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **安裝依賴項目**：
   ```bash
   pip install -r requirements.txt
   ```

4. **運行應用程式**：
   ```bash
   python sqflasher.py
   ```

---

## 建置說明

使用 **PyInstaller** 建置獨立應用程式：

1. 安裝 PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 建置應用程式：
   ```bash
   pyinstaller --onefile --windowed \
       --icon=MyIcon.icns \
       --hidden-import=esptool \
       --hidden-import=serial.tools.list_ports \
       --add-data "/Users/your_user/.venv/bin/esptool.py:." \
       sqflasher.py
   ```

3. 檢查輸出檔案：
   - `.app` 文件將位於 `dist/` 資料夾中。

---

## 問題排查

### macOS Gatekeeper 阻擋應用程式
- 右鍵點擊應用程式並選擇 **開啟**，以繞過 Gatekeeper。
- 如有需要，前往 **系統偏好設定 > 安全性與隱私 > 一般**，點擊 **仍要開啟**。

### 缺少依賴項
- 確保 `esptool.py` 已正確安裝並包含在建置中。

---

## 貢獻

歡迎貢獻！請 fork 本儲存庫，建立功能分支並提交 Pull Request。

---

## 授權

此專案基於 MIT 許可證。詳情請參閱 `LICENSE` 文件。

---

## 致謝

- **開發**：Your Name
- **圖示設計**：Siliqs 設計團隊
- **使用的函式庫**：
  - PyQt6
  - esptool

---

如有支援需求或疑問，請聯繫 [your_email@example.com]。

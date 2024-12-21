import sys
import os
import shutil
import subprocess
import serial.tools.list_ports
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QComboBox, QTextEdit
)
from PyQt6.QtCore import QThread, pyqtSignal


def get_esptool_path():
    """定位打包的 esptool.py 或系統中的 esptool.py"""
    if getattr(sys, 'frozen', False):
        # 當應用程式是由 PyInstaller 打包時
        base_path = sys._MEIPASS  # PyInstaller 提供的臨時目錄
        esptool_path = os.path.join(base_path, "esptool.py")
        if os.path.exists(esptool_path):
            return esptool_path
    else:
        # 在開發或虛擬環境中執行
        esptool_path = "/Users/living/code/siliqs_flasher/.venv/bin/esptool.py"
        if os.path.exists(esptool_path):
            return esptool_path

    raise FileNotFoundError("找不到 esptool.py，請確認已正確打包或安裝。")


class FlashThread(QThread):
    """Thread to handle the ESP32 flashing process."""
    output_signal = pyqtSignal(str)

    def __init__(self, chip_type: str, port: str, firmware: str):
        super().__init__()
        self.chip_type = chip_type
        self.port = port
        self.firmware = firmware
        self.esptool_path = get_esptool_path()

    def run(self):
        try:
            process = subprocess.Popen(
                [self.esptool_path, "--chip", self.chip_type, "--port", self.port, "write_flash", "0x1000", self.firmware],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            # Emit output line-by-line
            for line in process.stdout:
                self.output_signal.emit(line.strip())
            for line in process.stderr:
                self.output_signal.emit(line.strip())
        except Exception as e:
            self.output_signal.emit(f"錯誤：{str(e)}")


class ESP32Flasher(QWidget):
    """Main GUI for the ESP32 Flasher tool."""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the GUI layout and components."""
        self.setWindowTitle("ESP32 燒錄工具")
        layout = QVBoxLayout()

        # Serial Port Selector
        self.port_label = QLabel("串口 (Serial Port):")
        layout.addWidget(self.port_label)
        self.port_selector = QComboBox()
        self.refresh_serial_ports()
        layout.addWidget(self.port_selector)

        self.refresh_button = QPushButton("刷新串口 (Refresh Serial Ports)")
        self.refresh_button.clicked.connect(self.refresh_serial_ports)
        layout.addWidget(self.refresh_button)

        # Firmware File Selector
        self.file_label = QLabel("韌體檔案 (Firmware File):")
        layout.addWidget(self.file_label)
        self.file_input = QLineEdit()
        layout.addWidget(self.file_input)
        self.browse_button = QPushButton("瀏覽 (Browse)")
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        # Chip Type Selector
        self.chip_label = QLabel("晶片類型 (Chip Type):")
        layout.addWidget(self.chip_label)
        self.chip_selector = QComboBox()
        self.chip_selector.addItems(["esp32", "esp32c3", "esp32s3"])
        layout.addWidget(self.chip_selector)

        # Flash Button
        self.flash_button = QPushButton("開始燒錄 (Flash ESP32)")
        self.flash_button.clicked.connect(self.flash_esp32)
        layout.addWidget(self.flash_button)

        # Output Log
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def refresh_serial_ports(self):
        """Refresh the list of available serial ports."""
        self.port_selector.clear()
        ports = serial.tools.list_ports.comports()
        if ports:
            for port in ports:
                self.port_selector.addItem(f"{port.device} - {port.description}")
        else:
            self.port_selector.addItem("無可用串口 (No Available Ports)")

    def browse_file(self):
        """Open a file dialog to select a firmware file."""
        file_name, _ = QFileDialog.getOpenFileName(self, "選擇韌體檔案", "", "Binary Files (*.bin)")
        if file_name:
            self.file_input.setText(file_name)

    def flash_esp32(self):
        """Start the ESP32 flashing process."""
        port_info = self.port_selector.currentText()
        if " - " in port_info:
            port = port_info.split(" - ")[0]
        else:
            port = ""

        firmware = self.file_input.text()
        chip_type = self.chip_selector.currentText()

        if not port or not firmware:
            self.output_text.append("錯誤：請指定串口和韌體檔案！")
            return

        self.flash_button.setEnabled(False)
        self.output_text.append("開始燒錄...")

        # Start Flashing Thread
        self.flash_thread = FlashThread(chip_type, port, firmware)
        self.flash_thread.output_signal.connect(self.update_output)
        self.flash_thread.finished.connect(self.flash_done)
        self.flash_thread.start()

    def update_output(self, text: str):
        """Update the output log with text."""
        self.output_text.append(text)

    def flash_done(self):
        """Handle the completion of the flashing process."""
        self.output_text.append("燒錄完成！")
        self.flash_button.setEnabled(True)


def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    flasher = ESP32Flasher()
    flasher.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

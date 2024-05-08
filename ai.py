import sys
from PySide6.QtWidgets import *
from ui_dialog import Ui_Dialog
import jieba

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choice = ""  # 用于存储选择框选择的内容
        self.explanation_words = []  # 存储注解词汇
        self.explanations = []  # 存储注解解释
        self.main_content = ""  # 初始化主要内容
        self.individual_chars_main = []  # 分词后的主要内容
        self.complete.setText("")  # 设置名为 complete 的 label 文本为空白
        self.progressBar.setValue(0)  # 初始化进度条为0
        self.init_slots()

    def init_slots(self):
        # 连接按钮信号到相应的槽函数
        self.start.clicked.connect(self.start_process)
        self.chushibiao.clicked.connect(self.load_chushibiao)
        self.grade.currentIndexChanged.connect(self.grade_changed)

    def grade_changed(self, index):
        # 当选择框的选项改变时，更新 self.choice
        self.choice = self.grade.currentText()

    def load_chushibiao(self):
        # 打开文件对话框，选择待注解的文本文件
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.main_content = file.read()
                self.individual_chars_main = list(jieba.cut_for_search(self.main_content))
            self.progressBar.setValue(66)  # 分词后将进度条设置为66%

    def start_process(self):
        # 检查是否选择了年级
        if not self.choice:
            QMessageBox.warning(self, "错误", "请选择年级")
            return

        # 根据选择的年级读取对应的注释数据库文件
        annotations_file = f"{self.choice}.txt"
        try:
            with open(annotations_file, 'r', encoding='utf-8') as file:
                lines = file.read().splitlines()
                self.explanation_words = []
                self.explanations = []
                for line in lines:
                    word, exp = line.split(':', 1)  # 使用':'作为分词标准，且只分割一次
                    self.explanation_words.append(word)
                    self.explanations.append(exp)
                self.progressBar.setValue(33)  # 分词后将进度条设置为33%

            # 检查是否有 main_content
            if not self.main_content:
                QMessageBox.warning(self, "错误", "请先选择待注解的文本文件")
                return

            # 处理文本内容
            for i, word in enumerate(self.explanation_words, start=1):
                if word in self.individual_chars_main:
                    self.main_content = self.main_content.replace(word, f"{i}. {word}", 1)

            # 添加注解到文本末尾
            self.main_content += '\n'.join(f"{i}. {word}: {exp}" for i, (word, exp) in enumerate(zip(self.explanation_words, self.explanations), start=1))

            # 保存文件
            with open('注释版.txt', 'w', encoding='utf-8') as file:
                file.write(self.main_content)

            # 更新进度条为100%
            self.progressBar.setValue(100)
            self.complete.setText("完成！")  # 保存文件后设置名为 complete 的 label 文本为“完成！”

        except FileNotFoundError:
            QMessageBox.warning(self, "错误", f"文件未找到: {annotations_file}")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载注释数据库时出错: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
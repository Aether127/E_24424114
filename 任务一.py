import sys
from PySide6.QtWidgets import *
import jieba
from jiayan import CRFSentencizer, load_lm
from translate import Translator

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)  # 初始化进度条为0
        self.init_slots()
        self.main_content = ""  # 初始化主要内容
        self.explanation_words = []  # 存储注解词汇
        self.explanations = []  # 存储注解解释
        self.individual_chars_main = []  # 分词后的主要内容
        self.complete.setText("")  # 设置名为 complete 的 label 文本为空白
        self.load_explanation_db()  # 加载注释数据库

        # 加载语言模型和分句模型
        self.lm_path = 'path_to_jiayan_lm.klm'
        self.cut_model_path = 'path_to_cut_model'
        self.lm = load_lm(self.lm_path)
        self.sentencizer = CRFSentencizer(self.lm)
        self.sentencizer.load(self.cut_model_path)


    def init_slots(self):
        # 连接按钮信号到相应的槽函数
        self.chushibiao.clicked.connect(self.load_chushibiao)
        self.start.clicked.connect(self.start_process)

    def load_explanation_db(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.read().splitlines()
                for line in lines:
                    word, exp = line.split(':', 1)  # 使用':'作为分词标准，且只分割一次
                    self.explanation_words.append(word)
                    self.explanations.append(exp)
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载注释数据库时出错: {e}")
            return


# 假设我们有一个txt文件，包含不同年级的注释与翻译
annotations_file = 'annotations.txt'

# 加载注释数据
with open(annotations_file, 'r', encoding='utf-8') as f:
    annotations_data = txt.load(f)

#
根据学生年级和文言文内容检索注释与翻译
def get_annotation_and_translation(class_grade, text_content):
    # 这里需要根据实际数据结构进行检索
    for grade_data in annotations_data:
        if grade_data['grade'] == class_grade:
            for item in grade_data['items']:
                if text_content in item['text']:
                    return item['annotation'], item['translation']
    return None, None

class_grade = []
text_content = []

annotation, translation = get_annotation_and_translation(class_grade, text_content)

if annotation and translation:
    print(f"注释: {annotation}")
    print(f"翻译: {translation}")
else:
    print("没有找到对应的注释与翻译。")

    def load_chushibiao(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.main_content = content  # 将读取的内容赋值给变量
                self.individual_chars_main = list(jieba.cut_for_search(self.main_content))
                self.progressBar.setValue(50)  # 分词后将进度条设置为50%
        except FileNotFoundError:
            QMessageBox.warning(self, "错误", "文件未找到。")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"发生错误: {e}")

    def start_process(self):
        try:
            if not (self.main_content and self.explanation_words and self.explanations):
                QMessageBox.warning(self, "错误", "缺少文件")
                return

            # 处理文本内容
            for i, word in enumerate(self.explanation_words, start=1):
                if word in self.individual_chars_main:
                    self.main_content = self.main_content.replace(word, f"{i}. {word}", 1)
                else:
                    self.explanation_words.remove(word)
                    self.explanations.remove(self.explanations[i-1])

            # 添加注解到文本末尾
            self.main_content += '\n'.join(f"{i}. {word}: {exp}" for i, (word, exp) in enumerate(zip(self.explanation_words, self.explanations), start=1))

            # 翻译每个句子
            translator = Translator(to_lang='zh-cn')  # 确保正确设置了目标语言
            sentences = self.sentencizer.sentencize(self.main_content)
            translated_texts = [translator.translate(sentence) for sentence in sentences]

            # 保存文件
            with open('注释版.txt', 'w', encoding='utf-8') as file:
                file.write(self.main_content)

            # 输出翻译结果
            for original, translated in zip(sentences, translated_texts):
                print(f"原文: {original}\n翻译: {translated}\n")
            # 更新进度条为100%
            self.progressBar.setValue(100)  # 更新进度条为100%
            self.complete.setText("完成！")  # 保存文件后设置名为 complete 的 label 文本为“完成！”
        except Exception as e:
            QMessageBox.warning(self, "错误", f"处理过程中发生错误: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

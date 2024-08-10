import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QTextEdit, QPushButton, QGridLayout

class CourtCaseSummarizer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Main layout
        mainLayout = QGridLayout()

        # List of Court Cases
        self.caseList = QListWidget()
        self.caseList.addItems([
            "1. G.R. 174842; December 1, 2010",
            "2. G.R. 189359; January 20, 2014",
            "3. G.R. 193707; April 15, 2013",
            # Add more cases as needed
        ])
        mainLayout.addWidget(self.caseList,0,0)

        # Original Court Case
        originalCaseLayout = QVBoxLayout()
        originalCaseLabel = QLabel("Original Court Case")
        self.originalCaseText = QTextEdit()
        originalCaseLayout.addWidget(originalCaseLabel)
        originalCaseLayout.addWidget(self.originalCaseText)
        originalCaseLayout.addWidget(QLabel("Word Count: 1024"))

        mainLayout.addLayout(originalCaseLayout, 0,1)

        # Summarized Court Case
        summarizedCaseLayout = QVBoxLayout()
        summarizedCaseLabel = QLabel("Summarized Court Case")
        self.summarizedCaseText = QTextEdit()
        summarizedCaseLayout.addWidget(summarizedCaseLabel)
        summarizedCaseLayout.addWidget(self.summarizedCaseText)
        summarizedCaseLayout.addWidget(QLabel("Word Count: 512"))

        mainLayout.addLayout(summarizedCaseLayout, 0,2)

        # Bottom Buttons
        buttons1Layout = QHBoxLayout()
        addButton = QPushButton("Add Case")
        removeButton = QPushButton("Remove Case")
        buttons1Layout.addWidget(addButton)
        buttons1Layout.addWidget(removeButton)

        buttons2Layout = QHBoxLayout()
        uploadButton = QPushButton("Upload Case")
        deleteButton = QPushButton("Delete Case")
        buttons2Layout.addWidget(uploadButton)
        buttons2Layout.addWidget(deleteButton)

        buttons3Layout = QHBoxLayout()
        exportButton = QPushButton("Export PDF")
        buttons3Layout.addWidget(exportButton)

        mainLayout.addLayout(buttons1Layout, 1, 0)
        mainLayout.addLayout(buttons2Layout, 1, 1)
        mainLayout.addLayout(buttons3Layout, 1, 2)

        # Set the layout
        self.setLayout(mainLayout)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Philippine Court Case Summarizer')

def main():
    app = QApplication(sys.argv)
    ex = CourtCaseSummarizer()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

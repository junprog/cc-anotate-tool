import platform
import tkinter as tk

class ToolWindow():
    def __init__(self, tk_instance, os_info):
        self.os_info = os_info
        self.tk_instance = tk_instance
        
        self.tk_instance.title('VIP Crowd Counting Anotation Tool')

    def select_dataset_dir(self):
        ## データセットのディレクトリ選択

        #入力欄作成
        self.input_box = tk.Entry(width=40)
        self.input_box.place(x=10, y=100)

        #ラベルの作成
        self.input_label = tk.Label(text='参照するデータセットのディレクトリを選択してください。')
        self.input_label.place(x=10, y=70)

        #ボタンの作成
        self.button = tk.Button(text="参照",command=self._file_select)
        self.button.place(x=10, y=130)

    def _file_select(self):
        idir = 'C:/Users/jyuny/OneDrive/ドキュメント/archive/ShanghaiTech/part_B/test_data/images'
        filetype = [("テキスト","*.txt"), ("音楽","*.mp3"), ("すべて","*")]
        file_path = tk.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
        self.input_box.insert(tk.END, file_path)

    def maximize_window(self):
        if 'Windows' in self.os_info:
            self.tk_instance.state('zoomed')
        else:
            self.tk_instance.attributes("-zoomed", "1")
        
    def mainloop(self):
        self.tk_instance.mainloop()

if __name__ == '__main__':
    ## Create tKinter Instance
    window = ToolWindow(tk.Tk(), platform.system())

    ## ウィンドウ最大化
    window.maximize_window()

    ## 参照ディレクトリ選択
    window.select_dataset_dir()

    ## メインループ
    window.mainloop()
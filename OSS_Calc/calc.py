import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")

        self.expression = ""
        self.exchange_rate = 910  # 1 AUD = 910 KRW

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 숫자 및 연산자 버튼
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        # 환율 버튼 추가 (AUD → KRW, KRW → AUD)
        rate_frame = tk.Frame(root)
        rate_frame.pack(expand=True, fill="both")

        btn_aud_to_krw = tk.Button(
            rate_frame,
            text="AUD → KRW",
            font=("Arial", 14),
            command=self.convert_aud_to_krw
        )
        btn_aud_to_krw.pack(side="left", expand=True, fill="both")

        btn_krw_to_aud = tk.Button(
            rate_frame,
            text="KRW → AUD",
            font=("Arial", 14),
            command=self.convert_krw_to_aud
        )
        btn_krw_to_aud.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def convert_aud_to_krw(self):
        try:
            amount = float(self.entry.get())
            result = amount * self.exchange_rate
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(round(result, 2)))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "에러")

    def convert_krw_to_aud(self):
        try:
            amount = float(self.entry.get())
            result = amount / self.exchange_rate
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(round(result, 4)))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "에러")

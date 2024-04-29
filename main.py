import customtkinter as ctk
import rockpaperscissors as rps

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # sets the basic properties of the window
        self.title("Rock, Paper, Scissors")
        self.geometry("500x300")
        self.resizable(False, False)

        # creates constants of usable fonts
        self.FONT_CGOTHIC_BOLD_BIG = ("Century Gothic", 24, "bold")
        self.FONT_CGOTHIC_BOLD_SMALL = ("Century Gothic", 18, "bold")
        self.FONT_CGOTHIC_NORMAL = ("Century Gothic", 18, "normal")

        # creates main frame and configure its rows and columns
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        for row in range(5):
            if row == 0:
                self.main_frame.grid_rowconfigure(row, weight=1, pad=10)
            else:
                self.main_frame.grid_rowconfigure(row, weight=2, pad=10)

        for col in range(3):
            self.main_frame.grid_columnconfigure(col, weight=1, pad=20)
        
        # creates appearance modes option menu
        self.appearance_modes_menu = ctk.CTkOptionMenu(self.main_frame, values=["System", "Light", "Dark"], font=self.FONT_CGOTHIC_NORMAL, command=self.change_appearance_mode)
        self.appearance_modes_menu.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ne")
        
        # creates title label
        self.title_label = ctk.CTkLabel(self.main_frame, text="Rock, Paper, Scissors", font=self.FONT_CGOTHIC_BOLD_BIG)
        self.title_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # creates actions label that will be replaced with the actions chosen by the user and the computer
        self.actions_label = ctk.CTkLabel(self.main_frame, text="", font=self.FONT_CGOTHIC_NORMAL)
        self.actions_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # creates result label that will be replaced with the winner of the game
        self.result_label = ctk.CTkLabel(self.main_frame, text="", font=self.FONT_CGOTHIC_NORMAL)
        self.result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # creates buttons for the rock, paper and scissors actions
        self.rock_button = ctk.CTkButton(self.main_frame, text="Rock", font=self.FONT_CGOTHIC_BOLD_SMALL, command=lambda:self.action_button(rps.Action.rock))
        self.rock_button.grid(row=4, column=0, padx=10, pady=10)

        self.paper_button = ctk.CTkButton(self.main_frame, text="Paper", font=self.FONT_CGOTHIC_BOLD_SMALL, command=lambda:self.action_button(rps.Action.paper))
        self.paper_button.grid(row=4, column=1, padx=10, pady=10)

        self.scissors_button = ctk.CTkButton(self.main_frame, text="Scissors", font=self.FONT_CGOTHIC_BOLD_SMALL, command=lambda:self.action_button(rps.Action.scissors))
        self.scissors_button.grid(row=4, column=2, padx=10, pady=10)
    
    # displays the winner
    def action_button(self, user_action):
        computer_action = rps.get_computer_action()
        result = rps.determine_winner(user_action, computer_action)
        self.result_label.configure(text=result)
        self.actions_label.configure(text=f"You: {rps.get_action_name(user_action)};  Computer: {rps.get_action_name(computer_action)}")
    
    def change_appearance_mode(self, appearance_mode):
        ctk.set_appearance_mode(appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
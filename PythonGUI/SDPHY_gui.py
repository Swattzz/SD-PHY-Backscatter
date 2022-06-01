from msilib.schema import TextStyle
from tkinter import *
from scipy.fftpack import shift
from setuptools import Command


root = Tk()
root.title('SD-PHY tool')
#style = ttk.Style(root)
#ttk.Style().theme_names()
#style.theme_use('clam')

#Labels
Label(root, text = "SDPHY Parameter Calculator", font=("Arial",20)).grid(row = 0, column = 1,columnspan=2,padx=10)

# Text input part 1 (sampling frequency part)
Label(root, text = "Rate Generation", font=("Calibri",15)).grid(row = 1, column = 1,columnspan=1)

Label(root, text = "Sampling Frequency (MHz)", font=("Calibri",15)).grid(row = 2, column = 0)
fs = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
fs.grid(row = 2, column=1)

Label(root, text = "Synchronization Clock (MHz)", font=("Calibri",15)).grid(row = 3, column = 0)
sync_clk = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
sync_clk.grid(row = 3, column=1)

# Text input part 2 (shift frequency)
Label(root, text = "IF Frequency Generation", font=("Calibri",15)).grid(row = 4, column = 1,columnspan=1)

Label(root, text = "Shift Frequency 0 (MHz)", font=("Calibri",15)).grid(row = 5, column = 0)
shift_freq_0 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
shift_freq_0.grid(row = 5, column=1)

Label(root, text = "Shift Frequency 1 (MHz)", font=("Calibri",15)).grid(row = 6, column = 0)
shift_freq_1 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
shift_freq_1.grid(row = 6, column=1)

# Text input part 3 (sync part)
Label(root, text = "Synchronization Function", font=("Calibri",15)).grid(row = 7, column = 1,columnspan=1)

Label(root, text = "Sync. Pattern (16bits)", font=("Calibri",15)).grid(row = 8, column = 0)
sync_pattern = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
sync_pattern.grid(row = 8, column=1)

Label(root, text = "Sync. Mask (16bits)", font=("Calibri",15)).grid(row = 9, column = 0)
sync_mask = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
sync_mask.grid(row = 9, column=1)

# Text input part 4 (length control)
Label(root, text = "Length Control", font=("Calibri",15)).grid(row = 10, column = 1,columnspan=1)

Label(root, text = "Samples per symbol (<64,<2^16)", font=("Calibri",15)).grid(row = 11, column = 0)
sym_len = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
sym_len.grid(row = 11, column=1)

Label(root, text = "Length of data frame (<1024)", font=("Calibri",15)).grid(row = 12, column = 0)
data_len = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
data_len.grid(row = 12, column=1)

# Text input 4.5 Mode selection
Label(root, text="Mode (0/1)", font=("Calibri",15)).grid(row = 1, column = 2)
mode = Entry(root, width = 10, borderwidth=3, font=("Calibri",15))
mode.grid(row = 1, column=3)


# Text input part 5 (Generic modulator number 0)
Label(root, text = "Basic Modulator (Mode=0)", font=("Calibri",15)).grid(row = 2, column = 3,columnspan=1)

Label(root, text="Symbol 0", font=("Calibri",15)).grid(row = 3, column = 2)
symbol0 = Entry(root, width = 25, borderwidth=3, font=("Calibri",15))
symbol0.grid(row = 3, column=3)

Label(root, text="Symbol 1", font=("Calibri",15)).grid(row = 4, column = 2)
symbol1 = Entry(root, width = 25, borderwidth=3, font=("Calibri",15))
symbol1.grid(row = 4, column=3)

# Text input part 6 (Generic modulator number 1)
Label(root, text = "Advanced Modulator (Mode=1)", font=("Calibri",15)).grid(row = 5, column = 3,columnspan=1)

Label(root, text = "A0 parameter (*2*pi)", font=("Calibri",15)).grid(row = 6, column = 2)
a0 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
a0.grid(row = 6, column=3)

Label(root, text = "A1 parameter (*fs/2^16)", font=("Calibri",15)).grid(row = 7, column = 2)
a1 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
a1.grid(row = 7, column=3)

Label(root, text = "A2 parameter (2^16/2^SF)", font=("Calibri",15)).grid(row = 8, column = 2)
a2 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
a2.grid(row = 8, column=3)

Label(root, text = "B0 parameter (*2*pi)", font=("Calibri",15)).grid(row = 9, column = 2)
b0 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
b0.grid(row = 9, column=3)

Label(root, text = "B1 parameter (*fs/2^16)", font=("Calibri",15)).grid(row = 10, column = 2)
b1 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
b1.grid(row = 10, column=3)

Label(root, text = "B2 parameter (2^16/2^SF)", font=("Calibri",15)).grid(row = 11, column = 2)
b2 = Entry(root, width=25, borderwidth=3, font=("Calibri",15))
b2.grid(row = 11, column=3)


# Button to disable input from the wrong modualtor
def enter_mode():
    if int(mode.get()):
        symbol0.config(state = 'readonly')
        symbol1.config(state = 'readonly')
    else:
        symbol0.config(state = 'normal')
        symbol1.config(state = 'normal')
    if 1-int(mode.get()):
        a0.config(state = 'readonly')
        a1.config(state = 'readonly')
        a2.config(state = 'readonly')
        b0.config(state = 'readonly')
        b1.config(state = 'readonly')
        b2.config(state = 'readonly')
    else:
        a0.config(state = 'normal')
        a1.config(state = 'normal')
        a2.config(state = 'normal')
        b0.config(state = 'normal')
        b1.config(state = 'normal')
        b2.config(state = 'normal')    
Button(root, text="Apply mode (1)", font = ("Arial",15), command = enter_mode).grid(row = 13, column = 2)


# PHY parameter calculation
def on_click_gen_phy():
    disp_phy = Toplevel(root)
    disp_phy.geometry("700x600")
    disp_phy.title('PHY values')
    text = Text(disp_phy, width=100, height=50)
    text.pack()
    text.insert(INSERT, f'Wait, calculating PHY...\n----------------------------\n')
    # Calculate fs
    if fs.get() == '':
        text.insert(INSERT, f'Warning: no FS input.\n')
    else:
        fs_value = round(float(fs.get())/40 * 2**16)
        fs_value_print = '16\'d' + str(fs_value)
        text.insert(INSERT, f'PARAM FS: {fs_value_print}\n')
    # Calculate sync rate
    if sync_clk.get() == '':
        text.insert(INSERT, f'Warning: no Sync rate input.\n')
    else:
        sync_clk_value = round(float(sync_clk.get())/2 * 2**10)
        sync_clk_value_print = '10\'d' + str(sync_clk_value)
        text.insert(INSERT, f'PARAM SYNC_CLK: {sync_clk_value_print}\n')
    # Calculate shift frequency 0/1
    if shift_freq_0.get() == '' or shift_freq_1 == '':
        text.insert(INSERT, f'Warning: no IF frequency input.\n')
    else:
        shift_freq_0_value = round(float(shift_freq_0.get())/40 * 2**16)
        shift_freq_0_value_print = '10\'d' + str(shift_freq_0_value)
        shift_freq_1_value = round(float(shift_freq_1.get())/40 * 2**16)
        shift_freq_1_value_print = '10\'d' + str(shift_freq_1_value)
        text.insert(INSERT, f'PARAM IF freq 0: {shift_freq_0_value_print}\n')
        text.insert(INSERT, f'PARAM IF freq 1: {shift_freq_1_value_print}\n')
    # Calculate synchronization pattern and synchronization mask
    sp_tmp1 = sync_pattern.get()
    sm_tmp1 = sync_mask.get()
    sync_pattern_print = '16\'b' + sp_tmp1.zfill(16)
    sync_mask_print = '16\'b' + sm_tmp1.zfill(16)
    text.insert(INSERT, f'PARAM sync pattern (MSB first): {sync_pattern_print}\n')
    text.insert(INSERT, f'PARAM sync mask (MSB first): {sync_mask_print}\n')
    # Calculate samples per symbol and total number of symbols inside a frame
    if sym_len.get() == '' or data_len.get() == '':
        text.insert(INSERT, f'Warning: no symbol length or data length input.\n')
    else:
        sym_len_tmp = sym_len.get()
        data_len_tmp = data_len.get()
        sym_len_print = '16\'d' + sym_len_tmp
        data_len_print = '16\'d' + data_len_tmp
        text.insert(INSERT, f'PARAM symbol length: {sym_len_print}\n')
        text.insert(INSERT, f'PARAM data length: {data_len_print}\n')
    
    if sync_clk.get() == '':
        text.insert(INSERT, f'Warning: no Sync rate input.\n')
    else:
        sync_clk_value = round(float(sync_clk.get())/2 * 2**10)
        sync_clk_value_print = '10\'d' + str(sync_clk_value)
        text.insert(INSERT, f'PARAM SYNC_CLK: {sync_clk_value_print}\n')
    
    print(f'(Test)After click: {fs.get()}')

    
Button(root, text="Click to generate PHY (2)", font=("Arial",15), command=on_click_gen_phy).grid(row = 13, column = 3)


root.mainloop()
import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from math import *
set_dpi_awareness()

class main_frame(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)
        self.title('Calculator')
        self.geometry('1200x700')
        container=ttk.Frame(self)
        container.grid(row=4, padx=20, pady=10, sticky='EW')
        Frame1 = frame1(self,container) # this is the frame1 of our calculator
        Frame2 = frame2(self, container) # this is frame2 of our calculator
        Frame3 = frame3(self, container) # this is the frame3 of our calculator

        self.frames=dict()

        Frame3.grid(row=0, column=0, sticky="NSEW")
        Frame2.grid(row=0, column=0, sticky="NSEW")
        Frame1.grid(row=0, column=0, sticky="NSEW")

        self.frames['Calculator']=Frame1
        self.frames['Scientific Calculator'] = Frame2
        self.frames['Unit conversion'] = Frame3




        menu_bar = tk.Menu()
        menu_bar.add_command(label='Calculator', command= lambda :self.frames['Calculator'].tkraise())
        menu_bar.add_command(label='Scientific Calculator', command=lambda :self.frames['Scientific Calculator'].tkraise())
        menu_bar.add_command(label='Unit Converter', command=lambda :self.frames['Unit conversion'].tkraise())


        self.config(menu=menu_bar)
        self.switch_frames('Calculator')


    def switch_frames(self,container):
        frame=self.frames[container]
        frame.tkraise()


class frame1(ttk.Frame):
    def __init__(self,container,controller,*args,**kwargs): # this is the first options frame in our calculator
        super().__init__(container,*args,**kwargs)
        self.value_curr=tk.StringVar()
        self.calculated_value=tk.StringVar()
        self.bind_all("<Key>", self.on_key_press)  # this function will bind all the keys to our canvas
        btn1=ttk.Button(self,text='1',command=self.btn1)
        btn2 = ttk.Button(self, text='2',command=self.btn2)
        btn3 = ttk.Button(self, text='3',command=self.btn3)
        btn4 = ttk.Button(self, text='4',command=self.btn4)
        btn5 = ttk.Button(self, text='5',command=self.btn5)
        btn6 = ttk.Button(self, text='6',command=self.btn6)
        btn7 = ttk.Button(self, text='7',command=self.btn7)
        btn8 = ttk.Button(self, text='8',command=self.btn8)
        btn9 = ttk.Button(self, text='9',command=self.btn9)
        btn0 = ttk.Button(self, text='0',command=self.btn0)
        result=ttk.Button(self,text='=',command=self.result_fn)

        add=ttk.Button(self,text='+',command=self.add_fn)
        subtract=ttk.Button(self,text='-',command=self.subtract_fn)
        multiply=ttk.Button(self,text='*',command=self.multiply_fn)
        divide=ttk.Button(self,text='/',command=self.divide_fn)
        modulous=ttk.Button(self,text='%',command=self.modulous_fn)
        left_bracket=ttk.Button(self,text='(',command=self.leftBracket_fn)
        right_bracket=ttk.Button(self,text=')',command=self.rightBracket_fn)
        power=ttk.Button(self,text='^',command=self.power_fn)
        clear=ttk.Button(self,text='C',command=self.clear_fn)
        dot=ttk.Button(self,text='.',command=self.dot_fn)

        input_Label=ttk.Label(self,text='INPUT:')
        output_label=ttk.Label(self,text='OUTPUT')
        input_entry=tk.Entry(self,textvariable=self.value_curr)
        output_entry = tk.Entry(self,text=self.calculated_value,state='disabled')
        input_Label.grid(row=1,column=5)
        input_entry.grid(row=1,column=6,pady=(0,20),ipadx=120,ipady=60)
        output_label.grid(row=2,column=5)
        output_entry.grid(row=2,column=6,ipadx=120,ipady=60)

        btn1.grid(row=3,column=0,padx=40,pady=10)
        btn2.grid(row=3, column=1, padx=40, pady=10)
        btn3.grid(row=3, column=2, padx=40, pady=10)
        btn4.grid(row=4, column=0, padx=40, pady=10)
        btn5.grid(row=4, column=1, padx=40, pady=10)
        btn6.grid(row=4, column=2, padx=40, pady=10)
        btn7.grid(row=5, column=0, padx=40, pady=10)
        btn8.grid(row=5, column=1, padx=40, pady=10)
        btn9.grid(row=5, column=2, padx=40, pady=10)
        clear.grid(row=7,column=2,padx=40,pady=10)
        dot.grid(row=6,column=0,padx=40,pady=10)
        btn0.grid(row=6,column=1,padx=40,pady=10)
        result.grid(row=6,column=2,padx=40,pady=10)
        add.grid(row=3,column=3,padx=40,pady=10)
        subtract.grid(row=3,column=4,padx=40,pady=10)
        multiply.grid(row=4,column=3,padx=40,pady=10)
        divide.grid(row=4,column=4,padx=40,pady=10)
        modulous.grid(row=5,column=3,padx=40,pady=10)
        power.grid(row=5,column=4,padx=40,pady=10)
        left_bracket.grid(row=6,column=3,padx=40,pady=10)
        right_bracket.grid(row=6,column=4,padx=40,pady=10)
         # to add key bindings in here

    def on_key_press(self,e):
        keyValue=e.keysym
        print(keyValue)
        if keyValue == '1':
            self.value_curr.set(value=self.value_curr.get()+'1')
        elif keyValue == '2':
            self.value_curr.set(value=self.value_curr.get()+'2')
        elif keyValue == '3':
            self.value_curr.set(value=self.value_curr.get()+'3')
        elif keyValue == '4':
            self.value_curr.set(value=self.value_curr.get()+'4')
        elif keyValue == '5':
            self.value_curr.set(value=self.value_curr.get()+'5')
        elif keyValue == '6':
            self.value_curr.set(value=self.value_curr.get()+'6')
        elif keyValue == '7':
            self.value_curr.set(value=self.value_curr.get()+'7')
        elif keyValue == '8':
            self.value_curr.set(value=self.value_curr.get()+'8')
        elif keyValue == '9':
            self.value_curr.set(value=self.value_curr.get()+'9')
        elif keyValue == '0':
            self.value_curr.set(value=self.value_curr.get()+'0')
        elif keyValue == 'plus':
            self.value_curr.set(value=self.value_curr.get()+'+')
        elif keyValue == 'minus':
            self.value_curr.set(value=self.value_curr.get()+'-')
        elif keyValue == 'slash':
            self.value_curr.set(value=self.value_curr.get()+'/')
        elif keyValue == 'percent':
            self.value_curr.set(value=self.value_curr.get()+'%')
        elif keyValue == 'asterisk':
            self.value_curr.set(value=self.value_curr.get()+'*')
        elif keyValue == 'Return' or keyValue == 'equal':
            self.result_fn()
        elif keyValue == 'period':
            self.value_curr.set(value=self.value_curr.get()+'.')
        elif keyValue == 'parenleft':
            self.value_curr.set(value=self.value_curr.get()+'(')
        elif keyValue == 'parenright':
            self.value_curr.set(value=self.value_curr.get()+')')





    def btn1(self):
        val=self.value_curr.get()
        val=val+'1'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn2(self):
        val = self.value_curr.get()
        val = val + '2'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn3(self):
        val = self.value_curr.get()
        val = val + '3'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn4(self):
        val = self.value_curr.get()
        val = val + '4'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn5(self):
        val = self.value_curr.get()
        val = val + '5'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn6(self):
        val = self.value_curr.get()
        val = val + '6'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn7(self):
        val = self.value_curr.get()
        val = val + '7'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn8(self):
        val = self.value_curr.get()
        val = val + '8'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn9(self):
        val = self.value_curr.get()
        val = val + '9'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn0(self):
        val = self.value_curr.get()
        val = val + '0'
        self.value_curr.set(val)
        print(self.value_curr.get())

    def add_fn(self):
        val = self.value_curr.get()
        val = val + '+'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def subtract_fn(self):
        val = self.value_curr.get()
        val = val + '-'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def multiply_fn(self):
        val = self.value_curr.get()
        val = val + '*'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def divide_fn(self):
        val = self.value_curr.get()
        val = val + '/'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def modulous_fn(self):
        val = self.value_curr.get()
        val = val + '%'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def power_fn(self):
        val = self.value_curr.get()
        val = val + '^'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def leftBracket_fn(self):
        val = self.value_curr.get()
        val = val + '('
        self.value_curr.set(val)
        print(self.value_curr.get())
    def rightBracket_fn(self):
        val = self.value_curr.get()
        val = val + ')'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def clear_fn(self):
        self.value_curr.set('')
        print(self.value_curr.get())
        print("Your string in erased")

    def dot_fn(self):
        val = self.value_curr.get()
        val = val + '.'
        self.value_curr.set(val)
        print(f'This is the current vakue {self.value_curr.get()}')

    def result_fn(self):
        value=eval(self.value_curr.get())
        self.value_curr.set(f'{value}')

        self.calculated_value.set(f'{value}')
        print(eval(self.value_curr.get()))
        # we can repeat this for each operation done so far to reduce a single operation complexity and a
        # single point of failure
    # adding ket bindings to these buttons











# modfiy the algo by following these steps
# kal dekhlena chotta sa kaam hai
class frame2(ttk.Frame): # this will be a more scientific calculator
    # ismei ek kaam ye hoskta hai ki equation mei function add karte jao aur phir eval use karlo
    def __init__(self,container,controller,*args,**kwargs): # this is the second options frame in our calculator
        super().__init__(container,*args,**kwargs)
        self.value_curr=tk.StringVar()
        self.degree_rad_val=tk.StringVar(value='Degree')
        self.calculated_value = tk.StringVar()
        self.bind_all("<Key>", self.on_key_press)  # this function will bind all the keys to our canvas
        btn1 = ttk.Button(self, text='1', command=self.btn1)
        btn2 = ttk.Button(self, text='2', command=self.btn2)
        btn3 = ttk.Button(self, text='3', command=self.btn3)
        btn4 = ttk.Button(self, text='4', command=self.btn4)
        btn5 = ttk.Button(self, text='5', command=self.btn5)
        btn6 = ttk.Button(self, text='6', command=self.btn6)
        btn7 = ttk.Button(self, text='7', command=self.btn7)
        btn8 = ttk.Button(self, text='8', command=self.btn8)
        btn9 = ttk.Button(self, text='9', command=self.btn9)
        btn0 = ttk.Button(self, text='0', command=self.btn0)
        clear = ttk.Button(self, text='C', command=self.clear_fn)
        dot = ttk.Button(self,text='.',command=self.dot_fn)
        result = ttk.Button(self, text='=', command=self.result_fn)

        input_Label = ttk.Label(self, text='INPUT:')
        output_label = ttk.Label(self, text='OUTPUT')
        input_entry = tk.Entry(self, textvariable=self.value_curr)
        output_entry = tk.Entry(self, text=self.calculated_value, state='disabled')
        input_Label.grid(row=0, column=8)
        input_entry.grid(row=0, column=9, pady=(0, 20), ipadx=100, ipady=60)
        output_label.grid(row=1, column=8)
        output_entry.grid(row=1, column=9, ipadx=100, ipady=60)

        btn1.grid(row=2, column=0, padx=10, pady=10)
        btn2.grid(row=2, column=1, padx=10, pady=10)
        btn3.grid(row=2, column=2, padx=10, pady=10)
        btn4.grid(row=3, column=0, padx=10, pady=10)
        btn5.grid(row=3, column=1, padx=10, pady=10)
        btn6.grid(row=3, column=2, padx=10, pady=10)
        btn7.grid(row=4, column=0, padx=10, pady=10)
        btn8.grid(row=4, column=1, padx=10, pady=10)
        btn9.grid(row=4, column=2, padx=10, pady=10)
        dot.grid(row=5, column=0, padx=10, pady=10)
        btn0.grid(row=5, column=1, padx=10, pady=10)
        result.grid(row=5, column=2, padx=10, pady=10)




        #natural functions
        add = ttk.Button(self, text='+',command=self.add_fn)
        subtract = ttk.Button(self, text='-',command=self.subtract_fn)
        multiply = ttk.Button(self, text='*',command=self.multiply_fn)
        divide = ttk.Button(self, text='/',command=self.divide_fn)
        mod = ttk.Button(self, text='%',command=self.modulous_fn)
        left = ttk.Button(self, text='(',command=self.leftBracket_fn)
        right = ttk.Button(self,text=')',command=self.rightBracket_fn)

        #power functions
        power_2 = ttk.Button(self,text="2^x",command=self.power_2)
        square = ttk.Button(self,text='X^2',command=self.square_fn)
        cube = ttk.Button(self,text='X^3',command=self.cube_fn)
        general_power = ttk.Button(self,text='X^Y',command=self.general_power)
        e_power=ttk.Button(self,text='e^x',command=self.e_power_fn)

        #trignometric functions
        sin_btn = ttk.Button(self,text='sin',command=self.sin_function)
        cos_btn = ttk.Button(self, text='cos',command=self.cos_function)
        tan_btn = ttk.Button(self, text='tan',command=self.tan_function)
        sin_inverse=ttk.Button(self,text='sin-1',command=self.sin_inverse_function)
        cos_inverse = ttk.Button(self, text='cos-1',command=self.cos_inverse_function)
        tan_inverse = ttk.Button(self, text='tan-1',command=self.tan_inverse_function)
        sinh_btn = ttk.Button(self, text='sinh',command=self.sinh_function)
        cosh_btn = ttk.Button(self, text='cosh',command=self.cosh_function)
        tanh_btn = ttk.Button(self, text='tanh',command=self.tanh_function)
        sinh_inverse = ttk.Button(self, text='sinh-1',command=self.sinh_inverse_fn)
        cosh_inverse = ttk.Button(self, text='cosh-1',command=self.cosh_inverse_fn)
        tanh_inverse = ttk.Button(self, text='tanh-1',command=self.tanh_inverse_fn)

        # degree -> radian button
        deg_rad = ttk.Button(self,textvariable=self.degree_rad_val,command=self.degree_rad)

        # log functions
        log_btn = ttk.Button(self,text='log',command=self.log_fn)
        ln_btn = ttk.Button(self,text='ln',command=self.ln_fn)

        #factorial button
        factorial_btn = ttk.Button(self,text='X!',command=self.factorial_fn)

        #constants

        pi_btn=ttk.Button(self,text='Pi',command=self.pi_fn)
        e_btn=ttk.Button(self,text='e',command=self.e_fn)

        #absolute

        abs_btn=ttk.Button(self,text='|X|',command=self.abs_fn)
        reciprocal=ttk.Button(self,text='1/X',command=self.rec_fn)

        # underRoot functions
        square_root=ttk.Button(self,text='squareRoot',command=self.squre_root_fn)
        cube_root = ttk.Button(self, text='cub3Root',command=self.cube_root_fn)
        general_root = ttk.Button(self, text='generalRoot')

        # row 8 buttons
        add.grid(row=2,column=3,padx=5,pady=10)
        subtract.grid(row=2,column=4,padx=5,pady=10)
        multiply.grid(row=2,column=5,padx=5,pady=10)
        divide.grid(row=2,column=6,padx=5,pady=10)
        mod.grid(row=2,column=7,padx=5,pady=10)
        left.grid(row=2,column=8,padx=5,pady=10)

        # row 10 buttons
        right.grid(row=3, column=3, padx=5, pady=10)
        square.grid(row=3, column=4, padx=5, pady=10)
        cube.grid(row=3, column=5, padx=5, pady=10)
        power_2.grid(row=3, column=6, padx=5, pady=10)
        e_power.grid(row=3, column=7, padx=5, pady=10)
        general_power.grid(row=3,column=8,padx=5,pady=10)

        # row 12 buttons
        sin_btn.grid(row=4, column=3, padx=5, pady=10)
        cos_btn.grid(row=4, column=4, padx=5, pady=10)
        tan_btn.grid(row=4, column=5, padx=5, pady=10)
        sin_inverse.grid(row=4, column=6, padx=5, pady=10)
        cos_inverse.grid(row=4, column=7, padx=5, pady=10)
        tan_inverse.grid(row=4, column=8, padx=5, pady=10)

        # row 14 buttons
        sinh_btn.grid(row=5, column=3, padx=5, pady=10)
        cosh_btn.grid(row=5, column=4, padx=5, pady=10)
        tanh_btn.grid(row=5, column=5, padx=5, pady=10)
        sinh_inverse.grid(row=5, column=6, padx=5, pady=10)
        cosh_inverse.grid(row=5, column=7, padx=5, pady=10)
        tanh_inverse.grid(row=5, column=8, padx=5, pady=10)

        # row 16 buttons
        deg_rad.grid(row=6,column=1,padx=10,pady=10)
        log_btn.grid(row=6,column=3,padx=10,pady=10)
        ln_btn.grid(row=6,column=5,padx=10,pady=10)
        factorial_btn.grid(row=6,column=7,padx=10,pady=10)

        # row  18 buttons
        pi_btn.grid(row=7, column=1, padx=10, pady=10)
        e_btn.grid(row=7, column=3, padx=10, pady=10)
        abs_btn.grid(row=7, column=5, padx=10, pady=10)
        reciprocal.grid(row=7, column=7, padx=10, pady=10)

        # row 20 buttos
        square_root.grid(row=8,column=1,padx=10,pady=10)
        cube_root.grid(row=8,column=3,padx=10,pady=10)
        general_root.grid(row=8,column=5,padx=10,pady=10)
        clear.grid(row=8,column=7,padx=10,pady=10)
        self.bind('<Return>', self.result_fn)


    def on_key_press(self,e):
        keyValue=e.keysym
        print(keyValue)
        if keyValue == '1':
            self.value_curr.set(value=self.value_curr.get()+'1')
        elif keyValue == '2':
            self.value_curr.set(value=self.value_curr.get()+'2')
        elif keyValue == '3':
            self.value_curr.set(value=self.value_curr.get()+'3')
        elif keyValue == '4':
            self.value_curr.set(value=self.value_curr.get()+'4')
        elif keyValue == '5':
            self.value_curr.set(value=self.value_curr.get()+'5')
        elif keyValue == '6':
            self.value_curr.set(value=self.value_curr.get()+'6')
        elif keyValue == '7':
            self.value_curr.set(value=self.value_curr.get()+'7')
        elif keyValue == '8':
            self.value_curr.set(value=self.value_curr.get()+'8')
        elif keyValue == '9':
            self.value_curr.set(value=self.value_curr.get()+'9')
        elif keyValue == '0':
            self.value_curr.set(value=self.value_curr.get()+'0')
        elif keyValue == 'plus':
            self.value_curr.set(value=self.value_curr.get()+'+')
        elif keyValue == 'minus':
            self.value_curr.set(value=self.value_curr.get()+'-')
        elif keyValue == 'slash':
            self.value_curr.set(value=self.value_curr.get()+'/')
        elif keyValue == 'percent':
            self.value_curr.set(value=self.value_curr.get()+'%')
        elif keyValue == 'asterisk':
            self.value_curr.set(value=self.value_curr.get()+'*')
        elif keyValue == 'Return' or keyValue == 'equal':
            self.result_fn()
        elif keyValue == 'period':
            self.value_curr.set(value=self.value_curr.get()+'.')
        elif keyValue == 'parenleft':
            self.value_curr.set(value=self.value_curr.get()+'(')
        elif keyValue == 'parenright':
            self.value_curr.set(value=self.value_curr.get()+')')









    def btn1(self):
        val=self.value_curr.get()
        val=val+'1'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn2(self):
        val = self.value_curr.get()
        val = val + '2'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn3(self):
        val = self.value_curr.get()
        val = val + '3'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn4(self):
        val = self.value_curr.get()
        val = val + '4'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn5(self):
        val = self.value_curr.get()
        val = val + '5'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn6(self):
        val = self.value_curr.get()
        val = val + '6'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn7(self):
        val = self.value_curr.get()
        val = val + '7'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn8(self):
        val = self.value_curr.get()
        val = val + '8'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn9(self):
        val = self.value_curr.get()
        val = val + '9'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def btn0(self):
        val = self.value_curr.get()
        val = val + '0'
        self.value_curr.set(val)
        print(self.value_curr.get())

    def clear_fn(self):
        self.value_curr.set('')
        print(self.value_curr.get())
        print("Your string in erased")
    def result_fn(self):
        equation=self.value_curr.get()
        print(equation)





    def add_fn(self):
        val = self.value_curr.get()
        val = val + '+'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def subtract_fn(self):
        val = self.value_curr.get()
        val = val + '-'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def multiply_fn(self):
        val = self.value_curr.get()
        val = val + '*'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def divide_fn(self):
        val = self.value_curr.get()
        val = val + '/'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def modulous_fn(self):
        val = self.value_curr.get()
        val = val + '%'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def power_fn(self):
        val = self.value_curr.get()
        val = val + '^'
        self.value_curr.set(val)
        print(self.value_curr.get())
    def leftBracket_fn(self):
        val = self.value_curr.get()
        val = val + '('
        self.value_curr.set(val)
        print(self.value_curr.get())
    def rightBracket_fn(self):
        val = self.value_curr.get()
        val = val + ')'
        self.value_curr.set(val)
        print(self.value_curr.get())

    def power_2(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = pow(2,val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def square_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = val * val
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')
    def cube_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = val * val * val
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')
    def e_power_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = pow(e,val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def general_power(self):
        val=self.value_curr.get()
        val=val+'^'
        self.value_curr.set(val)
        print(f"The current value is {self.value_curr.get()}")

    def sin_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = sin(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def cos_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = cos(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def tan_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = tan(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def sin_inverse_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = asin(val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def cos_inverse_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = acos(val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def tan_inverse_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = atan(val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def sinh_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = sinh(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def cosh_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = cosh(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def tanh_function(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = tanh(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def sinh_inverse_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = asinh(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def cosh_inverse_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = acosh(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def tanh_inverse_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = atanh(radians(val))
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def dot_fn(self):
        val=self.value_curr.get()
        val=val+'.'
        self.value_curr.set(val)
        print(f'This is the current vakue {self.value_curr.get()}')

    def degree_rad(self):
        if self.degree_rad_val.get() == 'Degree':
            self.degree_rad_val.set('Radian')
        else:
            self.degree_rad_val.set('Degree')

        print(self.degree_rad_val.get())

    def log_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = log10(val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def ln_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = log(val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def factorial_fn(self):
        val = self.value_curr.get()
        val = eval(val)
        print(f'This is the original value {val}')
        val = factorial(val)
        print(f'This is the value after operation {val}')
        self.value_curr.set(f'{val}')

    def pi_fn(self):
        val=self.value_curr.get()
        print(f'This is the value before the operation {val}')
        val=val+f'{pi}'
        self.value_curr.set(val)
        print(f'This is the value after the operation {val}')


    def e_fn(self):
        val=self.value_curr.get()
        print(f'This is the value before the operation {val}')
        val=val+f'{e}'
        self.value_curr.set(val)
        print(f'This is the value after the operation {val}')

    def abs_fn(self):
        val = self.value_curr.get()
        print(f'This is the value before the operation {val}')
        val=eval(val)
        val = abs(val)
        self.value_curr.set(f'{val}')
        print(f'This is the value after the operation {val}')

    def rec_fn(self):
        val = self.value_curr.get()
        print(f'This is the value before the operation {val}')
        val=eval(val)
        val = 1/val
        self.value_curr.set(f'{val}')
        print(f'This is the value after the operation {val}')

    def squre_root_fn(self):
        val = self.value_curr.get()
        print(f'This is the value before the operation {val}')
        val = eval(val)
        val = sqrt(val)
        self.value_curr.set(f'{val}')
        print(f'This is the value after the operation {val}')

    def cube_root_fn(self):
        val = self.value_curr.get()
        print(f'This is the value before the operation {val}')
        val = eval(val)
        val = pow(val,1/3)
        self.value_curr.set(f'{val}')
        print(f'This is the value after the operation {val}')

    def general_root(self):
        pass





class frame3(ttk.Frame): # this will be a unit converter
    def __init__(self,container,controller,*args,**kwargs): # this is the third options frame in our calculator
        super().__init__(container,*args,**kwargs)
        self.frames = ['Weight','Length', 'Currency','Force','Area','Angle', 'Speed','Abusive words']
        self.framesR = ['Weight converter', 'Length converter', 'Currency converter', 'Force converter', 'Area converter', 'Angle converter', 'Speed converter', 'Abusive words converter']
        self.variableR=tk.StringVar()
        self.variableR.set(self.framesR[0])

        # setting variable for Integers
        self.variable = tk.StringVar()
        self.variable.set(self.frames[0])

        # creating widget
        dropdownL = tk.OptionMenu(self,self.variable,*self.frames,command=self.main_fn)
        dropdownR = tk.OptionMenu(self, self.variableR, *self.framesR, command=self.right_optionMenu)

        # positioning widget
        dropdownL.grid(row=0,column=0,padx=(10,0),pady=(0,50))
        dropdownR.grid(row=0,column=1,padx=(0,10),pady=(0,50))

        container=ttk.Frame(self)
        container.grid(row=2,column=0,padx=20,pady=40,sticky='NSEW')
        self.frames_mini=dict()
        Weigth_Container=converter1(container)
        Height_Container=converter2(container)
        Currency_Container=converter3(container)
        Force_container=converter4(container)
        Area_container=converter5(container)
        Angle_container=converter6(container)
        Speed_container=converter7(container)
        Gali_container=converter8(container)

        Weigth_Container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Height_Container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Currency_Container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Force_container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Area_container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Angle_container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Speed_container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')
        Gali_container.grid(row=1,column=0,padx=10,pady=10,sticky='NSEW')



        self.frames_mini['Container1'] = Weigth_Container
        self.frames_mini['Container2'] = Height_Container
        self.frames_mini['Container3'] = Currency_Container
        self.frames_mini['Container4'] = Force_container
        self.frames_mini['Container5'] = Area_container
        self.frames_mini['Container6'] = Angle_container
        self.frames_mini['Container7'] = Speed_container
        self.frames_mini['Container8'] = Gali_container
        self.frames_mini['Container1'].tkraise()




    def right_optionMenu(self,choice):
        choice = self.variableR.get()

        if choice == 'Weight converter':
            self.frames_mini['Container1'].tkraise()
        elif choice == 'Length converter':
            self.frames_mini['Container2'].tkraise()
        elif choice == 'Currency converter':
            self.frames_mini['Container3'].tkraise()
        elif choice == 'Force converter':
            self.frames_mini['Container4'].tkraise()
        elif choice == 'Area converter':
            self.frames_mini['Container5'].tkraise()
        elif choice == 'Angle converter':
            self.frames_mini['Container6'].tkraise()
        elif choice == 'Speed converter':
            self.frames_mini['Container7'].tkraise()
        elif choice == 'Abusive words converter':
            self.frames_mini['Container8'].tkraise()









    def main_fn(self,choice):
        choice = self.variable.get()
        if choice == 'Weight':
            self.side_converter1()
        elif choice == 'Length':
            self.side_converter2()
        elif choice == 'Currency':
            self.side_converter3()
        elif choice == 'Force':
            self.side_converter4()
        elif choice == 'Area':
            self.side_converter5()
        elif choice == 'Speed':
            self.side_converter6()
        elif choice == 'Angle':
            self.side_converter7()
        elif choice == 'Abusive words':
            self.side_converter8()


    # these functions will dislpay the side menu showing different unit conversion metrics
    def side_converter1(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        window.title('Weight units')
        title = ttk.Label(window,text="Available units")
        unit1 = ttk.Label(window,text="1)Kilograms (Kg)")
        unit2 = ttk.Label(window,text='2)LBS(lb)')
        unit3 = ttk.Label(window,text='3)Pounds(pnd)')
        unit4 = ttk.Label(window, text="4)Grams(g) ")
        unit5 = ttk.Label(window, text='5)Metric Ton(t)')
        unit6 = ttk.Label(window, text='6)Quintal(q)')
        unit7= ttk.Label(window,text='7)electronWeight(ew)')


        title.grid(row=0,column=3,padx=100,pady=8)
        unit1.grid(row=1,column=3,padx=100,pady=8)
        unit2.grid(row=2, column=3, padx=100, pady=8)
        unit3.grid(row=3, column=3, padx=100, pady=8)
        unit4.grid(row=4, column=3, padx=100, pady=8)
        unit5.grid(row=5, column=3, padx=100, pady=8)
        unit6.grid(row=6, column=3, padx=100, pady=8)
        unit7.grid(row=7, column=3, padx=100, pady=8)



    def side_converter2(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        window.title('Lenght Units')
        title = ttk.Label(window, text="Available units")
        unit1 = ttk.Label(window, text="1)Meter(m)")
        unit2 = ttk.Label(window, text='2)KiloMeter(km)')
        unit3 = ttk.Label(window, text='3)Feet(ft)')
        unit4 = ttk.Label(window, text="4)LightYear(Ly)")
        unit5 = ttk.Label(window, text='5)Atomic Length(u)')
        unit6 = ttk.Label(window, text='6)Inch(I)')
        unit7 = ttk.Label(window, text='7)Centimeter(cm)')

        title.grid(row=0, column=3, padx=100, pady=8)
        unit1.grid(row=1, column=3, padx=100, pady=8)
        unit2.grid(row=2, column=3, padx=100, pady=8)
        unit3.grid(row=3, column=3, padx=100, pady=8)
        unit4.grid(row=4, column=3, padx=100, pady=8)
        unit5.grid(row=5, column=3, padx=100, pady=8)
        unit6.grid(row=6, column=3, padx=100, pady=8)
        unit7.grid(row=7, column=3, padx=100, pady=8)


    def side_converter3(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        window.title('Currencies')
        title = ttk.Label(window, text="Available units")
        unit1 = ttk.Label(window, text="1)American Dollar($)")
        unit2 = ttk.Label(window, text='2)Indian Rupee(₹)')
        unit3 = ttk.Label(window, text='3)Euro(€)')
        unit4 = ttk.Label(window, text="4)Yen(¥) ")
        unit5 = ttk.Label(window, text='5)NewZeaLand Dollar(N$)')
        unit6 = ttk.Label(window, text='6)Australian Dollar(A$) ')
        unit7 = ttk.Label(window, text='7)Singapore Dollar(S$)')

        title.grid(row=0, column=3, padx=100, pady=8)
        unit1.grid(row=1, column=3, padx=100, pady=8)
        unit2.grid(row=2, column=3, padx=100, pady=8)
        unit3.grid(row=3, column=3, padx=100, pady=8)
        unit4.grid(row=4, column=3, padx=100, pady=8)
        unit5.grid(row=5, column=3, padx=100, pady=8)
        unit6.grid(row=6, column=3, padx=100, pady=8)
        unit7.grid(row=7, column=3, padx=100, pady=8)


    def side_converter4(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        window.title('Force units')
        title = ttk.Label(window, text="Available units")
        unit1 = ttk.Label(window, text="1)Newton(N)")
        unit2 = ttk.Label(window, text='2)Kgm2(K)')
        unit3 = ttk.Label(window, text='3)dyncecm2(D)')
        unit4 = ttk.Label(window, text="4)pound(P)")
        unit5 = ttk.Label(window, text='5)lbs(L)')
        unit6 = ttk.Label(window, text='6)Universal scale(U)')
        unit7 = ttk.Label(window, text='7)Atomic scale(A)')

        title.grid(row=0, column=3, padx=100, pady=8)
        unit1.grid(row=1, column=3, padx=100, pady=8)
        unit2.grid(row=2, column=3, padx=100, pady=8)
        unit3.grid(row=3, column=3, padx=100, pady=8)
        unit4.grid(row=4, column=3, padx=100, pady=8)
        unit5.grid(row=5, column=3, padx=100, pady=8)
        unit6.grid(row=6, column=3, padx=100, pady=8)
        unit7.grid(row=7, column=3, padx=100, pady=8)


    def side_converter5(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        window.title('Area units')
        title = ttk.Label(window, text="Available units")
        unit1 = ttk.Label(window, text="1)meter square(Ms)")
        unit2 = ttk.Label(window, text='2)ft square(Fs)')
        unit3 = ttk.Label(window, text='3)gaj(G)')
        unit4 = ttk.Label(window, text="4)biga(B)")
        unit5 = ttk.Label(window, text='5)km square(Km)')
        unit6 = ttk.Label(window, text='6)Acre(A)')
        unit7 = ttk.Label(window, text='7)atomic unit(U)')

        title.grid(row=0, column=3, padx=100, pady=8)
        unit1.grid(row=1, column=3, padx=100, pady=8)
        unit2.grid(row=2, column=3, padx=100, pady=8)
        unit3.grid(row=3, column=3, padx=100, pady=8)
        unit4.grid(row=4, column=3, padx=100, pady=8)
        unit5.grid(row=5, column=3, padx=100, pady=8)
        unit6.grid(row=6, column=3, padx=100, pady=8)
        unit7.grid(row=7, column=3, padx=100, pady=8)


    def side_converter6(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        window.title('Speed Units')
        title = ttk.Label(window, text="Available units")
        unit1 = ttk.Label(window, text="1)meter/second(ms)")
        unit2 = ttk.Label(window, text='2)kilometer/hour(kmh)')
        unit3 = ttk.Label(window, text='3)Miles/hour(mh)')
        unit4 = ttk.Label(window, text="4)Light Speed(L)")
        unit5 = ttk.Label(window, text='5)Sound Speed(S)')
        unit6 = ttk.Label(window, text='6)Atomic unit(U)')
        unit7 = ttk.Label(window, text='7)Kutta Bhar diya(Dogge)')

        title.grid(row=0, column=3, padx=100, pady=8)
        unit1.grid(row=1, column=3, padx=100, pady=8)
        unit2.grid(row=2, column=3, padx=100, pady=8)
        unit3.grid(row=3, column=3, padx=100, pady=8)
        unit4.grid(row=4, column=3, padx=100, pady=8)
        unit5.grid(row=5, column=3, padx=100, pady=8)
        unit6.grid(row=6, column=3, padx=100, pady=8)
        unit7.grid(row=7, column=3, padx=100, pady=8)


    def side_converter7(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title('Angle Units')
        title = ttk.Label(window, text="Available units")
        unit1 = ttk.Label(window, text="1)Degree(Deg)")
        unit2 = ttk.Label(window, text='2)Radian(Rad)')


        title.grid(row=0, column=3, padx=50, pady=8)
        unit1.grid(row=1, column=3, padx=50, pady=8)
        unit2.grid(row=2, column=3, padx=50, pady=8)



    def side_converter8(self):
        window = tk.Toplevel()
        window.geometry('680x600')
        window.title('Ab gali sun BC!')
        # tree banega bc ismei toe poora
        punjabi=ttk.Treeview(window,columns=(3),show='headings',height=10)
        punjabi.grid(row=2,column=0,padx=10,pady=10)
        punjabi.heading(0,text='Punjabi gali')
        bihari = ttk.Treeview(window, columns=(0), show='headings', height=10)
        bihari.grid(row=2, column=1, padx=10, pady=10)
        bihari.heading(0, text='Bihari gali')
        angreji = ttk.Treeview(window, columns=(0), show='headings', height=10)
        angreji.grid(row=2, column=2, padx=10, pady=10)
        angreji.heading(0, text='Angreji gali')
        dilli = ttk.Treeview(window, columns=(0), show='headings', height=10)
        dilli.grid(row=3, column=0, padx=10, pady=10)
        dilli.heading(0, text='Dilli ki gali')
        rajwadi = ttk.Treeview(window, columns=(0), show='headings', height=10)
        rajwadi.grid(row=3, column=1, padx=10, pady=10)
        rajwadi.heading(0, text='Rajwadi gali')
        kanada= ttk.Treeview(window, columns=(0), show='headings', height=10)
        kanada.grid(row=3, column=2, padx=10, pady=10)
        kanada.heading(0, text='Kannada gali')
        punjabi.insert(parent='', index=0, iid=0, values=('Penchod'))
        punjabi.insert(parent='', index=1, iid=1, values=('Madarchod'))
        punjabi.insert(parent='', index=2, iid=2, values=('Bsdk'))
        punjabi.insert(parent='', index=3, iid=3, values=('Bund_phaad_dunga'))
        punjabi.insert(parent='', index=4, iid=4, values=('Kudi_Chod'))
        punjabi.insert(parent='', index=5, iid=5, values=('Maa_ka_bhosda'))
        punjabi.insert(parent='', index=6, iid=6, values=('Chutiye'))
        punjabi.insert(parent='', index=7, iid=7, values=('Jhaat_ke_baal'))
        punjabi.insert(parent='', index=8, iid=8, values=('Kutiya'))
        punjabi.insert(parent='', index=9, iid=9, values=('Bund_da_jhed'))

        # bihari tree
        bihari.insert(parent='', index=0, iid=0, values=('Bhainchod'))
        bihari.insert(parent='', index=1, iid=1, values=('Madharchod'))
        bihari.insert(parent='', index=2, iid=2, values=('Bhosdike'))
        bihari.insert(parent='', index=3, iid=3, values=('Gaandiya_phaad_dunga'))
        bihari.insert(parent='', index=4, iid=4, values=('Launidya_Chod'))
        bihari.insert(parent='', index=5, iid=5, values=('Maa_ka_bhosda'))
        bihari.insert(parent='', index=6, iid=6, values=('Chutiye'))
        bihari.insert(parent='', index=7, iid=7, values=('Jhaat_ke_baal'))
        bihari.insert(parent='', index=8, iid=8, values=('Kutiya'))
        bihari.insert(parent='', index=9, iid=9, values=('Gand_ka_jhed'))

        # angreji
        angreji.insert(parent='', index=0, iid=0, values=('Sister_Fucker'))
        angreji.insert(parent='', index=1, iid=1, values=('Mother_Fucker'))
        angreji.insert(parent='', index=2, iid=2, values=('Rascal'))
        angreji.insert(parent='', index=3, iid=3, values=('Kick_your_ass'))
        angreji.insert(parent='', index=4, iid=4, values=('Casanova'))
        angreji.insert(parent='', index=5, iid=5, values=('Shit_man'))
        angreji.insert(parent='', index=6, iid=6, values=('Chutiya'))
        angreji.insert(parent='', index=7, iid=7, values=('Pubic_hair'))
        angreji.insert(parent='', index=8, iid=8, values=('Bitch'))
        angreji.insert(parent='', index=9, iid=9, values=('Ass hole'))

        # dilli

        dilli.insert(parent='', index=0, iid=0, values=('Bhenchod'))
        dilli.insert(parent='', index=1, iid=1, values=('Madarchod'))
        dilli.insert(parent='', index=2, iid=2, values=('Bhosdike'))
        dilli.insert(parent='', index=3, iid=3, values=('Gaandiya_phaad_dunga'))
        dilli.insert(parent='', index=4, iid=4, values=('Choot_marika'))
        dilli.insert(parent='', index=5, iid=5, values=('Maa_ka_bhosda'))
        dilli.insert(parent='', index=6, iid=6, values=('Chutiye'))
        dilli.insert(parent='', index=7, iid=7, values=('Jhaat_ke_baal'))
        dilli.insert(parent='', index=8, iid=8, values=('Kutiya'))
        dilli.insert(parent='', index=9, iid=9, values=('Gand_ka_jhed'))

        # rajwadi
        rajwadi.insert(parent='', index=0, iid=0, values=('Bhenchod'))
        rajwadi.insert(parent='', index=1, iid=1, values=('Madarchod'))
        rajwadi.insert(parent='', index=2, iid=2, values=('Bhosdike'))
        rajwadi.insert(parent='', index=3, iid=3, values=('Gaandiya_phaad_dunga'))
        rajwadi.insert(parent='', index=4, iid=4, values=('Chori_chod'))
        rajwadi.insert(parent='', index=5, iid=5, values=('Maa_ka_bhosda'))
        rajwadi.insert(parent='', index=6, iid=6, values=('Gael Choda'))
        rajwadi.insert(parent='', index=7, iid=7, values=('Jhaat_ke_baal'))
        rajwadi.insert(parent='', index=8, iid=8, values=('Kutiya'))
        rajwadi.insert(parent='', index=9, iid=9, values=('Gand_ka_jhed'))

        #kannada

        kanada.insert(parent='', index=0, iid=0, values=('Sahōdari_Laiṅgikate'))
        kanada.insert(parent='', index=1, iid=1, values=('Tāyi_Laiṅgikate'))
        kanada.insert(parent='', index=2, iid=2, values=('Yōni'))
        kanada.insert(parent='', index=3, iid=3, values=('Soṇṭa_Haridu hōguvudu'))
        kanada.insert(parent='', index=4, iid=4, values=('Huḍugi_chod'))
        kanada.insert(parent='', index=5, iid=5, values=('Maa_ka_bhosda'))
        kanada.insert(parent='', index=6, iid=6, values=('Tigamuchu'))
        kanada.insert(parent='', index=7, iid=7, values=('Shata'))
        kanada.insert(parent='', index=8, iid=8, values=('Kutiya'))
        kanada.insert(parent='', index=9, iid=9, values=('Gand_ka_jhed'))








class converter1(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val=tk.DoubleVar()
        self.Output_val=tk.DoubleVar()
        self.options=['kg','lb','pnd','gm','t','q','ew']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to=tk.OptionMenu(self,self.from_var,*self.options)
        options_from=tk.OptionMenu(self,self.to_var,*self.options)
        label_input=ttk.Label(self,text='Input:')
        label_output=ttk.Label(self,text='Output:')
        entry_input=ttk.Entry(self,textvariable=self.Input_val,width=50)
        output_entry=ttk.Entry(self,textvariable=self.Output_val,width=50)
        label_from=ttk.Label(self,text='FROM')
        label_to=ttk.Label(self,text='TO')
        calcualte=ttk.Button(self,text='Calculate',command=self.calculate)


        label_from.grid(row=0,column=2,padx=(10,0),pady=(10,10))
        options_from.grid(row=0,column=3,padx=(0,10),pady=(10,10))
        label_to.grid(row=0,column=4,padx=(50,0),pady=(10,10))
        option_to.grid(row=0,column=5,padx=(0,10),pady=(10,10))
        label_input.grid(row=1,column=0,pady=(50,50),padx=(10,5))
        entry_input.grid(row=1,column=1,padx=(0,10),pady=(50,50))
        label_output.grid(row=2,column=0,pady=(50,50),padx=(10,5))
        output_entry.grid(row=2,column=1,padx=(0,10),pady=(50,50))
        calcualte.grid(row=3,column=1,columnspan=2)

    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)

        result=self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())





class converter2(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['m', 'Km', 'ft', 'Ly', 'U', 'I', 'cm']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])

        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calculate = ttk.Button(self, text='Calculate',command=self.calculate)

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calculate.grid(row=3, column=1, columnspan=2)



    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'm':
            if from_val == 'm':
                conversion_ratio.set(1.0)
            elif from_val == 'Km':
                conversion_ratio.set(0.001)
            elif from_val == 'ft':
                conversion_ratio.set(3.280841666667)
            elif from_val == 'Ly':
                conversion_ratio.set(1.057e-16)
            elif from_val == 'U':
                conversion_ratio.set(1e+6)
            elif from_val == 'I':
                conversion_ratio.set(39.3701)
            elif from_val == 'cm':
                conversion_ratio.set(1e-2)

        elif to_val == 'Km':
            if from_val == 'm':
                conversion_ratio.set(1e-3)
            elif from_val == 'Km':
                conversion_ratio.set(1)
            elif from_val == 'ft':
                conversion_ratio.set(3.280841666667e3)
            elif from_val == 'Ly':
                conversion_ratio.set(1.057e-13)
            elif from_val == 'U':
                conversion_ratio.set(1e+9)
            elif from_val == 'I':
                conversion_ratio.set(39.3701e3)
            elif from_val == 'cm':
                conversion_ratio.set(1e-5)

        elif to_val == 'ft':
            if from_val == 'm':
                conversion_ratio.set(0.304800164592)
            elif from_val == 'Km':
                conversion_ratio.set(0.304800164592e3)
            elif from_val == 'ft':
                conversion_ratio.set(1)
            elif from_val == 'Ly':
                conversion_ratio.set(3.221740281845840388e-17)
            elif from_val == 'U':
                conversion_ratio.set(0.304800164592e-6)
            elif from_val == 'I':
                conversion_ratio.set(12.000006479999999698)
            elif from_val == 'cm':
                conversion_ratio.set(0.304800164592e-2)

        elif to_val == 'Ly':
            if from_val == 'm':
                conversion_ratio.set(9460735581375254)
            elif from_val == 'Km':
                conversion_ratio.set(9460735581375254e-3)
            elif from_val == 'ft':
                conversion_ratio.set(31039158731546108)
            elif from_val == 'Ly':
                conversion_ratio.set(1)
            elif from_val == 'U':
                conversion_ratio.set(9460735581375254e-6)
            elif from_val == 'I':
                conversion_ratio.set(372469904778553344)
            elif from_val == 'cm':
                conversion_ratio.set(9460735581375254e2)

        elif to_val == 'U':
            if from_val == 'm':
                conversion_ratio.set(1e-6)
            elif from_val == 'Km':
                conversion_ratio.set(1e-9)
            elif from_val == 'ft':
                conversion_ratio.set(3.280841666666665907e-6)
            elif from_val == 'Ly':
                conversion_ratio.set(1.057001404805065657e-22)
            elif from_val == 'U':
                conversion_ratio.set(1)
            elif from_val == 'I':
                conversion_ratio.set(3.937009999999999089e-5)
            elif from_val == 'cm':
                conversion_ratio.set(1e-4)

        elif to_val == 'I':
            if from_val == 'm':
                conversion_ratio.set(0.025400013715999994468)
            elif from_val == 'Km':
                conversion_ratio.set(0.025400013715999994468e3)
            elif from_val == 'ft':
                conversion_ratio.set(0.083333378333333305021)
            elif from_val == 'Ly':
                conversion_ratio.set(2.684783568204865834e-18)
            elif from_val == 'U':
                conversion_ratio.set(0.025400013715999994468e-6)
            elif from_val == 'I':
                conversion_ratio.set(1)
            elif from_val == 'cm':
                conversion_ratio.set(0.025400013715999994468e-2)

        elif to_val == 'cm':
            if from_val == 'm':
                conversion_ratio.set(1e-2)
            elif from_val == 'Km':
                conversion_ratio.set(1e-5)
            elif from_val == 'ft':
                conversion_ratio.set(3.280841666667e-2)
            elif from_val == 'Ly':
                conversion_ratio.set(1.057e-18)
            elif from_val == 'U':
                conversion_ratio.set(1e+4)
            elif from_val == 'I':
                conversion_ratio.set(39.3701e-2)
            elif from_val == 'cm':
                conversion_ratio.set(1)

        result = self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())







class converter3(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['$', 'N$', 'A$', 'S$', '₹', '¥', '€']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calcualte = ttk.Button(self, text='Calculate',command=self.calculate )

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calcualte.grid(row=3, column=1, columnspan=2)

    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)

        result = self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())


class converter4(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['N', 'K', 'D', 'P', 'L', 'U', 'A']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calcualte = ttk.Button(self, text='Calculate',command=self.calculate )

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calcualte.grid(row=3, column=1, columnspan=2)

    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)

        result = self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())



class converter5(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['Ms', 'Fs', 'G', 'B', 'Km', 'A', 'U']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calcualte = ttk.Button(self, text='Calculate',command=self.calculate )

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calcualte.grid(row=3, column=1, columnspan=2)

    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)

        result = self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())


class converter6(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['Deg','Rad']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calcualte = ttk.Button(self, text='Calculate',command=self.calculate )

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calcualte.grid(row=3, column=1, columnspan=2)

    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)

        result = self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())


class converter7(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['ms', 'Kmh', 'Mh', 'L', 'S', 'U', 'Dogge']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calcualte = ttk.Button(self, text='Calculate',command=self.calculate )

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calcualte.grid(row=3, column=1, columnspan=2)

    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)

        result = self.Input_val.get() * conversion_ratio.get()
        self.Output_val.set(result)
        print(conversion_ratio.get())


class converter8(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.Input_val = tk.DoubleVar()
        self.Output_val = tk.DoubleVar()
        self.options = ['Punjabi', 'Bihari', 'Angreji', 'Dilli', 'Rajwadi', 'Kannad']
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        self.from_var = tk.StringVar(value=self.options[0])
        self.to_var = tk.StringVar(value=self.options[0])
        option_to = tk.OptionMenu(self, self.from_var, *self.options)
        options_from = tk.OptionMenu(self, self.to_var, *self.options)
        label_input = ttk.Label(self, text='Input:')
        label_output = ttk.Label(self, text='Output:')
        entry_input = ttk.Entry(self, textvariable=self.Input_val, width=50)
        output_entry = ttk.Entry(self, textvariable=self.Output_val, width=50)
        label_from = ttk.Label(self, text='FROM')
        label_to = ttk.Label(self, text='TO')
        calcualte = ttk.Button(self, text='Calculate',command=self.calculate )

        label_from.grid(row=0, column=2, padx=(10, 0), pady=(10, 10))
        options_from.grid(row=0, column=3, padx=(0, 10), pady=(10, 10))
        label_to.grid(row=0, column=4, padx=(50, 0), pady=(10, 10))
        option_to.grid(row=0, column=5, padx=(0, 10), pady=(10, 10))
        label_input.grid(row=1, column=0, pady=(50, 50), padx=(10, 5))
        entry_input.grid(row=1, column=1, padx=(0, 10), pady=(50, 50))
        label_output.grid(row=2, column=0, pady=(50, 50), padx=(10, 5))
        output_entry.grid(row=2, column=1, padx=(0, 10), pady=(50, 50))
        calcualte.grid(row=3, column=1, columnspan=2)



    def calculate(self):
        to_value=self.to_var.get()
        from_value=self.from_var.get()
        self.calculate_util(to_value,from_value)


    def calculate_util(self,to_val,from_val):
        conversion_ratio=tk.DoubleVar()
        if to_val == 'kg':
            if from_val == 'kg':
                conversion_ratio.set(1.0)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3)
            elif from_val == 't':
                conversion_ratio.set(0.0009999988107)
            elif from_val == 'q':
                conversion_ratio.set(0.01)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808E+30)

        elif to_val == 'lb':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592*1.0977683828808e30)

        elif to_val == 'pnd':
            if from_val == 'kg':
                conversion_ratio.set(0.453592)
            elif from_val == 'lb':
                conversion_ratio.set(1)
            elif from_val == 'pnd':
                conversion_ratio.set(1)
            elif from_val == 'gm':
                conversion_ratio.set(0.453592e-3)
            elif from_val == 't':
                conversion_ratio.set(0.000499999592145)
            elif from_val == 'q':
                conversion_ratio.set(0.453502e-2)
            elif from_val == 'ew':
                conversion_ratio.set(0.453592 * 1.0977683828808e30)

        elif to_val == 'gm':
            if from_val == 'kg':
                conversion_ratio.set(1e-3)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462e-3)
            elif from_val == 'gm':
                conversion_ratio.set(1)
            elif from_val == 't':
                conversion_ratio.set(9.999991842900001118e-7)
            elif from_val == 'q':
                conversion_ratio.set(1e-5)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e28)

        elif to_val == 't':
            if from_val == 'kg':
                conversion_ratio.set(999.99918429000001652)
            elif from_val == 'lb':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'pnd':
                conversion_ratio.set(2204.6208235160570439)
            elif from_val == 'gm':
                conversion_ratio.set(999.99918429000001652e3)
            elif from_val == 't':
                conversion_ratio.set(1)
            elif from_val == 'q':
                conversion_ratio.set(999.99918429000001652e-2)
            elif from_val == 'ew':
                conversion_ratio.set(999.99918429000001652*1.0977683828808e30)

        elif to_val == 'q':
            if from_val == 'kg':
                conversion_ratio.set(1e2)
            elif from_val == 'lb':
                conversion_ratio.set(200)
            elif from_val == 'pnd':
                conversion_ratio.set(200)
            elif from_val == 'gm':
                conversion_ratio.set(1e5)
            elif from_val == 't':
                conversion_ratio.set(0.1)
            elif from_val == 'q':
                conversion_ratio.set(1)
            elif from_val == 'ew':
                conversion_ratio.set(1.0977683828808e32)

        elif to_val == 'ew':
            if from_val == 'kg':
                conversion_ratio.set(1/1.0977683828808e30)
            elif from_val == 'lb':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'pnd':
                conversion_ratio.set(2.20462/1.0977683828808e30)
            elif from_val == 'gm':
                conversion_ratio.set(1e-3/1.0977683828808e30)
            elif from_val == 't':
                conversion_ratio.set(1e3/1.097768382880830)
            elif from_val == 'q':
                conversion_ratio.set(1e2/1.097768382880830)
            elif from_val == 'ew':
                conversion_ratio.set(1)


        # a data frame can be used here for storing a 10X10 matrix where index are from 0-10 and columns are lang names and
        # then indexes can be compared for retrievin the values




        print(conversion_ratio.get())











root=main_frame()
set_dpi_awareness()
root.columnconfigure(0,weight=1)# this will place the column as central placed
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use('vista'))
root.mainloop()

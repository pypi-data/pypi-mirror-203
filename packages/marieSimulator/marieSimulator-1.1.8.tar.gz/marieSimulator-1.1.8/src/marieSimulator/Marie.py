class Marie:
    def __init__(self, mr = None):
        self.AC = 0x0000
        self.PC = 0b000000000000
        self.MAR = 0b000000000000
        self.MBR = 0x0000
        self.IR = 0x0000
        self.InReg = 0x00
        self.OutReg = 0x00

        self.GUI = False

        self.M = [0 for i in range(4096)]

        self.operation = None
        self.running = True
        self.canStep = True

        if mr != None:
            self.parse(mr)
    
    def parse(self, mr):
        self.M = mr.M
        self.M += [0] * (16**3 - len(mr.M))
        self.symbolTable = mr.symbolTable

    def show(self):
        output = "\n"

        for item in self.M:
            output += hex(item) + " | "
        output = output[:-3] + "\n"

        print(output)
    
    def run(self):
        while self.running:
            self.__fetch()
            self.__incrementPC()
            self.__decode()
            self.__getOperand()
            self.__execute()
    
    def step(self):
        if self.canStep:
            previousM = self.M.copy()
            self.__fetch()
            self.__incrementPC()
            self.__decode()
            self.__getOperand()
            self.__execute()
        
            output = []

            for i in range(len(self.M)):
                if self.M[i] != previousM[i]:
                    output.append(i)
            
            return output
        else:
            return None



    def __fetch(self):
        self.MAR = self.PC
        self.MBR = self.M[self.MAR]
        self.IR = self.MBR
    
    def __incrementPC(self):
        self.PC += 1
    
    def __decode(self):
        self.MAR = (self.IR & 0x0FFF)
        self.operation = (self.IR & 0xF000) >> 12

    def __getOperand(self):
        if self.operation not in [0x5, 0x6, 0x7, 0x8, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF]:
            self.MBR = self.M[self.MAR]

    def __execute(self):
        if self.operation == 0x0:
            self.__jnS()
        elif self.operation == 0x1:
            self.__load()
        elif self.operation == 0x2:
            self.__store()
        elif self.operation == 0x3:
            self.__add()
        elif self.operation == 0x4:
            self.__subt()
        elif self.operation == 0x5:
            self.__input()
        elif self.operation == 0x6:
            self.__output()
        elif self.operation == 0x7:
            self.__halt()
        elif self.operation == 0x8:
            self.__skipcond()
        elif self.operation == 0x9:
            self.__jump()
        elif self.operation == 0xA:
            self.__clear()
        elif self.operation == 0xB:
            self.__addI()
        elif self.operation == 0xC:
            self.__jumpI()
        elif self.operation == 0xD:
            self.__loadI()
        elif self.operation == 0xE:
            self.__storeI()
        


    def __jnS(self):
        self.MBR = self.PC
        self.M[self.MAR] = self.MBR
        self.MBR = (self.IR & 0x0FFF)
        self.AC = 0x1
        self.AC = self.AC + self.MBR
        self.PC = self.AC

    def __load(self):
        self.AC = self.MBR

    def __store(self):
        self.MBR = self.AC
        self.M[self.MAR] = self.MBR

    def __add(self):
        self.AC = self.AC + self.MBR

    def __subt(self):
        self.AC = self.AC - self.MBR

    def __input(self):
        if self.GUI:
            self.InReg = None
            while self.InReg == None:
                self.InReg = self.InReg
        else:
            self.InReg = int(input("Input (HEX): "), 16)
        self.AC = self.InReg

    def __output(self):
        self.OutReg = self.AC
        if not self.GUI:
            print("Output (HEX): " + hex(self.OutReg))


    def __halt(self):
        self.running = False
        self.canStep = False

    def __skipcond(self):
        skipBits = (self.IR & 0b0000110000000000) >> 8
        if skipBits == 0b0000:
            if self.AC < 0:
                self.__incrementPC()
        elif skipBits == 0b0100:
            if self.AC == 0:
                self.__incrementPC()
        elif skipBits == 0b1000:
            if self.AC > 0:
                self.__incrementPC()

    def __jump(self):
        self.PC = (self.IR & 0x0FFF)
    
    def __clear(self):
        self.AC = 0x0
    
    def __addI(self):
        self.MAR = self.MBR
        self.MBR = self.M[self.MAR]
        self.AC = self.AC + self.MBR

    def __jumpI(self):
        self.PC = self.MBR
    
    def __loadI(self):
        self.MAR = self.MBR
        self.MBR = self.M[self.MAR]
        self.AC = self.MBR
    
    def __storeI(self):
        self.MAR = self.MBR
        self.MBR = self.AC
        self.M[self.MAR] = self.MBR


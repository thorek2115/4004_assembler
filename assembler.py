## 4004 patterns

# one word machine instructions:
# pattern = "OPCODE REG"
# pattern = "OPCODE R_PAIR"
# pattern = "OPCODE DATA"

# two word machine instructions:
# pattern = "OPCODE UPPER_ADDR MID_AND_LOW_ADDR"
# pattern = "OPCODE CONDITION MID_AND_LOW_ADDR"
# pattern = "OPCODE REG MID_AND_LOW_ADDR"
# pattern = "OPCODE R_PAIR UPPER_AND_LOWER_DATA"

# I/O, RAM and A group instructions
# pattern = "OPCODE"
# I/O and RAM - 1110 XXXX
# A -           1111 XXXX

#
# write assembly code in code.asm
#

import os
import time

t1 = time.perf_counter(), time.process_time()  # time measure

if not "code.asm" in os.listdir('.'):
    open("code.asm", "w").close()
    print("File code.asm doesn't exist")
    print("Created file code.asm in project directory")
    print("Exiting...")
    exit(-1)

machine_code = []
m_code_all = ""
label_addresses = {}
line_is_label = False
line_is_empty = False

def get_hex(num):
    match num[0]:
        case '%': return hex(int(num[1:], 2))[2:]  # binary
        case '$': return hex(int(num[1:], 16))[2:]  # hex
        case '0':  # octal
            if len(num) == 1: return '0'
            return hex(int(num[1:], 8))[2:]
        case _:
            if num[0].isdigit():
                return hex(int(num, 10))[2:] # decimal
            else:
                print_error("Wrong character")
                exit(-1)

def print_error(message):
    print(f"Error in: line {index + 1}, file: \"{os.path.abspath("code.asm")}\"")
    print("  ", line.rstrip('\n'))
    print(message)
    exit(-1)

def check_arg_count(arg_count):
    if len(upper_line) != arg_count:
        print_error(f"Invalid number of arguments.")

def check_max_value(number, max_num):
    if int(number, 16) > max_num:
        print_error(f"Number has to be between 0 and {max_num}")


with open("code.asm", "r") as file:
    for index, line in enumerate(file):
        upper_line = line[:line.find(";")].strip().upper().split(' ')
        if not upper_line[0]:  # empty string
            line_is_empty = True
        elif upper_line[0][-1] == ',':
            line_is_label = True

        if not line_is_label and not line_is_empty:
            match upper_line[0]:
                case "NOP":
                    check_arg_count(1)
                    machine_code.append("00")
                case "JCN":
                    check_arg_count(3)
                    condition = upper_line[1]
                    check_max_value("9", 0xF)
                    machine_code.append("1" + str(get_hex(condition)))
                    machine_code.append(upper_line[2])
                case "FIM":
                    check_arg_count(3)
                    register_pair = int(get_hex(upper_line[1]), 16) * 2
                    check_max_value(hex(register_pair), 0xE)
                    machine_code.append("2" + str(hex(register_pair)[2:]))
                    machine_code.append(get_hex(upper_line[2]))
                case "FIN":
                    check_arg_count(2)
                    register_pair = int(get_hex(upper_line[1]), 16) * 2
                    check_max_value(hex(register_pair), 0xE)
                    machine_code.append("3" + str(hex(register_pair))[2:])
                case "JIN":
                    check_arg_count(2)
                    register_pair = int(get_hex(upper_line[1]), 16) * 2 + 1
                    check_max_value(hex(register_pair), 0xF)
                    machine_code.append("3" + str(hex(register_pair))[2:])
                case "JUN":
                    check_arg_count(2)
                    machine_code.append("40")
                    machine_code.append(upper_line[1])
                    # assume ROM 0
                case "JMS":
                    check_arg_count(2)
                    machine_code.append("50")
                    machine_code.append(upper_line[1])
                    # assume ROM 0
                case "INC":
                    check_arg_count(2)
                    machine_code.append("6" + get_hex(upper_line[1]))
                case "ISZ":
                    check_arg_count(3)
                    machine_code.append("7" + get_hex(upper_line[1]))
                    machine_code.append(upper_line[2])
                case "ADD":
                    check_arg_count(2)
                    machine_code.append("8" + get_hex(upper_line[1]))
                case "SUB":
                    check_arg_count(2)
                    machine_code.append("9" + get_hex(upper_line[1]))
                case "LD":
                    check_arg_count(2)
                    machine_code.append("A" + get_hex(upper_line[1]))
                case "XCH":
                    check_arg_count(2)
                    machine_code.append("B" + get_hex(upper_line[1]))
                case "BBL":
                    check_arg_count(2)
                    machine_code.append("C" + get_hex(upper_line[1]))
                case "LDM":
                    check_arg_count(2)
                    machine_code.append("D" + get_hex(upper_line[1]))
                case "CLB":
                    check_arg_count(1)
                    machine_code.append("F0")
                case "CLC":
                    check_arg_count(1)
                    machine_code.append("F1")
                case "IAC":
                    check_arg_count(1)
                    machine_code.append("F2")
                case "CMC":
                    check_arg_count(1)
                    machine_code.append("F3")
                case "CMA":
                    check_arg_count(1)
                    machine_code.append("F4")
                case "RAL":
                    check_arg_count(1)
                    machine_code.append("F5")
                case "RAR":
                    check_arg_count(1)
                    machine_code.append("F6")
                case "TCC":
                    check_arg_count(1)
                    machine_code.append("F7")
                case "DAC":
                    check_arg_count(1)
                    machine_code.append("F8")
                case "TCS":
                    check_arg_count(1)
                    machine_code.append("F9")
                case "STC":
                    check_arg_count(1)
                    machine_code.append("FA")
                case "DAA":
                    check_arg_count(1)
                    machine_code.append("FB")
                case "KBP":
                    check_arg_count(1)
                    machine_code.append("FC")
                case "DCL":
                    check_arg_count(1)
                    machine_code.append("FD")
                case "SRC":
                    check_arg_count(2)
                    register_pair = int(get_hex(upper_line[1]), 16) * 2 + 1
                    check_max_value(hex(register_pair), 0xF)
                    machine_code.append("2" + str(hex(register_pair))[2:])
                case "WRM":
                    check_arg_count(1)
                    machine_code.append("E0")
                case "WMP":
                    check_arg_count(1)
                    machine_code.append("E1")
                case "WRR":
                    check_arg_count(1)
                    machine_code.append("E2")
                case "WPM":
                    check_arg_count(1)
                    machine_code.append("E3")
                case "WR0":
                    check_arg_count(1)
                    machine_code.append("E4")
                case "WR1":
                    check_arg_count(1)
                    machine_code.append("E5")
                case "WR2":
                    check_arg_count(1)
                    machine_code.append("E6")
                case "WR3":
                    check_arg_count(1)
                    machine_code.append("E7")
                case "SBM":
                    check_arg_count(1)
                    machine_code.append("E8")
                case "RDM":
                    check_arg_count(1)
                    machine_code.append("E9")
                case "RDR":
                    check_arg_count(1)
                    machine_code.append("EA")
                case "ADM":
                    check_arg_count(1)
                    machine_code.append("EB")
                case "RD0":
                    check_arg_count(1)
                    machine_code.append("EC")
                case "RD1":
                    check_arg_count(1)
                    machine_code.append("ED")
                case "RD2":
                    check_arg_count(1)
                    machine_code.append("EE")
                case "RD3":
                    check_arg_count(1)
                    machine_code.append("EF")
                case _:
                    print_error(f"Opcode {upper_line[0]} doesn't exist.")
        elif line_is_label:
            label_addresses[line.strip()[:-1].upper()] = hex(len(machine_code))[2:]
            line_is_label = False
        elif line_is_empty:
            line_is_empty = False

for i, v in enumerate(machine_code):
    if v in label_addresses:
        machine_code[i] = str(label_addresses[v])

k = 0
for i in machine_code:
    if k == 8:
        m_code_all = m_code_all + "\n"
        k = 0
    if len(i) == 1: i = "0" + i
    m_code_all = m_code_all + i.upper() + " "
    k += 1

t2 = time.perf_counter(), time.process_time()

#print(m_code_all)
#print("")
#print(f"Real time: {(t2[0] - t1[0]) * 1000000} microseconds")
#print(f"CPU time: {(t2[1] - t1[1]) * 1000000} microseconds")

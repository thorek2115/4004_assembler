# Intel 4004 and 4040 assembler

```asm
; write assembly code in code.asm
```

## 4040 Extension
### In 27 line in assembler.py you can enable 4040 extension instructions such as: HLT, BBS or EIN:
```py
enabled_4040 = True
```

## **Opcode patterns:**
### One word machine instructions:
* "OPCODE REG"
* "OPCODE R_PAIR"
* "OPCODE DATA"
```asm
ADD 2      ; OPCODE REG
FIN %0110  ; OPCODE R_PAIR
LDM $A     ; OPCODE DATA
```

### Two word machine instructions:
* "OPCODE UPPER_ADDR ADDR(label)"
* "OPCODE CONDITION ADDR(label)"
* "OPCODE REG ADDR(label)"
* "OPCODE R_PAIR DATA"
```asm
JMS END     ; OPCODE UPPER_ADDR+ADDR(label)
JCN 10 END  ; OPCODE CONDITION ADDR(label)
ISZ $7 END  ; OPCODE REG ADDR(label)
FIM %10 END ; OPCODE R_PAIR DATA
```

### I/O, RAM and A group instructions
* "OPCODE"
* I/O and RAM - 1110 XXXX
* A -           1111 XXXX
```asm
WRR   ; 1110 0010  ROM
WRM   ; 1110 0000  RAM
IAC   ; 1111 0010  accumulator
```

### 4040 Extension
* "OPCODE"
* 0000 XXXX
```asm
HLT  ; 0000 0001
OR4  ; 0000 0100
RPM  ; 0000 1110
```

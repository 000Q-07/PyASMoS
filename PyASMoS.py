print("16 bit Python to ASM Compiler. (v 0.1)")
x = input("Enter code: ")

if x.startswith('print("') and x.endswith('")'):
    content = x[7:-2]


    print("Code: ")

    for char in content:
        print("mov ah, 0x0e")
        print(f'mov al, "{char}"')
        print("int 0x10")
elif x == "#bootsector":
    print("jmp $")
    print("times 510 - ($-$$) db 0")
    print("dw 0xAA55")
elif x == "#header":
    print("bits 16")
    print("org 0x7c00")
else:
    print("ERROR: either syntax error or ASM command wasn't added to the Compiler yet.")
    

;Dado un N numero en DECIMAL imprimir su valor en BINARIO.
;Ejemplo Desarrollado Simulador EMU8086
data segment
  
   NN db 0
   dig db 0
   aux db 0

ends

stack segment
    dw  128  dup(0)  ;tamaño WORD 
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
    mov es, ax

    bucle:
      call leer3 ; en dig esta el numero ascii
      cmp dig,0Dh
      je salir
      sub dig, 30h
      mov al,1010b
      mul NN
     
      add al,dig
      mov NN,al
   
      jmp bucle
        
    mov ax, 4c00h ; sale
    int 21h
   
    ;PROCESOS
       
    salir:
       call mostrar3
       mov ax, 4c00h
       int 21h
    ret
   
    mostrar3:
      mov cx,08h
      bucle2:
        rol nn,01h
        adc aux,00h
       
        mov dl, aux
        add dl,30h
        mov ah,02h
        int 21h
        mov aux,00h
	loop bucle2
    ret
       
    leer3:
      mov ah, 01h
      int 21h
      mov dig,al
    ret 

   
   
ends

end start ;establecer el punto de entrada y detener el ensamblador.
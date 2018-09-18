;Ejemplo Desarrollado Simulador EMU8086
.model small
.stack 64
.data
;------------------------------------------------------------
num1 db 'Introduce el primer numero==>',10,13,'$'
 
num2 db 'Introduce el segundo numero==>',10,13,'$'
 
 
guarda1 db '?',10,13,'$'
 
guarda2 db '?',10,13,'$'
 
resultado db 'El mayor es:','$'
 
hecho db 'Ciencias-3','$'
 
salto db '',10,13,'$'
 
;-----------------------------------------------------------
.code
mov ax,@data
mov ds,ax
;-----------------------------------------------------------
 
mov ah,06
mov al,01
mov bh,09      ;color de letra
mov cx,0000h
mov dx,184fh
int 10H
 
 
mov ah,9
lea dx,num1   ;pide 1er numero
int 21h
 
mov ah,1       ;teclado
int 21h
 
 
mov bl,al     ;guardamos valor 
 
 
mov ah,9
lea dx,salto   ;salto
int 21h
 
mov ah,9
lea dx,num2   ;pide 2do numero
int 21h
 
mov ah,1      ;teclado
int 21h
 
mov guarda1,al ;respaldamos para que no lo pierda en el salto
 
mov ah,9
lea dx,salto   ;salto
int 21h
 
mov al,guarda1  ;recuperamos valor
;-----------------------------------------------------------
cmp bl,al     ;COMPARACIONES 
 
jae imprime1  
jmp imprime2
 
;------------------------------------------------------------
 
imprime1:
 
mov guarda1,bl      
 
mov ah,9
lea dx,resultado    ;MENSAJE DE RESULTADO 
int 21h
 
mov ah,2
mov dl,guarda1      ;IMPRIMIMOS MAYOR
int 21h
 
jmp termina
;-----------------------------------------------------------
 
imprime2:
 
mov guarda2,al   
 
mov ah,9
lea dx,resultado ;MENSAJE DE RESULTADO 
int 21h
 
mov ah,2
mov dl,guarda2    ;IMPRIMIMOS MAYOR
int 21h
 
jmp termina
 
;----------------------------------------------------------
 
termina:
 
mov ah,9
lea dx,salto   ;salto
int 21h
 
mov ah,9
lea dx,hecho ;MENSAJE DE RESULTADO 
int 21h
 
mov ax,4c00h       ;TERMINA PROGRAMA
int 21h
 
end
ends

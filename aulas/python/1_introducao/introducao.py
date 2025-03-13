# Código em python para exemplificar a simplicidade da linguagem [Alto nível - fácil para humano assimilar]
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a) ao mundo do Python!"

nomes = ["Alice", "Bob", "Carlos"]

for nome in nomes:
    print(saudacao(nome))

# Código equivalente em Java (mais estruturado) [Alto nível mais complexo que Python]
"""
/*
import java.util.Arrays;
import java.util.List;

public class SaudacaoJava {
    public static String saudacao(String nome) {
        return "Olá, " + nome + "! Bem-vindo ao mundo do Java.";
    }
    
    public static void main(String[] args) {
        List<String> nomes = Arrays.asList("Alice", "Bob", "Carlos");
        for (String nome : nomes) {
            System.out.println(saudacao(nome));
        }
    }
}
*/
"""    

# Código equivalente em C++ (mais verboso) [Nível intermediário - mais complexo que Java]
"""
#include <iostream>
#include <vector>
using namespace std;

string saudacao(string nome) {
    return "Olá, " + nome + "! Bem-vindo ao mundo do C++.";
}

int main() {
    vector<string> nomes = {"Alice", "Bob", "Carlos"};
    for (const string& nome : nomes) {
        cout << saudacao(nome) << endl;
    }
    return 0;
}
*/
"""

# Código equivalente em Assembly [Baixo nível - difícil para humano assimilar - mais complexo que C++, mais rápido para o computador]
"""
section .data
    saudacao db "Olá, ", 0
    mensagem_final db "! Bem-vindo ao mundo do Assembly.", 10, 0
    nomes db "Alice", 0, "Bob", 0, "Carlos", 0

section .bss
    buffer resb 64  ; Buffer para armazenar a mensagem

section .text
    global _start

_start:
    ; Exibir saudação para cada nome
    mov esi, nomes   ; Ponteiro para a lista de nomes

loop_nomes:
    mov edi, buffer
    call copiar_saudacao

    ; Exibir mensagem formatada
    mov eax, 4       ; syscall: write
    mov ebx, 1       ; saída padrão
    mov ecx, buffer  ; ponteiro para mensagem formatada
    mov edx, 64      ; tamanho máximo
    int 0x80         ; chamada de sistema

    ; Avançar para o próximo nome
    add esi, 6       ; Pular para o próximo nome
    cmp byte [esi], 0
    jne loop_nomes

    ; Encerrar programa
    mov eax, 1       ; syscall: exit
    xor ebx, ebx
    int 0x80

copiar_saudacao:
    ; Copia "Olá, " para o buffer
    mov edi, buffer
    mov esi, saudacao
    call copiar_string

    ; Copia o nome
    mov esi, nomes
    call copiar_string

    ; Copia "! Bem-vindo ao mundo do Assembly."
    mov esi, mensagem_final
    call copiar_string

    ret

copiar_string:
    lodsb
    test al, al
    jz done
    stosb
    jmp copiar_string
done:
    ret

"""

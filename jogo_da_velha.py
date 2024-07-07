class jogoDavelha:
    tabuleiro =  {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}   
    turno = None

    def __init__(self, jogador_inicial="X"): # Jogada inicial por padrão sera x
        self.turno = jogador_inicial

    def exibir_tabuleiro(self):
        print("──┬───┬───┐") # montando um tabuleiro
        print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
        print("├───┼───┼───┤")
        print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")


    def verifica_jogada(self, jogada):
        if jogada in self.tabuleiro.keys(): # se jogada estive em tabuleiro
            if self.tabuleiro[jogada] == " ": # e no luga onde for a jogada == vaazio
                return True
            return False
        

    def verifica_tabuleiro(self):

        # Tabuleiro na vetical | verifica colunas
        if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != " ":
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != " ":
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != " ":
            return self.tabuleiro['9']
        
        # Tabuleiro na Horizontal
        elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != " ":
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != " ":
            return self.tabuleiro['4']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != " ":
            return self.tabuleiro['1']
        
        # 2 jogados na diagonal
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != " ":
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != " ":
            return self.tabuleiro['1']
        
      
        if [*self.tabuleiro.values()].count(' ') == 0:
            return 'empate'
        else:
            return [*self.tabuleiro.values()].count(' ')
        

    def jogar(self):
        while True:
            self.exibir_tabuleiro()

            # De quem e a vez de jogar ?
            print(f"turno de {self.turno} qual sua jogada ?.")

            # verifica jogada valida

            while True:
                jogada = input('Jogada')

                if self.verifica_jogada(jogada):
                    break

                else:
                    print(f'Jogada do {self.turno} invalida Tente novamente.')
             # verifica se o local esta vazio caso sim x sera na posição 7   
            self.tabuleiro[jogada] = self.turno

            # exibindo atualização do tabuleiro em tempo real | os estados do tabuleiro : x ganhou | o ganhou | empate 
            estado = self.verifica_tabuleiro()


            if estado == 'X':
                print("X é o vencedor !!!")
                break

            elif estado == 'O':
                print("O é o vencedor !!!")
                break


            elif estado == 'empate':
                print('EMPATE !!!')
                break

            # Trocando os turnos

            self.turno = "X" if self.turno == "O" else "O"
        self.exibir_tabuleiro()


game = jogoDavelha()
game.jogar()

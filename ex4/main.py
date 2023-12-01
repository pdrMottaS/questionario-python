class Agenda:
    agenda = []
    count = 1

    @classmethod
    def adicionar_contato(self):
        nome = input("insira o nome: ")
        telefone = input("insira o telefone: ")
        self.agenda.append({
            'id':self.count,
            'nome':nome,
            'telefone':int(telefone)
        })
        self.count += 1
    
    @classmethod
    def listar_contato(self):
        for i in self.agenda:
            print(f'id: {i["id"]}\nNome: {i["nome"]}\nTelefone:{i["telefone"]}')

    @classmethod
    def buscar_contato(self):
        search = input("Insira o nome ou telefone:")
        for i in self.agenda:
            if i['nome'] == search:
                print(f'id: {i["id"]}\nNome: {i["nome"]}\nTelefone:{i["telefone"]}')
                break
            if i['telefone'] == int(search):
                print(f'id: {i["id"]}\nNome: {i["nome"]}\nTelefone:{i["telefone"]}')
                break

    @classmethod
    def editar_contato(self):
        search = input("Insira o nome ou telefone:")
        for i in self.agenda:
            if i['nome'] == search:
                nome = input("insira o nome: ")
                telefone = input("insira o telefone: ")
                i['nome'] = nome
                i['telefone'] = telefone
                break
            if i['telefone'] == int(search):
                nome = input("insira o nome: ")
                telefone = input("insira o telefone: ")
                i['nome'] = nome
                i['telefone'] = telefone
                break
    
    @classmethod
    def excluir_contato(self):
        search = input("Insira o nome ou telefone:")
        for index,i in enumerate(self.agenda):
            if i['nome'] == search:
                self.agenda.pop(index)
                break
            if i['telefone'] == int(search):
                self.agenda.pop(index)
                break
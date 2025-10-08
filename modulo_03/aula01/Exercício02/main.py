from estudante import Estudante



    
aluno1 = Estudante("Ana Silva", 19, "Estudante", 12345, "Engenharia")
    

aluno1.adicionar_nota("Matemática", 9.5)    
aluno1.adicionar_nota("Matemática", 8.0)
aluno1.adicionar_nota("História", 7.5)
aluno1.adicionar_nota("Física", 10.0)
    

print("\n--- Informações do Estudante ---")
# Imprimir o objeto chama o método __str__ automaticamente
print(aluno1)
    
    
print("\n--- Acessando os atributos diretamente ---")
print(f"Nome do aluno: {aluno1.nome}")
print(f"Matrícula: {aluno1.matricula}")
print(f"Dicionário de notas: {aluno1.notas}")
print(f"Notas de Matemática: {aluno1.notas['Matemática']}")
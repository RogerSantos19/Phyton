alunos = {
    2312:{
        "nome":"tais",
        "email":"tais@gmail.com"
    }
}
matricula = int(input("qual a matricula?"))
if "tais" in alunos[matricula].values():
    print(alunos[matricula]) 

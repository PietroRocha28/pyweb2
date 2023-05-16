function confirmDelete(name, id){
    if(confirm("Você quer deletar " +name+"?")==true){
        window.open("deletar/"+id,'self')
    }
}
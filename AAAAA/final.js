function calcular() {
    let altura = Number(document.getElementById('altura').value)
    let peso = Number(document.querySelector('input#peso').value)
    let resposta = document.querySelector('div#mostruario')

    let imc = peso/(altura**2)
    
    if (peso == 0 || altura == 0 || !peso || !altura ){
        alert('Adicione numeros válidos ')
    } else if (imc < 18.5 ) {
        resposta.innerHTML = ` Você esta abaixo do peso ideal. Seu imc é de ${imc}`
    } else if (imc >= 18.5 && imc < 24.9) {
        resposta.innerHTML = `Você esta com o peso ideal. Seu imc é de ${imc}`
    } else if (imc >= 25 && imc <= 29.9) {
        resposta.innerHTML = `Você esta com sobrepeso. Seu imc é de ${imc}`
    } else if (imc >= 30 && imc <= 34.9) {
        resposta.innerHTML = ` Você esta com Obesidade grau 1. Seu imc é de ${imc}`
    } else if (imc >= 35 && imc <= 39.9){
        resposta.innerHTML = `Você esta com Obesidade grau 2. Seu imc é de ${imc}`
    } else {
        resposta.innerHTML = ` Você esta com Obesidade grau 3. Seu imc é de ${imc}`
    }
   
}
/**
 * 
 *  Formula Isodo para encontrar numeros perfeitos
 *  Autor: Riallis da Silva França
 *  Faculdade das Americas - FAM
**/


const tamanho = 150;

function numero_primo(n){
    
    if (n <= 3){
        return true
    }

    k = Math.sqrt(n)

    let count = 3 

    while (count <= k){
        if( (n % count) == 0){
            return false
        }
        
        count += 2
    }

    return true
}

for (let numero = 2; numero < tamanho; numero++) {
    
    var potencia = (Math.pow(2,numero) - 1)
    var primo = numero_primo(potencia)

    if(primo){
        console.log(`${potencia * Math.pow(2, (numero -1))} é um numero perfeito!`)
    }
    
}
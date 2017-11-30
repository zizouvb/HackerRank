function vowelsAndConsonants(s) {
   
    let vowels = ["a", "e", "i", "o", "u"];
    
    let arr = []
    for(let v of s) {
        if(vowels.includes(v))
            console.log(v)
        else {
            arr += v
        }
    }
    console.log(arr.split("").join('\n'))
}

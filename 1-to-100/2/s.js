function fiboEvenSum(n) {
    let a = 1;
    let b = 2 ;
    let c = a + b;
    let counter = 2;
    while( c <= n){
      if(c % 2 == 0 ){
        counter += c;
      }
      a = b ; 
      b = c;
      c = a + b;
    } 
    return counter;
}
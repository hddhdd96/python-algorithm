function solution(citations) {
    var answer = 0;
    citations.sort((a,b)=>b-a);
    let h = 0;
    
    while(h+1<=citations[h]) {
        h++;
        answer = h;
    }
    
    return answer;
}

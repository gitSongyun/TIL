function solution(n, m, section) {
    var answer = 0;
    
    while (section.length !== 0) {
        const start = section.shift()
        const end = start + m - 1
        let idx = 0
        answer += 1        
        for (let s of section) {
            if (end - s >= 0) {
                idx += 1
            } else {
                break
            }    
        }
        section = section.slice(idx)
        
    }
    
    return answer;
}
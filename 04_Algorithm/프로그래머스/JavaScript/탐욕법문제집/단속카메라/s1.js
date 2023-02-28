function solution(routes) {
    var answer = 0;
    let i = 0
    
    routes.sort((x,y)=> {
        return x[1]-y[1]
    })
    console.log(routes)
    let pos = 0
    while (i < routes.length) {
        
        if (i < routes.length) {
            pos = routes[i][1]
        }
        i +=1
        while (i < routes.length && pos >= routes[i][0] && routes[i][1] >= pos) {
            i+=1
        }
        answer += 1
        
    }
    return answer;
}

function solution(n, computers) {
    var answer = 0;
    let visited = [];
    
    for (let i=0; i<n; i++) {
        visited.push(false)   
    }
    
     for (let j=0; j<n; j++) {
        if (visited[j] === false) {
            bfs(j)
            answer += 1
        }                
     }
    
    function bfs(node) {
        let queue = [];
        queue.push(node);
        while (queue.length !== 0) {
            console.log(visited)
            let newNode = queue.shift()
            visited[newNode] = true
            for (let i=0; i<n; i++) {
                console.log(newNode, i)
                if (visited[i] === false) {
                    if(computers[newNode][i]===1){
                        visited[i] = true
                        queue.push(i)
                    }
                };
            };
        };
    
    };
    
    return answer;
}

// let visited = [false] *  

// computers 갯수 만큼 탐색
# 서로 매칭된 사람들 숫자 세기 

function solution(p) {
    var answer = 0;
    let like = {};

    for (let i of p) {
        if (!like[i[0]]) {
            like[i[0]] = [i[1]];
        } else {
            like[i[0]].push(i[1])
        }
        
        if (like[i[1]]) {
            if (like[i[1]].includes(i[0])) {
                answer += 1;
            } 
        }
    };
    
    return answer;
}


화살표로 <<<>> 레일이 주어지고, 어느 위치에 두면 탈출이 가능한지 

function solution(p){
    var answer = 0;
    let arrow = {'<' : -1, '>' : 1};
    // console.log(p_list)
    for (let i in p) {
        let cur = parseInt(i)
        let check = 0
        // console.log('새 시작', i)
        
        let startArrow = p[cur]

        if (startArrow === '<') {
            check = 0
        } else {
            check = p.length - 1
        }
        
        while (true) {
            let curArrow = p[cur]
            let nextArrow = p[cur+arrow[p[i]]]
            let next = cur + arrow[p[cur]]

            cur = next
            

            if (next < 0 || next > p.length-1) {
                break
            } else if (curArrow !== nextArrow) {
                cur = false
                break
            }
            if (curArrow != p[check]) {
                cur = false
                break
            } else if (startArrow === '<') {
                check += 1
            } else if (startArrow === '>') {
                check -= 1
            }
        }
        if (cur) {
            answer += 1
        }

    }
    return answer;
}



# 3 2 1 2 1 점수가 배열로 주어지고, 각각 순서대로 순위 매기기,   

function solution(grade) {
    var answer = [];
    let sortGrade = [...grade].sort(function(a, b) {return b- a});
    let rankObj = {};
    let rank = 0;
    let tmpRank = 0;
    let prevG = 0;
    
    sortGrade.map((v,i)=> {
        rank += 1;
        if (v == prevG) {
            rankObj[v] = tmpRank
        }else {
            rankObj[v] = rank
            tmpRank = rank
        }  
        prevG = v;
    });

    for (let i of grade) {
        answer.push(rankObj[i])
    };

    return answer;
}
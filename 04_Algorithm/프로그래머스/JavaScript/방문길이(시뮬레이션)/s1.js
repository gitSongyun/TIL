function solution(dirs) {
    var answer = 0;
    // 경로를 담을 배열
    let path = new Set()
    // 명령어 종류
    let command = {
        'U' : [-1, 0],
        'R' : [0, 1],
        'D' : [1, 0],
        'L' : [0, -1]
    };
    // 시작점
    let x = 5;
    let y = 5;
    // 이전 좌표
    let pre = '';
    // 명령을 수행하면서 경로를 path에 담는다.
    for (let dir of dirs) {
        pre = "" + x + y;
        [dx, dy] = command[dir];
        let nx = x + dx;
        let ny = y + dy;
        if (nx >= 0 && nx < 11 && ny >= 0 && ny < 11) {
            path.add(pre+""+nx+ny);
            path.add(""+nx+ny+pre);
            x = nx;
            y = ny;
        }
    }

    answer = path.size / 2;

    return answer;
}
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const loginBtn = document.querySelector("#theaterLoginBtn");

// 로그인 버튼 클릭 시 함수 실행
loginBtn.addEventListener('click', checkValue);
// 유효성 검사 함수
function checkValue () {
    // 이메일, 비밀번호 입력값 
    const emailValue = email.value;
    const passValue = password.value;

    // 이메일, 비밀번호 정규식 패턴
    let emailReg = new RegExp('^[a-zA-Z]([.]?[0-9a-zA-Z])*@[a-z]([-_.]?[0-9a-z])*.co');
    let pwReg = new RegExp('^.*(?=^.{8,20}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@~]).*$');
    
    // 정규식 검사 결과
    const emailCheck = emailReg.test(emailValue);
    const pwCheck = pwReg.test(passValue);

    // 둘 중 하나 이상 비어있거나 유효성 검사에 실패한 경우, 순차적으로 확인 후 잘못된 곳 alert 
    if (!emailValue.length || !passValue.length || !emailCheck || !pwCheck ) {
        if (!emailValue.length || !passValue.length) {
            window.alert('이메일 혹은 비밀번호가 입력되지 않았습니다.')
        } else {
            if (!emailCheck) {
                window.alert(' 이메일 형식이 올바르지 않습니다.')
            } else if (!pwCheck) {
                if (passValue.length <= 8 || passValue.length >= 20) {
                    window.alert(' 비밀번호는 최소 8자 이상, 최대 20자 이하로 구성해야 합니다.')
                } else {
                    window.alert('비밀번호는 영문, 숫자, 특수문자를 모두 포함해야 합니다.')
                }
            }
        }
    } else (
        window.alert('로그인 성공!')
    ) ;
}
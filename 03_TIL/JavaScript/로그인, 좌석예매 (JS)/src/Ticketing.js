const adultBtn = document.querySelector("#adultBtn");
const youthBtn = document.querySelector("#youthBtn");
const handiBtn = document.querySelector("#checkHandicap");

const adGroup = adultBtn.getElementsByClassName("btn");
const ytGroup = youthBtn.getElementsByClassName("btn");
handiBtn.setAttribute("disabled", true);

let adultNum = 0;
let youthNum = 0;
let totalNum = 0;

// 0명 기본 선택
adGroup[0].classList.replace("--general", "toggle");
ytGroup[0].classList.replace("--youth", "toggle");

// 어른 인원 선택
adultBtn.addEventListener("click", (e) => {
  const clickedBtn = e.target;
  const idx = clickedBtn.innerText;
  adultNum = parseInt(idx);
  // 선택한 인원만 toggle 속성 부여
  if (clickedBtn.classList[0] === "btn") {
    for (let i = 0; i < 9; i++) {
      if (i !== idx && adGroup[i].classList.contains("toggle")) {
        adGroup[i].classList.replace(["toggle"], ["--general"]);
      }
    }
    adGroup[idx].classList.replace(["--general"], ["toggle"]);
    calcNum();
  }
});

// 청소년 인원 선택
youthBtn.addEventListener("click", (e) => {
  const clickedBtn = e.target;
  const idx = clickedBtn.innerText;
  youthNum = parseInt(idx);
  if (clickedBtn.classList[0] === "btn") {
    // 선택한 인원만 toggle 속성 부여
    for (let i = 0; i < 9; i++) {
      if (i !== idx && ytGroup[i].classList.contains("toggle")) {
        ytGroup[i].classList.replace(["toggle"], ["--youth"]);
      }
    }
    ytGroup[idx].classList.replace(["--youth"], ["toggle"]);
    calcNum();
  }
});

// 총 인원
const calcNum = () => {
  totalNum = adultNum + youthNum;
  checkHandi();
};

const checkHandi = () => {
  // 장애인 체크박스
  if (totalNum === 0) {
    handiBtn.setAttribute("disabled", true);
  } else {
    handiBtn.removeAttribute("disabled");
  }
};
// 관람 인원 수 0명이면 선택 불가

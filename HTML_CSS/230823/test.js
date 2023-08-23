'use strict'
// 주석

// 변수 만드는 3가지 방법
// var a;
// let b;

// 상수 변수
const c = 3;

//  var와 let은 이런식으로 계속 수정 가능.
a = 3
a = 10

b = 4
b = 11

// c = 10 은 에러. 상수는 바꿀 수 없음.

var a = 1;
a = 3; c = 3; // 엄격모드에서는 이렇게 변수선언이 안 된다.



// length 속성을 통해 문자열의 길이를 구할 수 있음.
let myPassword = "qwer123!@#";
console.log(myPassword.length);
// 10



// 한번 만들어진 문자열은 절대 변하지 않음. 불변의 성질.
let 불멸자 = "immortal";
불멸자[0] = 'l';
console.log(불멸자);
// immortal

불멸자.toUpperCase();
console.log(불멸자);
// immortal



// 문자열은 +연산자로 연결될 수 있음.
let lyrics1 = '광야로 걸어가 ';
let lyrics2 = '알아 네 home ground';
'광야로 걸어가 알아 네 home ground' === lyrics1 + lyrics2;
// true



// indexOf 문자열 안에 존재하는 특정한 문자를 검색하여 문자의 인덱스를 반환. 
let text = "Next level 제껴라 제껴라 제껴라";
console.log(text.indexOf('level'));
// 5

console.log(text.indexOf('제껴라'));
// 11
console.log(text.indexOf('제껴라', 16));
// 19

console.log(text.indexOf('광야'));
// -1



// lastIndexOf 검색하는 순서가 indexOf()와 정반대. 인덱스 번호는 바뀌지 않음.
// let text = "Next level 제껴라 제껴라 제껴라";
console.log(text.lastIndexOf('level'));
// 5

console.log(text.lastIndexOf('제껴라'));
// 19
console.log(text.lastIndexOf('제껴라', 16));
// 15

console.log(text.lastIndexOf('광야'));
// -1



// match 메소드는 정규표현식을 인자로 받아 일치하는 문자열을 찾아 배열의 형태로 반환. (python re.findall)
console.log("Naevis 우리 ae, ae들을 불러봐".match(/ae/));
// g 플래그가 없는 경우 : ["ae"]

console.log("Naevis 우리 ae, ae들을 불러봐".match(/ae/g));
// g 플래그가 있는 경우 : ["ae", "ae", "ae"]

console.log("Naevis 우리 ae, ae들을 불러봐".match(/[a-zA-Z]\w+/g));
// w+ => 하나 이상의 문자로 이루어진 단어를 찾습니다 : ["Naevis", "ae", "ae"]



// replace 첫 번째 인자는 찾아야하는 문자열, 두 번째 인자는 대체할 값. 정규표현식을 지원.
console.log("제껴라 제껴라 제껴라 huh!".replace("제껴라", "check it out"));
// "check it out 제껴라 제껴라 huh!"

console.log("제껴라 제껴라 제껴라 huh!".replace(/제껴라/g, "check it out"));
// "check it out check it out check it out huh!"



// slice 시작 인덱스와 종료 인덱스를 인자로 전달. 문자열을 나눠 새로운 문자열 반환.
console.log("중심을 잃고 목소리도 잃고".slice(7));
// "목소리도 잃고"

console.log("중심을 잃고 목소리도 잃고".slice(7, 14));
// "목소리도 잃고"

console.log("중심을 잃고 목소리도 잃고".slice(-3));
// " 잃고"

console.log("중심을 잃고 목소리도 잃고".slice(-3, 13));
// " 잃"



// split 인자로 전달하는 구분자로 문자열을 쪼개어 각각의 값을 원소로 하는 "배열" 반환
console.log("La la la la la la".split(" "));
// ["La", "la", "la", "la", "la", "la"]

console.log("La la la la la la".split(""));
// ["L", "a", " ", "l", "a", " ", "l", "a", " ", "l", "a", " ", "l", "a", " ", "l", "a"]

console.log("La-la-la-la-la-la".split("-", 3));
// ["La", "la", "la"]



// toLowerCase, toUpperCase 문자열을 소문자, 혹은 대문자로 변환한 새로운 문자열을 생성하여 반환. (python upper, lower)
console.log("What's the name? Black mamba".toLowerCase());
// "what's the name? black mamba"

console.log("Watch me while I make it out".toUpperCase());
// "WATCH ME WHILE I MAKE IT OUT"



// trim() 문자열 앞 뒤의 공백을 제거. (python strip)
console.log("         abc  ".trim());
// "abc"



// padStart() 자릿수에 맞춰 값 채우기. (python  rjust)
let str = '99'
console.log(str.padStart(5, '0')); // '99'를 5자리 채웁니다. 부족한 부분은 0으로 채웁니다.
// "00099"
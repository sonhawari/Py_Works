function hello(){
  console.log("hello world!");
}

function helloYou(naame){
  console.log("Hello "+ name); }


function addNum(num1,num2){
  console.log(num1+num2);
}


function helloSomeone(name="Frank"){
  console.log("hello " + name)
}

function formal(name="aa",title="bb"){
  console.log(title + " " + name);
}


function formalr(name="aa",title="bb"){
  return title + " " + name
}


function timesFice(numinput){
  var result = numinput * 5
  return result
}


//Global SCOPE

var v = "GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff){
  console.log(v);
  stuff = "reassing stıff"
  console.log(stuff);
}

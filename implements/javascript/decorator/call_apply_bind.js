"use strict";

function hello(arg0, arg1) {
  console.log(this, this.value, arg0, arg1);
}

let object1 = { value: "value of obj" };

object1.func = hello;
object1.func(1, 2);

// 以 object1 臨時作為 hello's this
hello.call(object1, 1, 2);
hello.apply(object1, [1, 2]);

// 以 object1 替換 hello's this
hello.bind(object1)(1, 2);
// hello(1, 2); // TypeError

// 以 object1 替換 hello's this, 再把新的 hello 保存起來
hello = hello.bind(object1);
hello(1, 2);

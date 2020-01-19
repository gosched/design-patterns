function foo() {
  console.log(...arguments);
}

function wrapper(func) {
  const wrappedFunction = function() {
    console.log("before");
    const result = func.apply(this, arguments);
    console.log("after");
    return result;
  };
  return wrappedFunction;
}

const wrappedFoo = wrapper(foo);
wrappedFoo("bar", "baz");

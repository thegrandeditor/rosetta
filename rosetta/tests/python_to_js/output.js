function my_decorator(func) {
  return func;
}
class Base {
  greet() {
    return 'Hello';
  }
}
class Derived extends Base {
  /* @my_decorator */
  async process_data(items) {
    result = items.filter(x => (x > 0)).map(x => (x * 2));
    return result;
  }
  *my_generator() {
    yield 1
    yield 2
  }
}
async function main() {
  d = new Derived();
  console.log(await d.process_data([1, 2, -1]))
}

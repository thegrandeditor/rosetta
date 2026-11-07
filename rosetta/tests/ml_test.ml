val x = 5;
fun square n = n * n;
val y = square x;
datatype shape = Circle of int | Rect of int * int;
val s = Circle 10;
case s of
  Circle r => r * r
| Rect (w, h) => w * h;
let
  val a = 1
in
  a + 1
end;

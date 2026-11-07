PROGRAM Hello;
VAR
  i : Integer;
  sum : Integer;
BEGIN
  sum := 0;
  FOR i := 1 TO 10 DO
  BEGIN
    sum := sum + i;
  END;
  WRITELN('Sum is ', sum);
END.
